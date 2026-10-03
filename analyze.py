"""
analyze.py — queries.sql içindeki SQL sorgularını çalıştırır, sonucu terminale ve
reports/sql_analiz.md dosyasına (GitHub'da tablo olarak görünür) yazar.

Çalıştırma:  python analyze.py
Sadece Python standart kütüphanesi kullanır.
"""
import re
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

BASE = Path(__file__).parent
DB_PATH = BASE / "data" / "steam.db"
SQL_PATH = BASE / "queries.sql"
OUT = BASE / "reports" / "sql_analiz.md"


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
            except sqlite3.OperationalError as e:   # ör. game_details tablosu henüz yok
                table = f"_Atlandı: {e}_"
            print(f"\n=== {title}\n{table}")
            md.append(f"## {title}\n\n{table}\n")

    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text("\n".join(md), encoding="utf-8")
    print(f"\nRapor yazıldı -> {OUT}")


if __name__ == "__main__":
    main()
