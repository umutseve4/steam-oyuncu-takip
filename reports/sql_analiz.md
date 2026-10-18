# 🔎 SQL Analizi

_Otomatik üretildi: 18.10.2026 10:42 UTC · sorgular: [`queries.sql`](../queries.sql)_

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
| Rainbow Six Siege | 2026-10-18 | 59,810 | -14.1 |
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
| Star Wars Battlefront II | 2026-10-18 | 839 | -23.5 |
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
| Titanfall 2 | 2026-10-18 | 1,490 | -10.8 |
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
| Watch Dogs | 2026-10-18 | 981 | -15.9 |
| Watch Dogs | 2026-10-17 | 1,166 | 32 |

## 3. Her ölçümde oyunların sıralaması (son 5 ölçüm) — DENSE_RANK

| zaman_utc | oyun | oyuncu | sira |
|---|---|---|---|
| 2026-10-18T10:42:14+00:00 | Rainbow Six Siege | 44,301 | 1 |
| 2026-10-18T10:42:14+00:00 | Watch Dogs 2 | 3,705 | 2 |
| 2026-10-18T10:42:14+00:00 | Titanfall 2 | 1,667 | 3 |
| 2026-10-18T10:42:14+00:00 | Watch Dogs | 1,153 | 4 |
| 2026-10-18T10:42:14+00:00 | Star Wars Battlefront II | 834 | 5 |
| 2026-10-18T05:35:44+00:00 | Rainbow Six Siege | 61,993 | 1 |
| 2026-10-18T05:35:44+00:00 | Watch Dogs 2 | 3,472 | 2 |
| 2026-10-18T05:35:44+00:00 | Titanfall 2 | 1,710 | 3 |
| 2026-10-18T05:35:44+00:00 | Watch Dogs | 958 | 4 |
| 2026-10-18T05:35:44+00:00 | Star Wars Battlefront II | 724 | 5 |
| 2026-10-18T00:45:18+00:00 | Rainbow Six Siege | 73,136 | 1 |
| 2026-10-18T00:45:18+00:00 | Watch Dogs 2 | 1,548 | 2 |
| 2026-10-18T00:45:18+00:00 | Titanfall 2 | 1,092 | 3 |
| 2026-10-18T00:45:18+00:00 | Star Wars Battlefront II | 958 | 4 |
| 2026-10-18T00:45:18+00:00 | Watch Dogs | 833 | 5 |
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

## 4. Oynaklık: hangi oyunun oyuncu sayısı en çok dalgalanıyor? (max-min / ortalama)

| oyun | min | max | ort | dalga_yuzde |
|---|---|---|---|---|
| Watch Dogs 2 | 1,298 | 8,619 | 3,532 | 207.2 |
| Titanfall 2 | 823 | 2,760 | 1,473 | 131.5 |
| Star Wars Battlefront II | 398 | 1,623 | 936 | 130.9 |
| Watch Dogs | 581 | 2,131 | 1,263 | 122.7 |
| Rainbow Six Siege | 26,086 | 91,436 | 58,712 | 111.3 |

## 5. Hafta içi vs hafta sonu ortalaması

| oyun | hafta_sonu | hafta_ici |
|---|---|---|
| Rainbow Six Siege | 65,412 | 55,522 |
| Star Wars Battlefront II | 1,078 | 868 |
| Titanfall 2 | 1,750 | 1,341 |
| Watch Dogs | 1,384 | 1,205 |
| Watch Dogs 2 | 4,021 | 3,300 |

## 6. Mağaza verisi: fiyat, indirim, yorum puanı + anlık oyuncu (JOIN)

| oyun | anlik_oyuncu | fiyat | para_birimi | indirim_yuzde | toplam_yorum | olumlu_yuzde | steam_puani |
|---|---|---|---|---|---|---|---|
| Rainbow Six Siege | 44,301 | 0 | FREE | 0 | 1,563,487 | 82.1 | Very Positive |
| Watch Dogs 2 | 3,705 | 39.99 | USD | 0 | 105,307 | 82.1 | Very Positive |
| Titanfall 2 | 1,667 | 29.99 | USD | 0 | 288,465 | 95.7 | Overwhelmingly Positive |
| Watch Dogs | 1,153 | 15.99 | USD | 0 | 54,048 | 79.8 | Mostly Positive |
| Star Wars Battlefront II | 834 | 39.99 | USD | 0 | 100,481 | 88.3 | Very Positive |

## 7. İndirim etkisi: indirimli günlerde oyuncu sayısı artıyor mu? (JOIN + koşullu AVG)

| oyun | indirimli_gun | normal_gun | max_indirim_yuzde | ort_indirimli | ort_normal | fark_yuzde |
|---|---|---|---|---|---|---|
| Watch Dogs 2 | 4 | 10 | 95 | 5,047 | 3,030 | 66.6 |
| Watch Dogs | 4 | 10 | 90 | 1,603 | 1,161 | 38 |
| Titanfall 2 | 4 | 10 | 85 | 1,741 | 1,374 | 26.7 |
| Star Wars Battlefront II | 4 | 10 | 75 | 913 | 947 | -3.6 |
| Rainbow Six Siege | 0 | 14 | 0 | – | 58,242 | – |

## 8. İndirim × oyuncu sayısı korelasyonu (Pearson r, Python)

| oyun | gun_sayisi | pearson_r | yorum |
|---|---|---|---|
| Rainbow Six Siege | 14 | – | hesaplanamadı (indirim hiç değişmedi) |
| Star Wars Battlefront II | 14 | -0.110 | çok zayıf negatif |
| Titanfall 2 | 14 | +0.511 | orta pozitif |
| Watch Dogs | 14 | +0.604 | güçlü pozitif |
| Watch Dogs 2 | 14 | +0.706 | güçlü pozitif |

> r ≈ +1: indirim arttıkça oyuncu artıyor · r ≈ 0: ilişki yok · r ≈ −1: ters ilişki. Korelasyon nedensellik değildir; birkaç günlük veriyle sonuç güvenilir olmaz.
