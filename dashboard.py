"""
dashboard.py — Veritabanındaki verilerden tarayıcıda açılabilen interaktif bir HTML panosu üretir.

Çalıştırma:  python dashboard.py
Çıktı: docs/index.html  (çift tıkla aç; GitHub Pages ile internette de yayınlanır)
"""
import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

BASE = Path(__file__).parent
DB_PATH = BASE / "data" / "steam.db"
OUT = BASE / "docs" / "index.html"

COLORS = ["#ff6b35", "#4ecdc4", "#ffd23f", "#ee4266", "#3a86ff", "#8338ec", "#06d6a0"]


def load() -> dict:
    if not DB_PATH.exists():
        raise SystemExit("Veritabanı yok. Önce 'python collect.py' çalıştır.")
    with sqlite3.connect(DB_PATH) as conn:
        rows = conn.execute(
            "SELECT collected_at, game_name, player_count FROM player_counts ORDER BY collected_at"
        ).fetchall()
    series: dict[str, list] = {}
    for ts, game, count in rows:
        series.setdefault(game, []).append({"x": ts, "y": count})
    return series


def load_store() -> dict:
    """store.py'nin yazdığı en güncel mağaza verisi (tablo yoksa boş döner)."""
    with sqlite3.connect(DB_PATH) as conn:
        try:
            rows = conn.execute(
                """SELECT game_name, currency, final_price_cents, discount_percent,
                          total_reviews, positive_reviews, review_desc
                   FROM game_details
                   WHERE snapshot_date = (SELECT MAX(snapshot_date) FROM game_details)"""
            ).fetchall()
        except sqlite3.OperationalError:
            return {}
    out = {}
    for name, cur, price, disc, total, pos, desc in rows:
        out[name] = {
            "price": None if price is None else ("Ücretsiz" if cur == "FREE" else f"{price / 100:.2f} {cur}"),
            "discount": disc or 0,
            "positive": round(100 * pos / total, 1) if total else None,
            "reviews": total, "desc": desc,
        }
    return out


def stats(series: dict, store: dict) -> list[dict]:
    out = []
    for game, pts in series.items():
        ys = [p["y"] for p in pts]
        first, last = ys[0], ys[-1]
        change = ((last - first) / first * 100) if first else 0
        peak = max(pts, key=lambda p: p["y"])
        out.append({
            "game": game, "last": last, "avg": round(sum(ys) / len(ys)),
            "min": min(ys), "max": peak["y"], "peak_at": peak["x"],
            "change": round(change, 1), "n": len(ys),
            "store": store.get(game),
        })
    return sorted(out, key=lambda s: s["last"], reverse=True)


