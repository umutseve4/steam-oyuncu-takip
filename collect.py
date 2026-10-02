"""
collect.py — Steam'den anlık oyuncu sayılarını çeker ve SQLite veritabanına yazar.

Çalıştırma:  python collect.py
Her çalıştırmada her oyun için 1 satır eklenir. Saatlik çalıştırırsan zaman serisi oluşur.
Sadece Python standart kütüphanesi kullanır (kurulum gerekmez).
"""
import json
import sqlite3
import time
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

# İzlenecek oyunlar: {Steam app ID: oyun adı}
GAMES = {
    1237970: "Titanfall 2",
    359550: "Rainbow Six Siege",
    1237950: "Star Wars Battlefront II",
    243470: "Watch Dogs",
    447040: "Watch Dogs 2",
}

API_URL = "https://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v1/?appid={app_id}"
DB_PATH = Path(__file__).parent / "data" / "steam.db"


# --- EXTRACT (veriyi çek) ---------------------------------------------------
def fetch_player_count(app_id: int, retries: int = 3) -> int | None:
    """Bir oyunun anlık oyuncu sayısını döndürür. Hata olursa birkaç kez dener."""
    url = API_URL.format(app_id=app_id)
    for attempt in range(1, retries + 1):
        try:
            with urllib.request.urlopen(url, timeout=10) as resp:
                data = json.load(resp)
            if data["response"].get("result") == 1:
                return int(data["response"]["player_count"])
            print(f"  ! {app_id}: API başarısız sonuç döndü: {data}")
            return None
        except Exception as e:  # ağ hatası, zaman aşımı vb.
            print(f"  ! {app_id}: deneme {attempt}/{retries} başarısız ({e})")
            time.sleep(2 * attempt)
    return None


# --- LOAD (veritabanına yaz) -------------------------------------------------
def init_db(conn: sqlite3.Connection) -> None:
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS player_counts (
            id           INTEGER PRIMARY KEY AUTOINCREMENT,
            collected_at TEXT    NOT NULL,   -- UTC, ISO formatında
            app_id       INTEGER NOT NULL,
            game_name    TEXT    NOT NULL,
            player_count INTEGER NOT NULL
        )
        """
    )
    conn.commit()


def save_rows(conn: sqlite3.Connection, rows: list[tuple]) -> None:
    conn.executemany(
        "INSERT INTO player_counts (collected_at, app_id, game_name, player_count) VALUES (?, ?, ?, ?)",
        rows,
    )
    conn.commit()


def main() -> None:
    DB_PATH.parent.mkdir(exist_ok=True)
    now = datetime.now(timezone.utc).replace(microsecond=0).isoformat()

    rows = []
    for app_id, name in GAMES.items():
        count = fetch_player_count(app_id)
        if count is None:
            continue  # bu oyunu atla, diğerlerine devam et
        print(f"{name:<26} {count:>8,} oyuncu")
        rows.append((now, app_id, name, count))

    with sqlite3.connect(DB_PATH) as conn:
        init_db(conn)
        save_rows(conn, rows)

    print(f"\n{len(rows)}/{len(GAMES)} oyun kaydedildi -> {DB_PATH} ({now})")


if __name__ == "__main__":
    main()
