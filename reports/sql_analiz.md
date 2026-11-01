# 🔎 SQL Analizi

_Otomatik üretildi: 01.11.2026 12:57 UTC · sorgular: [`queries.sql`](../queries.sql)_

## 1. Her oyunun en kalabalık olduğu saat (UTC, ortalamaya göre)

| oyun | zirve_saat_utc | zirve_saat_tr | ort_oyuncu | olcum |
|---|---|---|---|---|
| Rainbow Six Siege | 20:00 | 23:00 | 78,514 | 8 |
| Watch Dogs 2 | 13:00 | 16:00 | 5,572 | 3 |
| Titanfall 2 | 13:00 | 16:00 | 2,013 | 3 |
| Watch Dogs | 15:00 | 18:00 | 1,662 | 5 |
| Star Wars Battlefront II | 18:00 | 21:00 | 1,485 | 9 |

## 2. Günlük ortalama ve günlük değişim (%) — LAG window function

| oyun | gun | gunluk_ort | degisim_yuzde |
|---|---|---|---|
| Rainbow Six Siege | 2026-11-01 | 50,813 | -17 |
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
| Star Wars Battlefront II | 2026-11-01 | 972 | -23.2 |
| Star Wars Battlefront II | 2026-10-31 | 1,266 | 15.1 |
| Star Wars Battlefront II | 2026-10-30 | 1,100 | 6.8 |
| Star Wars Battlefront II | 2026-10-29 | 1,030 | -3 |
| Star Wars Battlefront II | 2026-10-28 | 1,062 | -0.4 |
| Star Wars Battlefront II | 2026-10-27 | 1,066 | 6.8 |
| Star Wars Battlefront II | 2026-10-26 | 998 | -34.6 |
| Star Wars Battlefront II | 2026-10-25 | 1,527 | 7.2 |
| Star Wars Battlefront II | 2026-10-24 | 1,425 | 25.3 |
| Star Wars Battlefront II | 2026-10-23 | 1,137 | 21.9 |
| Star Wars Battlefront II | 2026-10-22 | 933 | 7.1 |
| Star Wars Battlefront II | 2026-10-21 | 871 | 11.1 |
| Star Wars Battlefront II | 2026-10-20 | 784 | -0.4 |
| Star Wars Battlefront II | 2026-10-19 | 787 | -27.6 |
| Star Wars Battlefront II | 2026-10-18 | 1,087 | -0.9 |
| Star Wars Battlefront II | 2026-10-17 | 1,097 | 30 |
| Star Wars Battlefront II | 2026-10-16 | 844 | 8.8 |
| Star Wars Battlefront II | 2026-10-15 | 776 | -4.4 |
| Star Wars Battlefront II | 2026-10-14 | 812 | 1.8 |
| Star Wars Battlefront II | 2026-10-13 | 798 | -17 |

## 3. Her ölçümde oyunların sıralaması (son 5 ölçüm) — DENSE_RANK

| zaman_utc | oyun | oyuncu | sira |
|---|---|---|---|
| 2026-11-01T12:57:25+00:00 | Rainbow Six Siege | 50,866 | 1 |
| 2026-11-01T12:57:25+00:00 | Watch Dogs 2 | 2,922 | 2 |
| 2026-11-01T12:57:25+00:00 | Titanfall 2 | 1,673 | 3 |
| 2026-11-01T12:57:25+00:00 | Star Wars Battlefront II | 1,068 | 4 |
| 2026-11-01T12:57:25+00:00 | Watch Dogs | 888 | 5 |
| 2026-11-01T05:22:03+00:00 | Rainbow Six Siege | 50,759 | 1 |
| 2026-11-01T05:22:03+00:00 | Watch Dogs 2 | 2,259 | 2 |
| 2026-11-01T05:22:03+00:00 | Titanfall 2 | 1,481 | 3 |
| 2026-11-01T05:22:03+00:00 | Star Wars Battlefront II | 876 | 4 |
| 2026-11-01T05:22:03+00:00 | Watch Dogs | 608 | 5 |
| 2026-10-31T23:13:32+00:00 | Rainbow Six Siege | 63,585 | 1 |
| 2026-10-31T23:13:32+00:00 | Star Wars Battlefront II | 1,314 | 2 |
| 2026-10-31T23:13:32+00:00 | Watch Dogs 2 | 1,102 | 3 |
| 2026-10-31T23:13:32+00:00 | Titanfall 2 | 948 | 4 |
| 2026-10-31T23:13:32+00:00 | Watch Dogs | 599 | 5 |
| 2026-10-31T19:48:45+00:00 | Rainbow Six Siege | 75,388 | 1 |
| 2026-10-31T19:48:45+00:00 | Star Wars Battlefront II | 1,706 | 2 |
| 2026-10-31T19:48:45+00:00 | Watch Dogs 2 | 1,630 | 3 |
| 2026-10-31T19:48:45+00:00 | Titanfall 2 | 1,216 | 4 |
| 2026-10-31T19:48:45+00:00 | Watch Dogs | 760 | 5 |
| 2026-10-31T15:39:11+00:00 | Rainbow Six Siege | 64,973 | 1 |
| 2026-10-31T15:39:11+00:00 | Watch Dogs 2 | 3,068 | 2 |
| 2026-10-31T15:39:11+00:00 | Titanfall 2 | 1,944 | 3 |
| 2026-10-31T15:39:11+00:00 | Star Wars Battlefront II | 1,414 | 4 |
| 2026-10-31T15:39:11+00:00 | Watch Dogs | 966 | 5 |

