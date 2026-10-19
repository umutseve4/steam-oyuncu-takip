# 🔎 SQL Analizi

_Otomatik üretildi: 19.10.2026 06:00 UTC · sorgular: [`queries.sql`](../queries.sql)_

## 1. Her oyunun en kalabalık olduğu saat (UTC, ortalamaya göre)

| oyun | zirve_saat_utc | zirve_saat_tr | ort_oyuncu | olcum |
|---|---|---|---|---|
| Rainbow Six Siege | 19:00 | 22:00 | 88,045 | 1 |
| Watch Dogs 2 | 14:00 | 17:00 | 7,208 | 3 |
| Titanfall 2 | 14:00 | 17:00 | 2,397 | 3 |
| Watch Dogs | 14:00 | 17:00 | 1,901 | 3 |
| Star Wars Battlefront II | 19:00 | 22:00 | 1,468 | 1 |

## 2. Günlük ortalama ve günlük değişim (%) — LAG window function

| oyun | gun | gunluk_ort | degisim_yuzde |
|---|---|---|---|
| Rainbow Six Siege | 2026-10-19 | 55,668 | -21.8 |
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
| Star Wars Battlefront II | 2026-10-19 | 689 | -36.6 |
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
| Titanfall 2 | 2026-10-19 | 886 | -38.8 |
| Titanfall 2 | 2026-10-18 | 1,447 | -13.4 |
| Titanfall 2 | 2026-10-17 | 1,671 | 47.9 |
| Titanfall 2 | 2026-10-16 | 1,130 | 7.1 |
| Titanfall 2 | 2026-10-15 | 1,055 | -2 |
| Titanfall 2 | 2026-10-14 | 1,076 | -1.2 |
| Titanfall 2 | 2026-10-13 | 1,089 | -4.3 |
| Titanfall 2 | 2026-10-12 | 1,138 | -36.7 |
| Titanfall 2 | 2026-10-11 | 1,798 | 4.8 |
| Titanfall 2 | 2026-10-10 | 1,715 | 8.6 |
| Titanfall 2 | 2026-10-09 | 1,579 | 10.2 |
| Titanfall 2 | 2026-10-08 | 1,433 | -11.5 |
| Titanfall 2 | 2026-10-07 | 1,620 | -9 |
| Titanfall 2 | 2026-10-06 | 1,781 | -16.3 |
| Titanfall 2 | 2026-10-05 | 2,129 | -9.9 |
| Titanfall 2 | 2026-10-03 | 2,363 | 97.2 |

## 3. Her ölçümde oyunların sıralaması (son 5 ölçüm) — DENSE_RANK

| zaman_utc | oyun | oyuncu | sira |
|---|---|---|---|
| 2026-10-19T06:00:34+00:00 | Rainbow Six Siege | 35,319 | 1 |
| 2026-10-19T06:00:34+00:00 | Watch Dogs 2 | 1,674 | 2 |
| 2026-10-19T06:00:34+00:00 | Titanfall 2 | 847 | 3 |
| 2026-10-19T06:00:34+00:00 | Watch Dogs | 554 | 4 |
| 2026-10-19T06:00:34+00:00 | Star Wars Battlefront II | 483 | 5 |
| 2026-10-19T00:58:23+00:00 | Rainbow Six Siege | 76,017 | 1 |
| 2026-10-19T00:58:23+00:00 | Watch Dogs 2 | 1,248 | 2 |
| 2026-10-19T00:58:23+00:00 | Titanfall 2 | 924 | 3 |
| 2026-10-19T00:58:23+00:00 | Star Wars Battlefront II | 895 | 4 |
| 2026-10-19T00:58:23+00:00 | Watch Dogs | 717 | 5 |
| 2026-10-18T22:54:47+00:00 | Rainbow Six Siege | 74,554 | 1 |
| 2026-10-18T22:54:47+00:00 | Watch Dogs 2 | 1,249 | 2 |
| 2026-10-18T22:54:47+00:00 | Titanfall 2 | 959 | 3 |
| 2026-10-18T22:54:47+00:00 | Star Wars Battlefront II | 952 | 4 |
| 2026-10-18T22:54:47+00:00 | Watch Dogs | 832 | 5 |
| 2026-10-18T20:24:55+00:00 | Rainbow Six Siege | 91,821 | 1 |
| 2026-10-18T20:24:55+00:00 | Watch Dogs 2 | 1,944 | 2 |
| 2026-10-18T20:24:55+00:00 | Star Wars Battlefront II | 1,360 | 3 |
| 2026-10-18T20:24:55+00:00 | Titanfall 2 | 1,233 | 4 |
| 2026-10-18T20:24:55+00:00 | Watch Dogs | 1,176 | 5 |
| 2026-10-18T17:55:30+00:00 | Rainbow Six Siege | 84,342 | 1 |
| 2026-10-18T17:55:30+00:00 | Watch Dogs 2 | 2,516 | 2 |
| 2026-10-18T17:55:30+00:00 | Star Wars Battlefront II | 1,584 | 3 |
| 2026-10-18T17:55:30+00:00 | Watch Dogs | 1,399 | 4 |
| 2026-10-18T17:55:30+00:00 | Titanfall 2 | 1,380 | 5 |

