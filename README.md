# 🎮 Steam Oyuncu Takip — ETL Pipeline

Sevdiğim oyunların Steam'deki **anlık oyuncu sayılarını** her saat, **fiyat / indirim / yorum puanını** her gün
otomatik toplayan, SQLite'ta saklayan, **SQL ile analiz eden** ve **interaktif bir HTML panoda** gösteren veri mühendisliği projesi.

🔗 **Canlı pano:** https://umutseve4.github.io/steam-oyuncu-takip/  
🔎 **SQL analizi (otomatik):** [reports/sql_analiz.md](reports/sql_analiz.md)

```
Steam Web API ──> collect.py ──┐
                               ├──> data/steam.db ──> analyze.py (queries.sql) ──> reports/sql_analiz.md
Steam Store API ─> store.py ───┘                  └─> dashboard.py ──> docs/index.html (GitHub Pages)
        ▲
        └──── GitHub Actions (her saat başı otomatik) ────
```

## İzlenen oyunlar
| Oyun | Steam App ID |
|---|---|
| Titanfall 2 | 1237970 |
| Rainbow Six Siege | 359550 |
| Star Wars Battlefront II | 1237950 |
| Watch Dogs | 243470 |
| Watch Dogs 2 | 447040 |

Yeni oyun eklemek için `collect.py` içindeki `GAMES` sözlüğüne app ID ekle
(ID, oyunun Steam mağaza linkinde yazar: `store.steampowered.com/app/<ID>/...`).

## Dosyalar
| Dosya | Görevi |
|---|---|
| `collect.py` | Steam API'den anlık oyuncu sayılarını çeker → `player_counts` tablosu |
| `store.py` | Fiyat, indirim, tür, toplam/olumlu yorum, Steam puanı → `game_details` tablosu (günde 1 snapshot) |
| `queries.sql` | 6 analiz sorgusu: zirve saat (`RANK`), günlük değişim (`LAG`), sıralama (`DENSE_RANK`), oynaklık, hafta içi/sonu, mağaza `JOIN` |
| `analyze.py` | `queries.sql`'i çalıştırır → `reports/sql_analiz.md` |
| `dashboard.py` | İnteraktif HTML pano (grafik + fiyat/yorum kartları) → `docs/index.html` |
| `report.py` | Terminal özeti + PNG grafik (pandas/matplotlib) |
| `.github/workflows/collect.yml` | Her saat tüm hattı çalıştırıp sonucu commit eder |

## Bulutta otomatik çalışma (bilgisayar kapalıyken de)
GitHub Actions her saat başı (UTC) `collect.py` → `store.py` → `analyze.py` → `dashboard.py` çalıştırır ve sonucu repoya commit eder.
Elle tetiklemek için: **Actions → Saatlik veri toplama → Run workflow**.

**GitHub Pages (bir kerelik ayar):** Settings → Pages → Source: *Deploy from a branch* →
Branch: `main`, klasör: `/docs` → Save.

## Yerelde çalıştırma
```
python collect.py      # oyuncu sayıları
python store.py        # fiyat + yorumlar (günde 1 kez; --force ile yenile)
python analyze.py      # SQL analizi -> reports/sql_analiz.md
python dashboard.py    # docs/index.html'i üret -> tarayıcıda aç
pip install -r requirements.txt && python report.py   # (opsiyonel) PNG grafik
```

## Veritabanı şeması
```
player_counts(id, collected_at [UTC ISO], app_id, game_name, player_count)
game_details(snapshot_date, app_id, game_name, currency, initial_price_cents, final_price_cents,
             discount_percent, total_reviews, positive_reviews, review_desc, genres, release_date)
             PRIMARY KEY (snapshot_date, app_id)
```

## Yol haritası
- [x] Saatlik otomatik toplama (GitHub Actions)
- [x] İnteraktif HTML pano (GitHub Pages)
- [x] SQL analizi: zirve saat, günlük değişim, sıralama, oynaklık (window functions)
- [x] Mağaza verisi: fiyat, indirim, yorum puanı
- [ ] İndirim dönemlerinde oyuncu sayısı artıyor mu? (fiyat × oyuncu korelasyonu)
- [ ] SQLite → PostgreSQL, script → Airflow
