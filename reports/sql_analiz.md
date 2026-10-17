# 🔎 SQL Analizi

_Otomatik üretildi: 17.10.2026 22:04 UTC · sorgular: [`queries.sql`](../queries.sql)_

## 1. Her oyunun en kalabalık olduğu saat (UTC, ortalamaya göre)

| oyun | zirve_saat_utc | zirve_saat_tr | ort_oyuncu | olcum |
|---|---|---|---|---|
| Rainbow Six Siege | 19:00 | 22:00 | 88,045 | 1 |
| Watch Dogs 2 | 14:00 | 17:00 | 8,384 | 2 |
| Titanfall 2 | 14:00 | 17:00 | 2,552 | 2 |
| Watch Dogs | 14:00 | 17:00 | 2,072 | 2 |
| Star Wars Battlefront II | 19:00 | 22:00 | 1,468 | 1 |

## 2. Günlük ortalama ve günlük değişim (%) — LAG window function

| oyun | gun | gunluk_ort | degisim_yuzde |
|---|---|---|---|
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
| Titanfall 2 | 2026-10-02 | 1,198 | – |
| Watch Dogs | 2026-10-17 | 1,166 | 32 |
| Watch Dogs | 2026-10-16 | 883 | -0.3 |
| Watch Dogs | 2026-10-15 | 886 | -6.8 |
| Watch Dogs | 2026-10-14 | 951 | -4.5 |
| Watch Dogs | 2026-10-13 | 996 | -14.1 |

## 3. Her ölçümde oyunların sıralaması (son 5 ölçüm) — DENSE_RANK

| zaman_utc | oyun | oyuncu | sira |
|---|---|---|---|
| 2026-10-17T22:04:43+00:00 | Rainbow Six Siege | 83,796 | 1 |
| 2026-10-17T22:04:43+00:00 | Watch Dogs 2 | 1,760 | 2 |
| 2026-10-17T22:04:43+00:00 | Star Wars Battlefront II | 1,265 | 3 |
| 2026-10-17T22:04:43+00:00 | Titanfall 2 | 1,165 | 4 |
| 2026-10-17T22:04:43+00:00 | Watch Dogs | 1,063 | 5 |
| 2026-10-17T19:07:48+00:00 | Rainbow Six Siege | 88,045 | 1 |
| 2026-10-17T19:07:48+00:00 | Watch Dogs 2 | 2,629 | 2 |
| 2026-10-17T19:07:48+00:00 | Star Wars Battlefront II | 1,468 | 3 |
| 2026-10-17T19:07:48+00:00 | Titanfall 2 | 1,464 | 4 |
| 2026-10-17T19:07:48+00:00 | Watch Dogs | 1,253 | 5 |
| 2026-10-17T16:14:05+00:00 | Rainbow Six Siege | 73,372 | 1 |
| 2026-10-17T16:14:05+00:00 | Watch Dogs 2 | 3,981 | 2 |
| 2026-10-17T16:14:05+00:00 | Titanfall 2 | 1,901 | 3 |
| 2026-10-17T16:14:05+00:00 | Watch Dogs | 1,490 | 4 |
| 2026-10-17T16:14:05+00:00 | Star Wars Battlefront II | 1,303 | 5 |
| 2026-10-17T12:49:15+00:00 | Rainbow Six Siege | 56,345 | 1 |
| 2026-10-17T12:49:15+00:00 | Watch Dogs 2 | 5,101 | 2 |
| 2026-10-17T12:49:15+00:00 | Titanfall 2 | 2,276 | 3 |
| 2026-10-17T12:49:15+00:00 | Watch Dogs | 1,376 | 4 |
| 2026-10-17T12:49:15+00:00 | Star Wars Battlefront II | 978 | 5 |
| 2026-10-17T08:25:03+00:00 | Rainbow Six Siege | 41,509 | 1 |
| 2026-10-17T08:25:03+00:00 | Watch Dogs 2 | 4,087 | 2 |
| 2026-10-17T08:25:03+00:00 | Titanfall 2 | 1,674 | 3 |
| 2026-10-17T08:25:03+00:00 | Watch Dogs | 971 | 4 |
| 2026-10-17T08:25:03+00:00 | Star Wars Battlefront II | 631 | 5 |

