# 🔎 SQL Analizi

_Otomatik üretildi: 21.10.2026 04:04 UTC · sorgular: [`queries.sql`](../queries.sql)_

## 1. Her oyunun en kalabalık olduğu saat (UTC, ortalamaya göre)

| oyun | zirve_saat_utc | zirve_saat_tr | ort_oyuncu | olcum |
|---|---|---|---|---|
| Rainbow Six Siege | 19:00 | 22:00 | 88,045 | 1 |
| Watch Dogs 2 | 14:00 | 17:00 | 6,398 | 4 |
| Titanfall 2 | 14:00 | 17:00 | 2,217 | 4 |
| Watch Dogs | 15:00 | 18:00 | 1,836 | 4 |
| Star Wars Battlefront II | 19:00 | 22:00 | 1,468 | 1 |

## 2. Günlük ortalama ve günlük değişim (%) — LAG window function

| oyun | gun | gunluk_ort | degisim_yuzde |
|---|---|---|---|
| Rainbow Six Siege | 2026-10-21 | 50,259 | -3.7 |
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
| Star Wars Battlefront II | 2026-10-21 | 709 | -9.6 |
| Star Wars Battlefront II | 2026-10-20 | 784 | -0.4 |
| Star Wars Battlefront II | 2026-10-19 | 787 | -27.6 |
| Star Wars Battlefront II | 2026-10-18 | 1,087 | -0.9 |
| Star Wars Battlefront II | 2026-10-17 | 1,097 | 30 |
| Star Wars Battlefront II | 2026-10-16 | 844 | 8.8 |
| Star Wars Battlefront II | 2026-10-15 | 776 | -4.4 |
| Star Wars Battlefront II | 2026-10-14 | 812 | 1.8 |
| Star Wars Battlefront II | 2026-10-13 | 798 | -17 |
| Star Wars Battlefront II | 2026-10-12 | 961 | -20.9 |
| Star Wars Battlefront II | 2026-10-11 | 1,215 | 5.6 |
| Star Wars Battlefront II | 2026-10-10 | 1,151 | 17.7 |
| Star Wars Battlefront II | 2026-10-09 | 978 | 13.9 |
| Star Wars Battlefront II | 2026-10-08 | 859 | -3.6 |
| Star Wars Battlefront II | 2026-10-07 | 891 | 7.2 |
| Star Wars Battlefront II | 2026-10-06 | 831 | -22.5 |
| Star Wars Battlefront II | 2026-10-05 | 1,072 | 16 |
| Star Wars Battlefront II | 2026-10-03 | 924 | -6.7 |
| Star Wars Battlefront II | 2026-10-02 | 990 | – |
| Titanfall 2 | 2026-10-21 | 854 | -4.2 |
| Titanfall 2 | 2026-10-20 | 891 | -18.6 |
| Titanfall 2 | 2026-10-19 | 1,094 | -24.4 |
| Titanfall 2 | 2026-10-18 | 1,447 | -13.4 |
| Titanfall 2 | 2026-10-17 | 1,671 | 47.9 |
| Titanfall 2 | 2026-10-16 | 1,130 | 7.1 |
| Titanfall 2 | 2026-10-15 | 1,055 | -2 |
| Titanfall 2 | 2026-10-14 | 1,076 | -1.2 |
| Titanfall 2 | 2026-10-13 | 1,089 | -4.3 |
| Titanfall 2 | 2026-10-12 | 1,138 | -36.7 |
| Titanfall 2 | 2026-10-11 | 1,798 | 4.8 |
| Titanfall 2 | 2026-10-10 | 1,715 | 8.6 |

## 3. Her ölçümde oyunların sıralaması (son 5 ölçüm) — DENSE_RANK

