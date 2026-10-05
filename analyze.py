"""
analyze.py — queries.sql içindeki SQL sorgularını çalıştırır, sonucu terminale ve
reports/sql_analiz.md dosyasına (GitHub'da tablo olarak görünür) yazar.
Ayrıca indirim × oyuncu sayısı korelasyonunu (Pearson r) hesaplar.

Çalıştırma:  python analyze.py
Sadece Python standart kütüphanesi kullanır.
"""
import re
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from statistics import StatisticsError, correlation

BASE = Path(__file__).parent
DB_PATH = BASE / "data" / "steam.db"
SQL_PATH = BASE / "queries.sql"
OUT = BASE / "reports" / "sql_analiz.md"

# Günlük ortalama oyuncu sayısı + o günün mağaza snapshot'ı (indirim yüzdesi)
CORR_SQL = """
WITH daily AS (
    SELECT app_id, date(collected_at) AS gun, AVG(player_count) AS ort
    FROM player_counts
    GROUP BY app_id, gun
)
SELECT g.game_name, COALESCE(g.discount_percent, 0), d.ort
FROM daily d
JOIN game_details g ON g.app_id = d.app_id AND g.snapshot_date = d.gun
ORDER BY g.game_name, d.gun
"""


def load_queries() -> list[tuple[str, str]]:
    """'-- name: Başlık' satırlarına göre dosyayı (başlık, sorgu) çiftlerine böler."""
    parts = re.split(r"^-- name:\s*(.+)$", SQL_PATH.read_text(encoding="utf-8"), flags=re.M)
    return [(parts[i].strip(), parts[i + 1].strip()) for i in range(1, len(parts), 2)]


def fmt(v) -> str:
    if v is None:
        return "–"
    if isinstance(v, float):
        return f"{v:,.2f}".rstrip("0").rstrip(".") if v % 1 else f"{int(v):,}"
    if isinstance(v, int):
        return f"{v:,}"
    return str(v)


def to_markdown(cols: list[str], rows: list[tuple]) -> str:
    if not rows:
        return "_Henüz veri yok._"
    head = "| " + " | ".join(cols) + " |\n|" + "---|" * len(cols)
    body = "\n".join("| " + " | ".join(fmt(v) for v in r) + " |" for r in rows)
    return head + "\n" + body


def interpret(r: float) -> str:
    a = abs(r)
    strength = "çok zayıf" if a < 0.2 else "zayıf" if a < 0.4 else "orta" if a < 0.6 else "güçlü"
    return f"{strength} {'pozitif' if r > 0 else 'negatif'}"


def discount_correlation(conn: sqlite3.Connection) -> tuple[list[str], list[tuple]]:
    """Her oyun için indirim yüzdesi ile günlük ortalama oyuncu arasındaki Pearson r."""
    data: dict[str, tuple[list[float], list[float]]] = {}
    for game, disc, avg in conn.execute(CORR_SQL):
        xs, ys = data.setdefault(game, ([], []))
        xs.append(float(disc))
        ys.append(float(avg))

    rows = []
    for game, (xs, ys) in data.items():
        if len(xs) < 3:
            rows.append((game, len(xs), None, "hesaplanamadı (en az 3 günlük mağaza verisi gerekli)"))
            continue
        try:
            r = correlation(xs, ys)
            rows.append((game, len(xs), f"{r:+.3f}", interpret(r)))
        except StatisticsError:  # indirim (veya oyuncu sayısı) hiç değişmemiş
            note = "indirim hiç değişmedi" if len(set(xs)) <= 1 else "oyuncu sayısı sabit"
            rows.append((game, len(xs), None, f"hesaplanamadı ({note})"))
    return ["oyun", "gun_sayisi", "pearson_r", "yorum"], rows


def main() -> None:
    if not DB_PATH.exists():
        raise SystemExit("Veritabanı yok. Önce 'python collect.py' çalıştır.")

    now = datetime.now(timezone.utc).strftime("%d.%m.%Y %H:%M")
    md = [f"# 🔎 SQL Analizi\n\n_Otomatik üretildi: {now} UTC · sorgular: [`queries.sql`](../queries.sql)_\n"]

    with sqlite3.connect(DB_PATH) as conn:
        for title, sql in load_queries():
            try:
                cur = conn.execute(sql)
                cols = [c[0] for c in cur.description]
                rows = cur.fetchall()
                table = to_markdown(cols, rows[:50])
            except sqlite3.Error as e:   # ör. game_details tablosu henüz yok
                table = f"_Atlandı: {e}_"
            print(f"\n=== {title}\n{table}")
            md.append(f"## {title}\n\n{table}\n")

        title = "8. İndirim × oyuncu sayısı korelasyonu (Pearson r, Python)"
        try:
            table = to_markdown(*discount_correlation(conn))
        except sqlite3.Error as e:
            table = f"_Atlandı: {e}_"
        note = ("> r ≈ +1: indirim arttıkça oyuncu artıyor · r ≈ 0: ilişki yok · r ≈ −1: ters ilişki. "
                "Korelasyon nedensellik değildir; birkaç günlük veriyle sonuç güvenilir olmaz.")
        print(f"\n=== {title}\n{table}")
        md.append(f"## {title}\n\n{table}\n\n{note}\n")

    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text("\n".join(md), encoding="utf-8")
    print(f"\nRapor yazıldı -> {OUT}")


if __name__ == "__main__":
    main()