## 4. Oynaklık: hangi oyunun oyuncu sayısı en çok dalgalanıyor? (max-min / ortalama)

| oyun | min | max | ort | dalga_yuzde |
|---|---|---|---|---|
| Watch Dogs 2 | 1,248 | 8,619 | 3,419 | 215.6 |
| Titanfall 2 | 823 | 2,760 | 1,452 | 133.4 |
| Star Wars Battlefront II | 398 | 1,623 | 948 | 129.2 |
| Watch Dogs | 554 | 2,131 | 1,243 | 126.9 |
| Rainbow Six Siege | 26,086 | 91,821 | 59,862 | 109.8 |

## 5. Hafta içi vs hafta sonu ortalaması

| oyun | hafta_sonu | hafta_ici |
|---|---|---|
| Rainbow Six Siege | 67,806 | 55,528 |
| Star Wars Battlefront II | 1,110 | 860 |
| Titanfall 2 | 1,694 | 1,320 |
| Watch Dogs | 1,360 | 1,179 |
| Watch Dogs 2 | 3,791 | 3,216 |

## 6. Mağaza verisi: fiyat, indirim, yorum puanı + anlık oyuncu (JOIN)

| oyun | anlik_oyuncu | fiyat | para_birimi | indirim_yuzde | toplam_yorum | olumlu_yuzde | steam_puani |
|---|---|---|---|---|---|---|---|
| Rainbow Six Siege | 35,319 | 0 | FREE | 0 | 1,563,836 | 82.1 | Very Positive |
| Watch Dogs 2 | 1,674 | 39.99 | USD | 0 | 105,371 | 82.1 | Very Positive |
| Titanfall 2 | 847 | 29.99 | USD | 0 | 288,524 | 95.7 | Overwhelmingly Positive |
| Watch Dogs | 554 | 15.99 | USD | 0 | 54,081 | 79.8 | Mostly Positive |
| Star Wars Battlefront II | 483 | 39.99 | USD | 0 | 100,491 | 88.3 | Very Positive |

## 7. İndirim etkisi: indirimli günlerde oyuncu sayısı artıyor mu? (JOIN + koşullu AVG)

| oyun | indirimli_gun | normal_gun | max_indirim_yuzde | ort_indirimli | ort_normal | fark_yuzde |
|---|---|---|---|---|---|---|
| Watch Dogs 2 | 4 | 11 | 95 | 5,047 | 2,874 | 75.6 |
| Watch Dogs | 4 | 11 | 90 | 1,603 | 1,127 | 42.2 |
| Titanfall 2 | 4 | 11 | 85 | 1,741 | 1,326 | 31.3 |
| Star Wars Battlefront II | 4 | 11 | 75 | 913 | 946 | -3.5 |
| Rainbow Six Siege | 0 | 15 | 0 | – | 58,831 | – |

## 8. İndirim × oyuncu sayısı korelasyonu (Pearson r, Python)

| oyun | gun_sayisi | pearson_r | yorum |
|---|---|---|---|
| Rainbow Six Siege | 15 | – | hesaplanamadı (indirim hiç değişmedi) |
| Star Wars Battlefront II | 15 | -0.096 | çok zayıf negatif |
| Titanfall 2 | 15 | +0.530 | orta pozitif |
| Watch Dogs | 15 | +0.597 | orta pozitif |
| Watch Dogs 2 | 15 | +0.706 | güçlü pozitif |

> r ≈ +1: indirim arttıkça oyuncu artıyor · r ≈ 0: ilişki yok · r ≈ −1: ters ilişki. Korelasyon nedensellik değildir; birkaç günlük veriyle sonuç güvenilir olmaz.
