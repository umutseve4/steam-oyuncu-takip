# 🔎 SQL Analizi

_Otomatik üretildi: 17.11.2026 03:35 UTC · sorgular: [`queries.sql`](../queries.sql)_

## 1. Her oyunun en kalabalık olduğu saat (UTC, ortalamaya göre)

| oyun | zirve_saat_utc | zirve_saat_tr | ort_oyuncu | olcum |
|---|---|---|---|---|
| Rainbow Six Siege | 20:00 | 23:00 | 74,665 | 11 |
| Watch Dogs 2 | 15:00 | 18:00 | 5,075 | 5 |
| Titanfall 2 | 15:00 | 18:00 | 1,972 | 5 |
| Watch Dogs | 15:00 | 18:00 | 1,662 | 5 |
| Star Wars Battlefront II | 19:00 | 22:00 | 1,481 | 5 |

## 2. Günlük ortalama ve günlük değişim (%) — LAG window function

| oyun | gun | gunluk_ort | degisim_yuzde |
|---|---|---|---|
| Rainbow Six Siege | 2026-11-17 | 58,923 | 14.3 |
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
| Rainbow Six Siege | 2026-10-03 | 53,977 | -21.5 |
| Rainbow Six Siege | 2026-10-02 | 68,763 | – |
| Star Wars Battlefront II | 2026-11-17 | 831 | -8.6 |
| Star Wars Battlefront II | 2026-11-16 | 909 | -19.6 |
| Star Wars Battlefront II | 2026-11-15 | 1,130 | -3.5 |
| Star Wars Battlefront II | 2026-11-14 | 1,171 | 24 |

## 3. Her ölçümde oyunların sıralaması (son 5 ölçüm) — DENSE_RANK

| zaman_utc | oyun | oyuncu | sira |
|---|---|---|---|
| 2026-11-17T03:33:31+00:00 | Rainbow Six Siege | 58,923 | 1 |
| 2026-11-17T03:33:31+00:00 | Star Wars Battlefront II | 831 | 2 |
| 2026-11-17T03:33:31+00:00 | Titanfall 2 | 800 | 3 |
| 2026-11-17T03:33:31+00:00 | Watch Dogs 2 | 755 | 4 |
| 2026-11-17T03:33:31+00:00 | Watch Dogs | 388 | 5 |
| 2026-11-16T20:08:46+00:00 | Rainbow Six Siege | 60,374 | 1 |
| 2026-11-16T20:08:46+00:00 | Star Wars Battlefront II | 1,176 | 2 |
| 2026-11-16T20:08:46+00:00 | Watch Dogs 2 | 996 | 3 |
| 2026-11-16T20:08:46+00:00 | Titanfall 2 | 751 | 4 |
| 2026-11-16T20:08:46+00:00 | Watch Dogs | 526 | 5 |
| 2026-11-16T09:16:55+00:00 | Rainbow Six Siege | 25,692 | 1 |
| 2026-11-16T09:16:55+00:00 | Watch Dogs 2 | 1,235 | 2 |
| 2026-11-16T09:16:55+00:00 | Titanfall 2 | 689 | 3 |
| 2026-11-16T09:16:55+00:00 | Star Wars Battlefront II | 430 | 4 |
| 2026-11-16T09:16:55+00:00 | Watch Dogs | 378 | 5 |
| 2026-11-16T01:41:14+00:00 | Rainbow Six Siege | 68,569 | 1 |
| 2026-11-16T01:41:14+00:00 | Star Wars Battlefront II | 1,122 | 2 |
| 2026-11-16T01:41:14+00:00 | Watch Dogs 2 | 800 | 3 |
| 2026-11-16T01:41:14+00:00 | Titanfall 2 | 788 | 4 |
| 2026-11-16T01:41:14+00:00 | Watch Dogs | 418 | 5 |
| 2026-11-15T21:33:48+00:00 | Rainbow Six Siege | 79,573 | 1 |
| 2026-11-15T21:33:48+00:00 | Star Wars Battlefront II | 1,481 | 2 |
| 2026-11-15T21:33:48+00:00 | Watch Dogs 2 | 1,051 | 3 |
| 2026-11-15T21:33:48+00:00 | Titanfall 2 | 995 | 4 |
| 2026-11-15T21:33:48+00:00 | Watch Dogs | 594 | 5 |

