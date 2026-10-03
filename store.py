"""
store.py — Steam mağaza verisini (fiyat, indirim, yorum puanı) çeker ve günde 1 kez SQLite'a yazar.

Çalıştırma:  python store.py            (bugün zaten kayıt varsa atlar)
             python store.py --force    (bugünkü kaydı yenile)
Kaynaklar:
  - store.steampowered.com/api/appdetails?appids=<ID>&cc=tr   -> fiyat / indirim / tür / çıkış tarihi
  - store.steampowered.com/appreviews/<ID>?json=1             -> toplam / olumlu yorum, Steam puanı
Sadece Python standart kütüphanesi kullanır.
"""
import json
import sqlite3
import sys
import time
import urllib.request
from datetime import datetime, timezone

from collect import DB_PATH, GAMES

DETAILS_URL = "https://store.steampowered.com/api/appdetails?appids={app_id}&cc=tr&l=english"
REVIEWS_URL = ("https://store.steampowered.com/appreviews/{app_id}"
               "?json=1&language=all&purchase_type=all&num_per_page=0")
HEADERS = {"User-Agent": "steam-oyuncu-takip (github.com/umutseve4/steam-oyuncu-takip)"}


def get_json(url: str, retries: int = 3) -> dict | None:
    for attempt in range(1, retries + 1):
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=15) as resp:
                return json.load(resp)
        except Exception as e:
            print(f"  ! deneme {attempt}/{retries} başarısız ({e})")
            time.sleep(3 * attempt)
    return None


# --- EXTRACT + TRANSFORM -----------------------------------------------------
def fetch_game(app_id: int, name: str) -> dict | None:
    details = get_json(DETAILS_URL.format(app_id=app_id))
    reviews = get_json(REVIEWS_URL.format(app_id=app_id))
    if not details or not details.get(str(app_id), {}).get("success"):
        print(f"  ! {name}: mağaza verisi alınamadı")
        return None

    d = details[str(app_id)]["data"]
    price = d.get("price_overview") or {}                    # ücretsiz oyunlarda yok
    q = (reviews or {}).get("query_summary", {})
    return {
        "app_id": app_id,
        "game_name": name,
        "currency": price.get("currency", "FREE" if d.get("is_free") else None),
        "initial_price_cents": price.get("initial", 0 if d.get("is_free") else None),
        "final_price_cents": price.get("final", 0 if d.get("is_free") else None),
        "discount_percent": price.get("discount_percent", 0),
        "total_reviews": q.get("total_reviews"),
        "positive_reviews": q.get("total_positive"),
        "review_desc": q.get("review_score_desc"),
        "genres": ", ".join(g["description"] for g in d.get("genres", [])),
        "release_date": (d.get("release_date") or {}).get("date"),
    }


# --- LOAD --------------------------------------------------------------------
def init_db(conn: sqlite3.Connection) -> None:
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS game_details (
            snapshot_date       TEXT    NOT NULL,   -- UTC gün (YYYY-MM-DD)
            app_id              INTEGER NOT NULL,
            game_name           TEXT    NOT NULL,
            currency            TEXT,
            initial_price_cents INTEGER,            -- indirimsiz fiyat (kuruş/cent)
            final_price_cents   INTEGER,            -- indirimli fiyat
            discount_percent    INTEGER,
            total_reviews       INTEGER,
            positive_reviews    INTEGER,
            review_desc         TEXT,               -- ör. "Very Positive"
            genres              TEXT,
            release_date        TEXT,
            PRIMARY KEY (snapshot_date, app_id)
        )
        """
    )
    conn.commit()


def main() -> None:
    force = "--force" in sys.argv
    today = datetime.now(timezone.utc).date().isoformat()
    DB_PATH.parent.mkdir(exist_ok=True)

    with sqlite3.connect(DB_PATH) as conn:
        init_db(conn)
        done = conn.execute("SELECT COUNT(*) FROM game_details WHERE snapshot_date = ?", (today,)).fetchone()[0]
        if done and not force:
            print(f"Bugünün ({today}) mağaza verisi zaten var, atlanıyor. (--force ile yenile)")
            return

        rows = []
        for app_id, name in GAMES.items():
            g = fetch_game(app_id, name)
            if g:
                price = "?" if g["final_price_cents"] is None else f"{g['final_price_cents'] / 100:.2f} {g['currency']}"
                print(f"{name:<26} {price:>14}  %{g['discount_percent']:<3} indirim  {g['review_desc']}")
                rows.append({"snapshot_date": today, **g})
            time.sleep(1.5)  # mağaza API'sine nazik ol (rate limit)

        conn.executemany(
            """INSERT OR REPLACE INTO game_details VALUES (
                   :snapshot_date, :app_id, :game_name, :currency, :initial_price_cents, :final_price_cents,
                   :discount_percent, :total_reviews, :positive_reviews, :review_desc, :genres, :release_date)""",
            rows,
        )
        conn.commit()
    print(f"\n{len(rows)}/{len(GAMES)} oyunun mağaza verisi kaydedildi ({today})")


if __name__ == "__main__":
    main()
