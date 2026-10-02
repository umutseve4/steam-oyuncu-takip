# 🎮 Steam Oyuncu Takip — İlk Veri Hattım (ETL Pipeline)

Sevdiğim oyunların Steam'deki **anlık oyuncu sayılarını** her saat otomatik toplayan,
SQLite veritabanında saklayan ve **interaktif bir HTML panoda** gösteren veri mühendisliği projesi.

🔗 **Canlı pano:** https://umutseve4.github.io/steam-oyuncu-takip/

```
Steam API ──(Extract)──> collect.py ──(Load)──> data/steam.db ──(Transform)──> dashboard.py ──> docs/index.html
                 ▲                                                                                │
                 └──────────── GitHub Actions (her saat başı otomatik) ───────────────────────────┘
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
| `collect.py` | Steam API'den oyuncu sayılarını çeker, `data/steam.db`'ye yazar (sadece standart kütüphane) |
| `dashboard.py` | Veritabanından interaktif HTML pano üretir → `docs/index.html` |
| `report.py` | Terminal özeti + PNG grafik (pandas/matplotlib) |
| `.github/workflows/collect.yml` | Her saat collect + dashboard çalıştırıp sonucu commit eder |

## Bulutta otomatik çalışma (bilgisayar kapalıyken de)
GitHub Actions her saat başı (UTC) `collect.py` + `dashboard.py` çalıştırır ve sonucu repoya commit eder.
Elle tetiklemek için: **Actions → Saatlik veri toplama → Run workflow**.

**GitHub Pages (bir kerelik ayar):** Settings → Pages → Source: *Deploy from a branch* →
Branch: `main`, klasör: `/docs` → Save.

## Yerelde çalıştırma
```
python collect.py      # veriyi çek ve kaydet
python dashboard.py    # docs/index.html'i üret → tarayıcıda aç
pip install -r requirements.txt && python report.py   # (opsiyonel) PNG grafik
```

## Veritabanı şeması
`player_counts(id, collected_at [UTC ISO], app_id, game_name, player_count)`

## Sonraki adımlar
- [x] Saatlik otomatik toplama (GitHub Actions)
- [x] İnteraktif HTML pano (GitHub Pages)
- [ ] SQL pratiği: "Hangi saatte en çok oyuncu var?" sorgusu
- [ ] Mağaza verisi ekle (fiyat, yorum): `store.steampowered.com/api/appdetails?appids=<ID>`
- [ ] SQLite → PostgreSQL, script → Airflow
