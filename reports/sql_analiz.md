# 🔎 SQL Analizi

_Otomatik üretildi: 23.11.2026 00:41 UTC · sorgular: [`queries.sql`](../queries.sql)_

## 1. Her oyunun en kalabalık olduğu saat (UTC, ortalamaya göre)

| oyun | zirve_saat_utc | zirve_saat_tr | ort_oyuncu | olcum |
|---|---|---|---|---|
| Rainbow Six Siege | 20:00 | 23:00 | 74,665 | 11 |
| Watch Dogs 2 | 15:00 | 18:00 | 5,075 | 5 |
| Titanfall 2 | 15:00 | 18:00 | 1,972 | 5 |
| Watch Dogs | 15:00 | 18:00 | 1,662 | 5 |
| Star Wars Battlefront II | 19:00 | 22:00 | 1,554 | 7 |

## 2. Günlük ortalama ve günlük değişim (%) — LAG window function

| oyun | gun | gunluk_ort | degisim_yuzde |
|---|---|---|---|
| Rainbow Six Siege | 2026-11-23 | 55,826 | 4.7 |
| Rainbow Six Siege | 2026-11-22 | 53,345 | 3.1 |
| Rainbow Six Siege | 2026-11-21 | 51,758 | 15.9 |
| Rainbow Six Siege | 2026-11-20 | 44,647 | -2.6 |
| Rainbow Six Siege | 2026-11-19 | 45,828 | -7.9 |
| Rainbow Six Siege | 2026-11-18 | 49,750 | -2.7 |
| Rainbow Six Siege | 2026-11-17 | 51,141 | -0.8 |
| Rainbow Six Siege | 2026-11-16 | 51,545 | -17 |
| Rainbow Six Siege | 2026-11-15 | 62,105 | 5.1 |
| Rainbow Six Siege | 2026-11-14 | 59,102 | 18.9 |
| Rainbow Six Siege | 2026-11-13 | 49,726 | 9 |
| Rainbow Six Siege | 2026-11-12 | 45,640 | -10.6 |
| Rainbow Six Siege | 2026-11-11 | 51,068 | 7.6 |
| Rainbow Six Siege | 2026-11-10 | 47,464 | -1.9 |
| Rainbow Six Siege | 2026-11-09 | 48,402 | -20.8 |
| Rainbow Six Siege | 2026-11-08 | 61,110 | -1.7 |
| Rainbow Six Siege | 2026-11-07 | 62,177 | 25.1 |
| Rainbow Six Siege | 2026-11-06 | 49,713 | 1.4 |
| Rainbow Six Siege | 2026-11-05 | 49,050 | 4 |
| Rainbow Six Siege | 2026-11-04 | 47,149 | -9 |
| Rainbow Six Siege | 2026-11-03 | 51,827 | -5.6 |
| Rainbow Six Siege | 2026-11-02 | 54,905 | -12.9 |
| Rainbow Six Siege | 2026-11-01 | 63,002 | 2.9 |
| Rainbow Six Siege | 2026-10-31 | 61,236 | 13.8 |
| Rainbow Six Siege | 2026-10-30 | 53,818 | 3.7 |
| Rainbow Six Siege | 2026-10-29 | 51,878 | 5.1 |
| Rainbow Six Siege | 2026-10-28 | 49,379 | -11.8 |
| Rainbow Six Siege | 2026-10-27 | 55,996 | 13.6 |
| Rainbow Six Siege | 2026-10-26 | 49,313 | -29.3 |
| Rainbow Six Siege | 2026-10-25 | 69,753 | 4.5 |
| Rainbow Six Siege | 2026-10-24 | 66,776 | 18.2 |
| Rainbow Six Siege | 2026-10-23 | 56,497 | 9 |
| Rainbow Six Siege | 2026-10-22 | 51,832 | 0.8 |
| Rainbow Six Siege | 2026-10-21 | 51,423 | -1.5 |
| Rainbow Six Siege | 2026-10-20 | 52,203 | -9.7 |
| Rainbow Six Siege | 2026-10-19 | 57,819 | -18.8 |
| Rainbow Six Siege | 2026-10-18 | 71,219 | 2.3 |
| Rainbow Six Siege | 2026-10-17 | 69,613 | 15 |
| Rainbow Six Siege | 2026-10-16 | 60,516 | 11.3 |
| Rainbow Six Siege | 2026-10-15 | 54,362 | 3.6 |
| Rainbow Six Siege | 2026-10-14 | 52,483 | -1.4 |
| Rainbow Six Siege | 2026-10-13 | 53,235 | -10.1 |
| Rainbow Six Siege | 2026-10-12 | 59,244 | -13.6 |
| Rainbow Six Siege | 2026-10-11 | 68,604 | 4.3 |
| Rainbow Six Siege | 2026-10-10 | 65,751 | 13.6 |
| Rainbow Six Siege | 2026-10-09 | 57,891 | 10.8 |
| Rainbow Six Siege | 2026-10-08 | 52,254 | -0.1 |
| Rainbow Six Siege | 2026-10-07 | 52,319 | -1.9 |
| Rainbow Six Siege | 2026-10-06 | 53,345 | -4.7 |
| Rainbow Six Siege | 2026-10-05 | 55,958 | 3.7 |

## 3. Her ölçümde oyunların sıralaması (son 5 ölçüm) — DENSE_RANK

