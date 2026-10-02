"""
report.py — Toplanan verilerden özet tablo ve grafik üretir.

Çalıştırma:  python report.py
Çıktı: terminalde özet + reports/oyuncu_grafigi.png
"""
import sqlite3
from pathlib import Path

import matplotlib

matplotlib.use("Agg")  # ekran olmadan da grafik kaydedebilsin
import matplotlib.pyplot as plt
import pandas as pd

BASE = Path(__file__).parent
DB_PATH = BASE / "data" / "steam.db"
OUT_DIR = BASE / "reports"


def load_data() -> pd.DataFrame:
    if not DB_PATH.exists():
        raise SystemExit("Veritabanı yok. Önce 'python collect.py' çalıştır.")
    with sqlite3.connect(DB_PATH) as conn:
        df = pd.read_sql("SELECT collected_at, game_name, player_count FROM player_counts", conn)
    df["collected_at"] = pd.to_datetime(df["collected_at"])
    return df


# --- TRANSFORM (özetle) ------------------------------------------------------
def summarize(df: pd.DataFrame) -> pd.DataFrame:
    summary = (
        df.sort_values("collected_at")
        .groupby("game_name")["player_count"]
        .agg(son="last", ortalama="mean", min="min", max="max", olcum_sayisi="count")
        .round(0)
        .astype(int)
        .sort_values("son", ascending=False)
    )
    return summary


def plot(df: pd.DataFrame) -> Path:
    OUT_DIR.mkdir(exist_ok=True)
    pivot = df.pivot_table(index="collected_at", columns="game_name", values="player_count")
    ax = pivot.plot(figsize=(11, 6), marker="o", markersize=3)
    ax.set_title("Steam anlık oyuncu sayıları")
    ax.set_xlabel("Zaman (UTC)")
    ax.set_ylabel("Oyuncu sayısı")
    ax.grid(alpha=0.3)
    ax.legend(title="Oyun")
    plt.tight_layout()
    out = OUT_DIR / "oyuncu_grafigi.png"
    plt.savefig(out, dpi=120)
    plt.close()
    return out


def main() -> None:
    df = load_data()
    print(f"Toplam {len(df)} ölçüm, {df['collected_at'].nunique()} farklı zaman\n")
    print(summarize(df).to_string())
    print(f"\nGrafik kaydedildi -> {plot(df)}")


if __name__ == "__main__":
    main()
