# 🔎 SQL Analizi

_Otomatik üretildi: 22.10.2026 19:10 UTC · sorgular: [`queries.sql`](../queries.sql)_

## 1. Her oyunun en kalabalık olduğu saat (UTC, ortalamaya göre)

| oyun | zirve_saat_utc | zirve_saat_tr | ort_oyuncu | olcum |
|---|---|---|---|---|
| Rainbow Six Siege | 20:00 | 23:00 | 77,547 | 7 |
| Watch Dogs 2 | 10:00 | 13:00 | 5,796 | 2 |
| Titanfall 2 | 10:00 | 13:00 | 2,086 | 2 |
| Watch Dogs | 15:00 | 18:00 | 1,836 | 4 |
| Star Wars Battlefront II | 19:00 | 22:00 | 1,396 | 3 |

## 2. Günlük ortalama ve günlük değişim (%) — LAG window function

| oyun | gun | gunluk_ort | degisim_yuzde |
|---|---|---|---|
| Rainbow Six Siege | 2026-10-22 | 49,280 | -4.2 |
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
| Star Wars Battlefront II | 2026-10-22 | 930 | 6.8 |
| Star Wars Battlefront II | 2026-10-21 | 871 | 11.1 |
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
| Titanfall 2 | 2026-10-22 | 1,043 | 7.3 |
| Titanfall 2 | 2026-10-21 | 972 | 9.1 |
| Titanfall 2 | 2026-10-20 | 891 | -18.6 |
| Titanfall 2 | 2026-10-19 | 1,094 | -24.4 |
| Titanfall 2 | 2026-10-18 | 1,447 | -13.4 |
| Titanfall 2 | 2026-10-17 | 1,671 | 47.9 |
| Titanfall 2 | 2026-10-16 | 1,130 | 7.1 |
| Titanfall 2 | 2026-10-15 | 1,055 | -2 |
| Titanfall 2 | 2026-10-14 | 1,076 | -1.2 |
| Titanfall 2 | 2026-10-13 | 1,089 | -4.3 |

## 3. Her ölçümde oyunların sıralaması (son 5 ölçüm) — DENSE_RANK

| zaman_utc | oyun | oyuncu | sira |
|---|---|---|---|
| 2026-10-22T19:10:19+00:00 | Rainbow Six Siege | 66,174 | 1 |
| 2026-10-22T19:10:19+00:00 | Watch Dogs 2 | 1,531 | 2 |
| 2026-10-22T19:10:19+00:00 | Star Wars Battlefront II | 1,478 | 3 |
| 2026-10-22T19:10:19+00:00 | Titanfall 2 | 895 | 4 |
| 2026-10-22T19:10:19+00:00 | Watch Dogs | 876 | 5 |
| 2026-10-22T14:59:25+00:00 | Rainbow Six Siege | 50,002 | 1 |
| 2026-10-22T14:59:25+00:00 | Watch Dogs 2 | 3,445 | 2 |
| 2026-10-22T14:59:25+00:00 | Titanfall 2 | 1,561 | 3 |
| 2026-10-22T14:59:25+00:00 | Star Wars Battlefront II | 992 | 4 |
| 2026-10-22T14:59:25+00:00 | Watch Dogs | 949 | 5 |
| 2026-10-22T09:55:29+00:00 | Rainbow Six Siege | 27,891 | 1 |
| 2026-10-22T09:55:29+00:00 | Watch Dogs 2 | 2,160 | 2 |
| 2026-10-22T09:55:29+00:00 | Titanfall 2 | 902 | 3 |
| 2026-10-22T09:55:29+00:00 | Watch Dogs | 548 | 4 |
| 2026-10-22T09:55:29+00:00 | Star Wars Battlefront II | 482 | 5 |
| 2026-10-22T04:05:28+00:00 | Rainbow Six Siege | 53,051 | 1 |
| 2026-10-22T04:05:28+00:00 | Watch Dogs 2 | 1,283 | 2 |
| 2026-10-22T04:05:28+00:00 | Titanfall 2 | 812 | 3 |
| 2026-10-22T04:05:28+00:00 | Star Wars Battlefront II | 768 | 4 |
| 2026-10-22T04:05:28+00:00 | Watch Dogs | 541 | 5 |
| 2026-10-21T23:07:17+00:00 | Rainbow Six Siege | 62,087 | 1 |
| 2026-10-21T23:07:17+00:00 | Watch Dogs 2 | 978 | 2 |
| 2026-10-21T23:07:17+00:00 | Star Wars Battlefront II | 963 | 3 |
| 2026-10-21T23:07:17+00:00 | Titanfall 2 | 698 | 4 |
| 2026-10-21T23:07:17+00:00 | Watch Dogs | 533 | 5 |