| zaman_utc | oyun | oyuncu | sira |
|---|---|---|---|
| 2026-11-23T00:39:45+00:00 | Rainbow Six Siege | 55,826 | 1 |
| 2026-11-23T00:39:45+00:00 | Watch Dogs 2 | 1,695 | 2 |
| 2026-11-23T00:39:45+00:00 | Star Wars Battlefront II | 1,381 | 3 |
| 2026-11-23T00:39:45+00:00 | Titanfall 2 | 1,350 | 4 |
| 2026-11-23T00:39:45+00:00 | Watch Dogs | 754 | 5 |
| 2026-11-22T19:15:42+00:00 | Rainbow Six Siege | 67,847 | 1 |
| 2026-11-22T19:15:42+00:00 | Watch Dogs 2 | 3,144 | 2 |
| 2026-11-22T19:15:42+00:00 | Star Wars Battlefront II | 1,991 | 3 |
| 2026-11-22T19:15:42+00:00 | Titanfall 2 | 1,751 | 4 |
| 2026-11-22T19:15:42+00:00 | Watch Dogs | 1,215 | 5 |
| 2026-11-22T11:01:21+00:00 | Rainbow Six Siege | 34,195 | 1 |
| 2026-11-22T11:01:21+00:00 | Watch Dogs 2 | 4,069 | 2 |
| 2026-11-22T11:01:21+00:00 | Titanfall 2 | 2,376 | 3 |
| 2026-11-22T11:01:21+00:00 | Star Wars Battlefront II | 1,106 | 4 |
| 2026-11-22T11:01:21+00:00 | Watch Dogs | 1,039 | 5 |
| 2026-11-22T02:56:42+00:00 | Rainbow Six Siege | 57,994 | 1 |
| 2026-11-22T02:56:42+00:00 | Watch Dogs 2 | 2,451 | 2 |
| 2026-11-22T02:56:42+00:00 | Titanfall 2 | 2,155 | 3 |
| 2026-11-22T02:56:42+00:00 | Star Wars Battlefront II | 1,352 | 4 |
| 2026-11-22T02:56:42+00:00 | Watch Dogs | 846 | 5 |
| 2026-11-21T22:55:59+00:00 | Rainbow Six Siege | 64,436 | 1 |
| 2026-11-21T22:55:59+00:00 | Watch Dogs 2 | 2,300 | 2 |
| 2026-11-21T22:55:59+00:00 | Star Wars Battlefront II | 1,697 | 3 |
| 2026-11-21T22:55:59+00:00 | Titanfall 2 | 1,537 | 4 |
| 2026-11-21T22:55:59+00:00 | Watch Dogs | 919 | 5 |

## 4. Oynaklık: hangi oyunun oyuncu sayısı en çok dalgalanıyor? (max-min / ortalama)

| oyun | min | max | ort | dalga_yuzde |
|---|---|---|---|---|
| Watch Dogs 2 | 685 | 8,619 | 2,268 | 349.8 |
| Watch Dogs | 315 | 2,131 | 835 | 217.4 |
| Titanfall 2 | 628 | 2,760 | 1,211 | 176 |
| Star Wars Battlefront II | 398 | 2,156 | 1,036 | 169.8 |
| Rainbow Six Siege | 23,921 | 91,821 | 56,341 | 120.5 |

## 5. Hafta içi vs hafta sonu ortalaması

| oyun | hafta_sonu | hafta_ici |
|---|---|---|
| Rainbow Six Siege | 63,981 | 52,465 |
| Star Wars Battlefront II | 1,254 | 925 |
| Titanfall 2 | 1,499 | 1,065 |
| Watch Dogs | 972 | 766 |
| Watch Dogs 2 | 2,686 | 2,056 |

## 6. Mağaza verisi: fiyat, indirim, yorum puanı + anlık oyuncu (JOIN)

| oyun | anlik_oyuncu | fiyat | para_birimi | indirim_yuzde | toplam_yorum | olumlu_yuzde | steam_puani |
|---|---|---|---|---|---|---|---|
| Rainbow Six Siege | 55,826 | 0 | FREE | 0 | – | – | – |
| Watch Dogs 2 | 1,695 | 5.99 | USD | 85 | – | – | – |
| Star Wars Battlefront II | 1,381 | 7.99 | USD | 80 | – | – | – |
| Titanfall 2 | 1,350 | 4.49 | USD | 85 | – | – | – |
| Watch Dogs | 754 | 3.99 | USD | 75 | – | – | – |

## 7. İndirim etkisi: indirimli günlerde oyuncu sayısı artıyor mu? (JOIN + koşullu AVG)

| oyun | indirimli_gun | normal_gun | max_indirim_yuzde | ort_indirimli | ort_normal | fark_yuzde |
|---|---|---|---|---|---|---|
| Watch Dogs 2 | 9 | 41 | 95 | 3,576 | 1,904 | 87.8 |
| Watch Dogs | 9 | 41 | 90 | 1,156 | 735 | 57.3 |
| Titanfall 2 | 8 | 42 | 85 | 1,703 | 1,096 | 55.4 |
| Star Wars Battlefront II | 8 | 42 | 80 | 1,104 | 1,016 | 8.6 |
| Rainbow Six Siege | 0 | 50 | 0 | – | 55,220 | – |

## 8. İndirim × oyuncu sayısı korelasyonu (Pearson r, Python)

| oyun | gun_sayisi | pearson_r | yorum |
|---|---|---|---|
| Rainbow Six Siege | 50 | – | hesaplanamadı (indirim hiç değişmedi) |
| Star Wars Battlefront II | 50 | +0.181 | çok zayıf pozitif |
| Titanfall 2 | 50 | +0.632 | güçlü pozitif |
| Watch Dogs | 50 | +0.478 | orta pozitif |
| Watch Dogs 2 | 50 | +0.567 | orta pozitif |

> r ≈ +1: indirim arttıkça oyuncu artıyor · r ≈ 0: ilişki yok · r ≈ −1: ters ilişki. Korelasyon nedensellik değildir; birkaç günlük veriyle sonuç güvenilir olmaz.