| zaman_utc | oyun | oyuncu | sira |
|---|---|---|---|
| 2026-10-21T04:04:21+00:00 | Rainbow Six Siege | 50,259 | 1 |
| 2026-10-21T04:04:21+00:00 | Watch Dogs 2 | 1,327 | 2 |
| 2026-10-21T04:04:21+00:00 | Titanfall 2 | 854 | 3 |
| 2026-10-21T04:04:21+00:00 | Star Wars Battlefront II | 709 | 4 |
| 2026-10-21T04:04:21+00:00 | Watch Dogs | 523 | 5 |
| 2026-10-20T23:41:57+00:00 | Rainbow Six Siege | 61,959 | 1 |
| 2026-10-20T23:41:57+00:00 | Watch Dogs 2 | 936 | 2 |
| 2026-10-20T23:41:57+00:00 | Star Wars Battlefront II | 859 | 3 |
| 2026-10-20T23:41:57+00:00 | Titanfall 2 | 716 | 4 |
| 2026-10-20T23:41:57+00:00 | Watch Dogs | 578 | 5 |
| 2026-10-20T20:20:34+00:00 | Rainbow Six Siege | 63,943 | 1 |
| 2026-10-20T20:20:34+00:00 | Watch Dogs 2 | 1,364 | 2 |
| 2026-10-20T20:20:34+00:00 | Star Wars Battlefront II | 1,018 | 3 |
| 2026-10-20T20:20:34+00:00 | Titanfall 2 | 857 | 4 |
| 2026-10-20T20:20:34+00:00 | Watch Dogs | 789 | 5 |
| 2026-10-20T16:37:12+00:00 | Rainbow Six Siege | 53,279 | 1 |
| 2026-10-20T16:37:12+00:00 | Watch Dogs 2 | 2,194 | 2 |
| 2026-10-20T16:37:12+00:00 | Titanfall 2 | 1,050 | 3 |
| 2026-10-20T16:37:12+00:00 | Star Wars Battlefront II | 970 | 4 |
| 2026-10-20T16:37:12+00:00 | Watch Dogs | 923 | 5 |
| 2026-10-20T11:12:49+00:00 | Rainbow Six Siege | 29,677 | 1 |
| 2026-10-20T11:12:49+00:00 | Watch Dogs 2 | 2,407 | 2 |
| 2026-10-20T11:12:49+00:00 | Titanfall 2 | 1,053 | 3 |
| 2026-10-20T11:12:49+00:00 | Watch Dogs | 681 | 4 |
| 2026-10-20T11:12:49+00:00 | Star Wars Battlefront II | 507 | 5 |

## 4. Oynaklık: hangi oyunun oyuncu sayısı en çok dalgalanıyor? (max-min / ortalama)

| oyun | min | max | ort | dalga_yuzde |
|---|---|---|---|---|
| Watch Dogs 2 | 936 | 8,619 | 3,234 | 237.6 |
| Titanfall 2 | 716 | 2,760 | 1,397 | 146.4 |
| Watch Dogs | 523 | 2,131 | 1,183 | 135.9 |
| Star Wars Battlefront II | 398 | 1,623 | 931 | 131.6 |
| Rainbow Six Siege | 26,086 | 91,821 | 59,143 | 111.1 |

## 5. Hafta içi vs hafta sonu ortalaması

| oyun | hafta_sonu | hafta_ici |
|---|---|---|
| Rainbow Six Siege | 67,806 | 55,220 |
| Star Wars Battlefront II | 1,110 | 849 |
| Titanfall 2 | 1,694 | 1,262 |
| Watch Dogs | 1,360 | 1,103 |
| Watch Dogs 2 | 3,791 | 2,981 |

## 6. Mağaza verisi: fiyat, indirim, yorum puanı + anlık oyuncu (JOIN)

| oyun | anlik_oyuncu | fiyat | para_birimi | indirim_yuzde | toplam_yorum | olumlu_yuzde | steam_puani |
|---|---|---|---|---|---|---|---|
| Rainbow Six Siege | 50,259 | 0 | FREE | 0 | 1,564,327 | 82.1 | Very Positive |
| Watch Dogs 2 | 1,327 | 39.99 | USD | 0 | 105,439 | 82.1 | Very Positive |
| Titanfall 2 | 854 | 29.99 | USD | 0 | 288,600 | 95.7 | Overwhelmingly Positive |
| Star Wars Battlefront II | 709 | 39.99 | USD | 0 | 100,514 | 88.3 | Very Positive |
| Watch Dogs | 523 | 15.99 | USD | 0 | 54,109 | 79.8 | Mostly Positive |

## 7. İndirim etkisi: indirimli günlerde oyuncu sayısı artıyor mu? (JOIN + koşullu AVG)

| oyun | indirimli_gun | normal_gun | max_indirim_yuzde | ort_indirimli | ort_normal | fark_yuzde |
|---|---|---|---|---|---|---|
| Watch Dogs 2 | 4 | 13 | 95 | 5,047 | 2,707 | 86.5 |
| Watch Dogs | 4 | 13 | 90 | 1,603 | 1,059 | 51.3 |
| Titanfall 2 | 4 | 13 | 85 | 1,741 | 1,272 | 36.8 |
| Star Wars Battlefront II | 4 | 13 | 75 | 913 | 923 | -1 |
| Rainbow Six Siege | 0 | 17 | 0 | – | 58,063 | – |

## 8. İndirim × oyuncu sayısı korelasyonu (Pearson r, Python)

| oyun | gun_sayisi | pearson_r | yorum |
|---|---|---|---|
| Rainbow Six Siege | 17 | – | hesaplanamadı (indirim hiç değişmedi) |
| Star Wars Battlefront II | 17 | -0.028 | çok zayıf negatif |
| Titanfall 2 | 17 | +0.553 | orta pozitif |
| Watch Dogs | 17 | +0.605 | güçlü pozitif |
| Watch Dogs 2 | 17 | +0.713 | güçlü pozitif |

> r ≈ +1: indirim arttıkça oyuncu artıyor · r ≈ 0: ilişki yok · r ≈ −1: ters ilişki. Korelasyon nedensellik değildir; birkaç günlük veriyle sonuç güvenilir olmaz.
