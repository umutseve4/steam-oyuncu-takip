# 🔎 SQL Analizi

_Otomatik üretildi: 26.11.2026 04:49 UTC · sorgular: [`queries.sql`](../queries.sql)_

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
| Rainbow Six Siege | 2026-11-26 | 52,112 | 10.9 |
| Rainbow Six Siege | 2026-11-25 | 47,010 | 14.6 |
| Rainbow Six Siege | 2026-11-24 | 41,036 | -11.6 |
| Rainbow Six Siege | 2026-11-23 | 46,443 | -12.9 |
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

## 3. Her ölçümde oyunların sıralaması (son 5 ölçüm) — DENSE_RANK

| zaman_utc | oyun | oyuncu | sira |
|---|---|---|---|
| 2026-11-26T04:48:09+00:00 | Rainbow Six Siege | 52,112 | 1 |
| 2026-11-26T04:48:09+00:00 | Watch Dogs 2 | 2,065 | 2 |
| 2026-11-26T04:48:09+00:00 | Titanfall 2 | 1,772 | 3 |
| 2026-11-26T04:48:09+00:00 | Star Wars Battlefront II | 1,099 | 4 |
| 2026-11-26T04:48:09+00:00 | Watch Dogs | 614 | 5 |
| 2026-11-25T22:15:35+00:00 | Rainbow Six Siege | 57,280 | 1 |
| 2026-11-25T22:15:35+00:00 | Watch Dogs 2 | 1,604 | 2 |
| 2026-11-25T22:15:35+00:00 | Star Wars Battlefront II | 1,406 | 3 |
| 2026-11-25T22:15:35+00:00 | Titanfall 2 | 1,197 | 4 |
| 2026-11-25T22:15:35+00:00 | Watch Dogs | 765 | 5 |
| 2026-11-25T12:23:19+00:00 | Rainbow Six Siege | 28,672 | 1 |
| 2026-11-25T12:23:19+00:00 | Watch Dogs 2 | 3,005 | 2 |
| 2026-11-25T12:23:19+00:00 | Titanfall 2 | 2,048 | 3 |
| 2026-11-25T12:23:19+00:00 | Watch Dogs | 726 | 4 |
| 2026-11-25T12:23:19+00:00 | Star Wars Battlefront II | 718 | 5 |
| 2026-11-25T02:05:16+00:00 | Rainbow Six Siege | 55,077 | 1 |
| 2026-11-25T02:05:16+00:00 | Watch Dogs 2 | 1,399 | 2 |
| 2026-11-25T02:05:16+00:00 | Titanfall 2 | 1,225 | 3 |
| 2026-11-25T02:05:16+00:00 | Star Wars Battlefront II | 1,164 | 4 |
| 2026-11-25T02:05:16+00:00 | Watch Dogs | 681 | 5 |
| 2026-11-24T17:17:46+00:00 | Rainbow Six Siege | 43,368 | 1 |
| 2026-11-24T17:17:46+00:00 | Watch Dogs 2 | 2,573 | 2 |
| 2026-11-24T17:17:46+00:00 | Titanfall 2 | 1,458 | 3 |
| 2026-11-24T17:17:46+00:00 | Star Wars Battlefront II | 1,277 | 4 |
| 2026-11-24T17:17:46+00:00 | Watch Dogs | 0 | 5 |

## 4. Oynaklık: hangi oyunun oyuncu sayısı en çok dalgalanıyor? (max-min / ortalama)

| oyun | min | max | ort | dalga_yuzde |
|---|---|---|---|---|
| Watch Dogs 2 | 685 | 8,619 | 2,263 | 350.6 |
| Watch Dogs | 0 | 2,131 | 827 | 257.8 |
| Titanfall 2 | 628 | 2,760 | 1,223 | 174.4 |
| Star Wars Battlefront II | 398 | 2,156 | 1,036 | 169.7 |
| Rainbow Six Siege | 23,921 | 91,821 | 55,915 | 121.4 |

## 5. Hafta içi vs hafta sonu ortalaması

| oyun | hafta_sonu | hafta_ici |
|---|---|---|
| Rainbow Six Siege | 63,981 | 52,047 |
| Star Wars Battlefront II | 1,254 | 931 |
| Titanfall 2 | 1,499 | 1,091 |
| Watch Dogs | 972 | 757 |
| Watch Dogs 2 | 2,686 | 2,060 |

## 6. Mağaza verisi: fiyat, indirim, yorum puanı + anlık oyuncu (JOIN)

| oyun | anlik_oyuncu | fiyat | para_birimi | indirim_yuzde | toplam_yorum | olumlu_yuzde | steam_puani |
|---|---|---|---|---|---|---|---|
| Rainbow Six Siege | 52,112 | 0 | FREE | 0 | – | – | – |
| Watch Dogs 2 | 2,065 | 5.99 | USD | 85 | – | – | – |
| Titanfall 2 | 1,772 | 4.49 | USD | 85 | – | – | – |
| Star Wars Battlefront II | 1,099 | 7.99 | USD | 80 | – | – | – |
| Watch Dogs | 614 | 3.99 | USD | 75 | – | – | – |

## 7. İndirim etkisi: indirimli günlerde oyuncu sayısı artıyor mu? (JOIN + koşullu AVG)

| oyun | indirimli_gun | normal_gun | max_indirim_yuzde | ort_indirimli | ort_normal | fark_yuzde |
|---|---|---|---|---|---|---|
| Watch Dogs 2 | 12 | 41 | 95 | 3,238 | 1,904 | 70.1 |
| Titanfall 2 | 11 | 42 | 85 | 1,682 | 1,096 | 53.4 |
| Watch Dogs | 12 | 41 | 90 | 1,002 | 735 | 36.3 |
| Star Wars Battlefront II | 11 | 42 | 80 | 1,071 | 1,016 | 5.4 |
| Rainbow Six Siege | 0 | 53 | 0 | – | 54,562 | – |

## 8. İndirim × oyuncu sayısı korelasyonu (Pearson r, Python)

| oyun | gun_sayisi | pearson_r | yorum |
|---|---|---|---|
| Rainbow Six Siege | 53 | – | hesaplanamadı (indirim hiç değişmedi) |
| Star Wars Battlefront II | 53 | +0.131 | çok zayıf pozitif |
| Titanfall 2 | 53 | +0.666 | güçlü pozitif |
| Watch Dogs | 53 | +0.356 | zayıf pozitif |
| Watch Dogs 2 | 53 | +0.514 | orta pozitif |

> r ≈ +1: indirim arttıkça oyuncu artıyor · r ≈ 0: ilişki yok · r ≈ −1: ters ilişki. Korelasyon nedensellik değildir; birkaç günlük veriyle sonuç güvenilir olmaz.