## 4. Oynaklık: hangi oyunun oyuncu sayısı en çok dalgalanıyor? (max-min / ortalama)

| oyun | min | max | ort | dalga_yuzde |
|---|---|---|---|---|
| Watch Dogs 2 | 899 | 8,619 | 2,694 | 286.6 |
| Watch Dogs | 428 | 2,131 | 987 | 172.6 |
| Star Wars Battlefront II | 398 | 2,156 | 1,024 | 171.7 |
| Titanfall 2 | 662 | 2,760 | 1,290 | 162.6 |
| Rainbow Six Siege | 26,086 | 91,821 | 58,286 | 112.8 |

## 5. Hafta içi vs hafta sonu ortalaması

| oyun | hafta_sonu | hafta_ici |
|---|---|---|
| Rainbow Six Siege | 66,388 | 54,235 |
| Star Wars Battlefront II | 1,229 | 922 |
| Titanfall 2 | 1,555 | 1,158 |
| Watch Dogs | 1,121 | 920 |
| Watch Dogs 2 | 3,105 | 2,488 |

## 6. Mağaza verisi: fiyat, indirim, yorum puanı + anlık oyuncu (JOIN)

| oyun | anlik_oyuncu | fiyat | para_birimi | indirim_yuzde | toplam_yorum | olumlu_yuzde | steam_puani |
|---|---|---|---|---|---|---|---|
| Rainbow Six Siege | 50,866 | 0 | FREE | 0 | – | – | – |
| Watch Dogs 2 | 2,922 | 39.99 | USD | 0 | – | – | – |
| Titanfall 2 | 1,673 | 29.99 | USD | 0 | – | – | – |
| Star Wars Battlefront II | 1,068 | 39.99 | USD | 0 | – | – | – |
| Watch Dogs | 888 | 15.99 | USD | 0 | – | – | – |

## 7. İndirim etkisi: indirimli günlerde oyuncu sayısı artıyor mu? (JOIN + koşullu AVG)

| oyun | indirimli_gun | normal_gun | max_indirim_yuzde | ort_indirimli | ort_normal | fark_yuzde |
|---|---|---|---|---|---|---|
| Watch Dogs 2 | 4 | 24 | 95 | 5,047 | 2,367 | 113.2 |
| Watch Dogs | 4 | 24 | 90 | 1,603 | 898 | 78.5 |
| Titanfall 2 | 4 | 24 | 85 | 1,741 | 1,221 | 42.5 |
| Star Wars Battlefront II | 4 | 24 | 75 | 913 | 1,028 | -11.2 |
| Rainbow Six Siege | 0 | 28 | 0 | – | 57,340 | – |

## 8. İndirim × oyuncu sayısı korelasyonu (Pearson r, Python)

| oyun | gun_sayisi | pearson_r | yorum |
|---|---|---|---|
| Rainbow Six Siege | 28 | – | hesaplanamadı (indirim hiç değişmedi) |
| Star Wars Battlefront II | 28 | -0.215 | zayıf negatif |
| Titanfall 2 | 28 | +0.553 | orta pozitif |
| Watch Dogs | 28 | +0.642 | güçlü pozitif |
| Watch Dogs 2 | 28 | +0.737 | güçlü pozitif |

> r ≈ +1: indirim arttıkça oyuncu artıyor · r ≈ 0: ilişki yok · r ≈ −1: ters ilişki. Korelasyon nedensellik değildir; birkaç günlük veriyle sonuç güvenilir olmaz.