## 4. Oynaklık: hangi oyunun oyuncu sayısı en çok dalgalanıyor? (max-min / ortalama)

| oyun | min | max | ort | dalga_yuzde |
|---|---|---|---|---|
| Watch Dogs 2 | 685 | 8,619 | 2,273 | 349 |
| Watch Dogs | 315 | 2,131 | 847 | 214.5 |
| Titanfall 2 | 628 | 2,760 | 1,194 | 178.6 |
| Star Wars Battlefront II | 398 | 2,156 | 1,029 | 170.8 |
| Rainbow Six Siege | 23,921 | 91,821 | 57,041 | 119 |

## 5. Hafta içi vs hafta sonu ortalaması

| oyun | hafta_sonu | hafta_ici |
|---|---|---|
| Rainbow Six Siege | 65,264 | 52,930 |
| Star Wars Battlefront II | 1,238 | 925 |
| Titanfall 2 | 1,444 | 1,069 |
| Watch Dogs | 973 | 784 |
| Watch Dogs 2 | 2,643 | 2,089 |

## 6. Mağaza verisi: fiyat, indirim, yorum puanı + anlık oyuncu (JOIN)

| oyun | anlik_oyuncu | fiyat | para_birimi | indirim_yuzde | toplam_yorum | olumlu_yuzde | steam_puani |
|---|---|---|---|---|---|---|---|
| Rainbow Six Siege | 58,923 | 0 | FREE | 0 | – | – | – |
| Star Wars Battlefront II | 831 | 39.99 | USD | 0 | – | – | – |
| Titanfall 2 | 800 | 29.99 | USD | 0 | – | – | – |
| Watch Dogs 2 | 755 | 39.99 | USD | 0 | – | – | – |
| Watch Dogs | 388 | 15.99 | USD | 0 | – | – | – |

## 7. İndirim etkisi: indirimli günlerde oyuncu sayısı artıyor mu? (JOIN + koşullu AVG)

| oyun | indirimli_gun | normal_gun | max_indirim_yuzde | ort_indirimli | ort_normal | fark_yuzde |
|---|---|---|---|---|---|---|
| Watch Dogs 2 | 4 | 40 | 95 | 5,047 | 1,909 | 164.4 |
| Watch Dogs | 4 | 40 | 90 | 1,603 | 740 | 116.5 |
| Titanfall 2 | 4 | 40 | 85 | 1,741 | 1,106 | 57.4 |
| Star Wars Battlefront II | 4 | 40 | 75 | 913 | 1,025 | -10.9 |
| Rainbow Six Siege | 0 | 44 | 0 | – | 56,082 | – |

## 8. İndirim × oyuncu sayısı korelasyonu (Pearson r, Python)

| oyun | gun_sayisi | pearson_r | yorum |
|---|---|---|---|
| Rainbow Six Siege | 44 | – | hesaplanamadı (indirim hiç değişmedi) |
| Star Wars Battlefront II | 44 | -0.183 | çok zayıf negatif |
| Titanfall 2 | 44 | +0.562 | orta pozitif |
| Watch Dogs | 44 | +0.634 | güçlü pozitif |
| Watch Dogs 2 | 44 | +0.720 | güçlü pozitif |

> r ≈ +1: indirim arttıkça oyuncu artıyor · r ≈ 0: ilişki yok · r ≈ −1: ters ilişki. Korelasyon nedensellik değildir; birkaç günlük veriyle sonuç güvenilir olmaz.