## 4. Oynaklık: hangi oyunun oyuncu sayısı en çok dalgalanıyor? (max-min / ortalama)

| oyun | min | max | ort | dalga_yuzde |
|---|---|---|---|---|
| Watch Dogs 2 | 1,298 | 8,619 | 3,564 | 205.4 |
| Titanfall 2 | 823 | 2,760 | 1,472 | 131.6 |
| Star Wars Battlefront II | 398 | 1,623 | 941 | 130.2 |
| Watch Dogs | 581 | 2,131 | 1,277 | 121.4 |
| Rainbow Six Siege | 26,086 | 91,436 | 58,656 | 111.4 |

## 5. Hafta içi vs hafta sonu ortalaması

| oyun | hafta_sonu | hafta_ici |
|---|---|---|
| Rainbow Six Siege | 66,400 | 55,522 |
| Star Wars Battlefront II | 1,120 | 868 |
| Titanfall 2 | 1,795 | 1,341 |
| Watch Dogs | 1,455 | 1,205 |
| Watch Dogs 2 | 4,217 | 3,300 |

## 6. Mağaza verisi: fiyat, indirim, yorum puanı + anlık oyuncu (JOIN)

| oyun | anlik_oyuncu | fiyat | para_birimi | indirim_yuzde | toplam_yorum | olumlu_yuzde | steam_puani |
|---|---|---|---|---|---|---|---|
| Rainbow Six Siege | 83,796 | 0 | FREE | 0 | 1,563,248 | 82.1 | Very Positive |
| Watch Dogs 2 | 1,760 | 39.99 | USD | 0 | 105,217 | 82.1 | Very Positive |
| Star Wars Battlefront II | 1,265 | 39.99 | USD | 0 | 100,474 | 88.3 | Very Positive |
| Titanfall 2 | 1,165 | 29.99 | USD | 0 | 288,406 | 95.7 | Overwhelmingly Positive |
| Watch Dogs | 1,063 | 15.99 | USD | 0 | 54,014 | 79.8 | Mostly Positive |

## 7. İndirim etkisi: indirimli günlerde oyuncu sayısı artıyor mu? (JOIN + koşullu AVG)

| oyun | indirimli_gun | normal_gun | max_indirim_yuzde | ort_indirimli | ort_normal | fark_yuzde |
|---|---|---|---|---|---|---|
| Watch Dogs 2 | 4 | 9 | 95 | 5,047 | 3,044 | 65.8 |
| Watch Dogs | 4 | 9 | 90 | 1,603 | 1,181 | 35.7 |
| Titanfall 2 | 4 | 9 | 85 | 1,741 | 1,361 | 27.9 |
| Star Wars Battlefront II | 4 | 9 | 75 | 913 | 959 | -4.8 |
| Rainbow Six Siege | 0 | 13 | 0 | – | 58,121 | – |

## 8. İndirim × oyuncu sayısı korelasyonu (Pearson r, Python)

| oyun | gun_sayisi | pearson_r | yorum |
|---|---|---|---|
| Rainbow Six Siege | 13 | – | hesaplanamadı (indirim hiç değişmedi) |
| Star Wars Battlefront II | 13 | -0.150 | çok zayıf negatif |
| Titanfall 2 | 13 | +0.520 | orta pozitif |
| Watch Dogs | 13 | +0.588 | orta pozitif |
| Watch Dogs 2 | 13 | +0.698 | güçlü pozitif |

> r ≈ +1: indirim arttıkça oyuncu artıyor · r ≈ 0: ilişki yok · r ≈ −1: ters ilişki. Korelasyon nedensellik değildir; birkaç günlük veriyle sonuç güvenilir olmaz.