## 4. Oynaklık: hangi oyunun oyuncu sayısı en çok dalgalanıyor? (max-min / ortalama)

| oyun | min | max | ort | dalga_yuzde |
|---|---|---|---|---|
| Watch Dogs 2 | 936 | 8,619 | 3,126 | 245.7 |
| Titanfall 2 | 698 | 2,760 | 1,361 | 151.5 |
| Watch Dogs | 523 | 2,131 | 1,142 | 140.8 |
| Star Wars Battlefront II | 398 | 1,623 | 930 | 131.8 |
| Rainbow Six Siege | 26,086 | 91,821 | 58,329 | 112.7 |

## 5. Hafta içi vs hafta sonu ortalaması

| oyun | hafta_sonu | hafta_ici |
|---|---|---|
| Rainbow Six Siege | 67,806 | 54,601 |
| Star Wars Battlefront II | 1,110 | 859 |
| Titanfall 2 | 1,694 | 1,231 |
| Watch Dogs | 1,360 | 1,056 |
| Watch Dogs 2 | 3,791 | 2,865 |

## 6. Mağaza verisi: fiyat, indirim, yorum puanı + anlık oyuncu (JOIN)

| oyun | anlik_oyuncu | fiyat | para_birimi | indirim_yuzde | toplam_yorum | olumlu_yuzde | steam_puani |
|---|---|---|---|---|---|---|---|
| Rainbow Six Siege | 66,174 | 0 | FREE | 0 | 1,564,576 | 82.1 | Very Positive |
| Watch Dogs 2 | 1,531 | 39.99 | USD | 0 | 105,471 | 82.1 | Very Positive |
| Star Wars Battlefront II | 1,478 | 39.99 | USD | 0 | 100,517 | 88.3 | Very Positive |
| Titanfall 2 | 895 | 29.99 | USD | 0 | 288,630 | 95.7 | Overwhelmingly Positive |
| Watch Dogs | 876 | 15.99 | USD | 0 | 54,127 | 79.8 | Mostly Positive |

## 7. İndirim etkisi: indirimli günlerde oyuncu sayısı artıyor mu? (JOIN + koşullu AVG)

| oyun | indirimli_gun | normal_gun | max_indirim_yuzde | ort_indirimli | ort_normal | fark_yuzde |
|---|---|---|---|---|---|---|
| Watch Dogs 2 | 4 | 14 | 95 | 5,047 | 2,707 | 86.5 |
| Watch Dogs | 4 | 14 | 90 | 1,603 | 1,049 | 52.8 |
| Titanfall 2 | 4 | 14 | 85 | 1,741 | 1,264 | 37.7 |
| Star Wars Battlefront II | 4 | 14 | 75 | 913 | 935 | -2.3 |
| Rainbow Six Siege | 0 | 18 | 0 | – | 57,640 | – |

## 8. İndirim × oyuncu sayısı korelasyonu (Pearson r, Python)

| oyun | gun_sayisi | pearson_r | yorum |
|---|---|---|---|
| Rainbow Six Siege | 18 | – | hesaplanamadı (indirim hiç değişmedi) |
| Star Wars Battlefront II | 18 | -0.067 | çok zayıf negatif |
| Titanfall 2 | 18 | +0.567 | orta pozitif |
| Watch Dogs | 18 | +0.623 | güçlü pozitif |
| Watch Dogs 2 | 18 | +0.727 | güçlü pozitif |

> r ≈ +1: indirim arttıkça oyuncu artıyor · r ≈ 0: ilişki yok · r ≈ −1: ters ilişki. Korelasyon nedensellik değildir; birkaç günlük veriyle sonuç güvenilir olmaz.