HTML = """<!DOCTYPE html>
<html lang="tr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Steam Oyuncu Takip</title>
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/chartjs-adapter-date-fns@3.0.0/dist/chartjs-adapter-date-fns.bundle.min.js"></script>
<style>
  :root { --bg:#0f1117; --card:#181b24; --text:#e8e8ea; --muted:#8b8fa3; --border:#262a36; }
  * { box-sizing:border-box; }
  body { margin:0; font-family:system-ui,-apple-system,"Segoe UI",Roboto,sans-serif; background:var(--bg); color:var(--text); }
  .wrap { max-width:1150px; margin:0 auto; padding:28px 18px 50px; }
  h1 { margin:0 0 4px; font-size:28px; }
  .sub { color:var(--muted); margin-bottom:24px; font-size:14px; }
  .cards { display:grid; grid-template-columns:repeat(auto-fit,minmax(200px,1fr)); gap:14px; margin-bottom:22px; }
  .card { background:var(--card); border:1px solid var(--border); border-radius:14px; padding:16px; border-top:4px solid var(--c); }
  .card .name { color:var(--muted); font-size:13px; margin-bottom:6px; }
  .card .num { font-size:30px; font-weight:700; }
  .card .delta { font-size:13px; margin-top:4px; }
  .card .shop { font-size:12px; color:var(--muted); margin-top:8px; border-top:1px solid var(--border); padding-top:8px; }
  .tag { background:#06d6a0; color:#0f1117; border-radius:5px; padding:1px 5px; font-weight:700; margin-left:4px; }
  .up { color:#06d6a0; } .down { color:#ee4266; }
  .panel { background:var(--card); border:1px solid var(--border); border-radius:14px; padding:18px; margin-bottom:22px; overflow-x:auto; }
  .panel h2 { margin:0 0 12px; font-size:17px; }
  .chart-box { position:relative; height:420px; }
  table { width:100%; border-collapse:collapse; font-size:14px; }
  th,td { padding:10px 8px; text-align:right; border-bottom:1px solid var(--border); white-space:nowrap; }
  th:first-child,td:first-child { text-align:left; }
  th { color:var(--muted); font-weight:600; }
  .dot { display:inline-block; width:10px; height:10px; border-radius:50%; margin-right:8px; }
  .btns button { background:var(--border); color:var(--text); border:0; border-radius:8px; padding:6px 12px; margin:0 6px 10px 0; cursor:pointer; }
  .btns button.active { background:#3a86ff; }
  footer { color:var(--muted); font-size:12px; text-align:center; line-height:1.8; }
  a { color:#4ecdc4; }
</style>
</head>
<body>
<div class="wrap">
  <h1>🎮 Steam Oyuncu Takip</h1>
  <div class="sub">Anlık oyuncu sayıları · __N__ ölçüm · Son güncelleme: __UPDATED__ (UTC)</div>

  <div class="cards" id="cards"></div>

  <div class="panel">
    <h2>📈 Zaman içinde oyuncu sayısı</h2>
    <div class="btns">
      <button data-r="24" >Son 24 saat</button>
      <button data-r="168">Son 7 gün</button>
      <button data-r="0" class="active">Tümü</button>
    </div>
    <div class="chart-box"><canvas id="line"></canvas></div>
  </div>

  <div class="panel">
    <h2>📊 Özet istatistikler</h2>
    <table>
      <thead><tr><th>Oyun</th><th>Son</th><th>Ortalama</th><th>Min</th><th>Max</th><th>Zirve zamanı</th><th>Değişim</th><th>Fiyat</th><th>Olumlu yorum</th></tr></thead>
      <tbody id="tbody"></tbody>
    </table>
  </div>

  <footer>Veri: Steam Web API (GetNumberOfCurrentPlayers) + Steam Store API (appdetails, appreviews)<br>
    🔎 <a href="https://github.com/umutseve4/steam-oyuncu-takip/blob/main/reports/sql_analiz.md">SQL analizi</a> ·
    Kaynak kod: <a href="https://github.com/umutseve4/steam-oyuncu-takip">github.com/umutseve4/steam-oyuncu-takip</a></footer>
</div>

<script>
const SERIES = __SERIES__;
const STATS  = __STATS__;
const COLORS = __COLORS__;
const fmt = n => n.toLocaleString("tr-TR");
const color = {}; Object.keys(SERIES).forEach((g,i) => color[g] = COLORS[i % COLORS.length]);

const shop = s => !s.store ? "" : `<div class="shop">💲 ${s.store.price ?? "–"}${s.store.discount ? `<span class="tag">-%${s.store.discount}</span>` : ""}
  · 👍 ${s.store.positive != null ? "%" + s.store.positive : "–"} <span title="Steam puanı">${s.store.desc ?? ""}</span></div>`;

document.getElementById("cards").innerHTML = STATS.map(s => `
  <div class="card" style="--c:${color[s.game]}">
    <div class="name">${s.game}</div>
    <div class="num">${fmt(s.last)}</div>
    <div class="delta ${s.change>=0?'up':'down'}">${s.change>=0?'▲':'▼'} %${Math.abs(s.change)} (ilk ölçüme göre)</div>
    ${shop(s)}
  </div>`).join("");

document.getElementById("tbody").innerHTML = STATS.map(s => `
  <tr><td><span class="dot" style="background:${color[s.game]}"></span>${s.game}</td>
  <td>${fmt(s.last)}</td><td>${fmt(s.avg)}</td><td>${fmt(s.min)}</td><td>${fmt(s.max)}</td>
  <td>${new Date(s.peak_at).toLocaleString("tr-TR",{timeZone:"UTC"})}</td>
  <td class="${s.change>=0?'up':'down'}">${s.change>=0?'+':''}${s.change}%</td>
  <td>${s.store?.price ?? "–"}</td>
  <td>${s.store?.positive != null ? "%" + s.store.positive + " (" + fmt(s.store.reviews) + ")" : "–"}</td></tr>`).join("");

Chart.defaults.color = "#8b8fa3"; Chart.defaults.borderColor = "#262a36";
const chart = new Chart(document.getElementById("line"), {
  type: "line",
  data: { datasets: Object.entries(SERIES).map(([g, pts]) => ({
    label: g, data: pts, borderColor: color[g], backgroundColor: color[g],
    tension: .3, pointRadius: 2, borderWidth: 2 })) },
  options: {
    responsive: true, maintainAspectRatio: false,
    interaction: { mode: "index", intersect: false },
    scales: { x: { type: "time", time: { tooltipFormat: "dd.MM.yyyy HH:mm" } },
              y: { beginAtZero: true, ticks: { callback: v => fmt(v) } } },
    plugins: { tooltip: { callbacks: { label: c => `${c.dataset.label}: ${fmt(c.parsed.y)}` } } }
  }
});

const allX = Object.values(SERIES).flat().map(p => new Date(p.x).getTime());
const maxX = Math.max(...allX);
document.querySelectorAll(".btns button").forEach(b => b.onclick = () => {
  document.querySelectorAll(".btns button").forEach(x => x.classList.remove("active"));
  b.classList.add("active");
  const h = +b.dataset.r;
  chart.options.scales.x.min = h ? maxX - h * 3600e3 : undefined;
  chart.update();
});
</script>
</body>
</html>
"""


def main() -> None:
    series = load()
    st = stats(series, load_store())
    n = sum(s["n"] for s in st)
    html = (HTML
            .replace("__SERIES__", json.dumps(series))
            .replace("__STATS__", json.dumps(st))
            .replace("__COLORS__", json.dumps(COLORS))
            .replace("__N__", f"{n:,}".replace(",", "."))
            .replace("__UPDATED__", datetime.now(timezone.utc).strftime("%d.%m.%Y %H:%M")))
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(html, encoding="utf-8")
    print(f"Pano oluşturuldu -> {OUT}  (tarayıcıda aç)")


if __name__ == "__main__":
    main()
