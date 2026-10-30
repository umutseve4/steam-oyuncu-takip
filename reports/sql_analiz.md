# 🔎 SQL Analizi

_Otomatik üretildi: 30.10.2026 22:52 UTC · sorgular: [`queries.sql`](../queries.sql)_

## 1. Her oyunun en kalabalık olduğu saat (UTC, ortalamaya göre)

| oyun | zirve_saat_utc | zirve_saat_tr | ort_oyuncu | olcum |
|---|---|---|---|---|
| Rainbow Six Siege | 20:00 | 23:00 | 78,514 | 8 |
| Watch Dogs 2 | 15:00 | 18:00 | 5,577 | 4 |
| Titanfall 2 | 13:00 | 16:00 | 2,013 | 3 |
| Watch Dogs | 15:00 | 18:00 | 1,836 | 4 |
| Star Wars Battlefront II | 18:00 | 21:00 | 1,485 | 9 |

## 2. Günlük ortalama ve günlük değişim (%) — LAG window function

| oyun | gun | gunluk_ort | degisim_yuzde |
|---|---|---|---|
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
| Star Wars Battlefront II | 2026-10-12 | 961 | -20.9 |
| Star Wars Battlefront II | 2026-10-11 | 1,215 | 5.6 |
| Star Wars Battlefront II | 2026-10-10 | 1,151 | 17.7 |
| Star Wars Battlefront II | 2026-10-09 | 978 | 13.9 |

## 3. Her ölçümde oyunların sıralaması (son 5 ölçüm) — DENSE_RANK

| zaman_utc | oyun | oyuncu | sira |
|---|---|---|---|
| 2026-10-30T22:52:09+00:00 | Rainbow Six Siege | 73,484 | 1 |
| 2026-10-30T22:52:09+00:00 | Star Wars Battlefront II | 1,437 | 2 |
| 2026-10-30T22:52:09+00:00 | Watch Dogs 2 | 1,060 | 3 |
| 2026-10-30T22:52:09+00:00 | Titanfall 2 | 957 | 4 |
| 2026-10-30T22:52:09+00:00 | Watch Dogs | 553 | 5 |
| 2026-10-30T18:29:06+00:00 | Rainbow Six Siege | 59,728 | 1 |
| 2026-10-30T18:29:06+00:00 | Watch Dogs 2 | 1,639 | 2 |
| 2026-10-30T18:29:06+00:00 | Star Wars Battlefront II | 1,506 | 3 |
| 2026-10-30T18:29:06+00:00 | Titanfall 2 | 1,046 | 4 |
| 2026-10-30T18:29:06+00:00 | Watch Dogs | 727 | 5 |
| 2026-10-30T12:29:24+00:00 | Rainbow Six Siege | 40,699 | 1 |
| 2026-10-30T12:29:24+00:00 | Watch Dogs 2 | 2,745 | 2 |
| 2026-10-30T12:29:24+00:00 | Titanfall 2 | 1,455 | 3 |
| 2026-10-30T12:29:24+00:00 | Star Wars Battlefront II | 749 | 4 |
| 2026-10-30T12:29:24+00:00 | Watch Dogs | 654 | 5 |
| 2026-10-30T05:08:27+00:00 | Rainbow Six Siege | 41,359 | 1 |
| 2026-10-30T05:08:27+00:00 | Watch Dogs 2 | 1,433 | 2 |
| 2026-10-30T05:08:27+00:00 | Titanfall 2 | 991 | 3 |
| 2026-10-30T05:08:27+00:00 | Star Wars Battlefront II | 709 | 4 |
| 2026-10-30T05:08:27+00:00 | Watch Dogs | 436 | 5 |
| 2026-10-29T23:10:03+00:00 | Rainbow Six Siege | 68,861 | 1 |
| 2026-10-29T23:10:03+00:00 | Star Wars Battlefront II | 1,251 | 2 |
| 2026-10-29T23:10:03+00:00 | Watch Dogs 2 | 963 | 3 |
| 2026-10-29T23:10:03+00:00 | Titanfall 2 | 788 | 4 |
| 2026-10-29T23:10:03+00:00 | Watch Dogs | 496 | 5 |

## 4. Oynaklık: hangi oyunun oyuncu sayısı en çok dalgalanıyor? (max-min / ortalama)

| oyun | min | max | ort | dalga_yuzde |
|---|---|---|---|---|
| Watch Dogs 2 | 899 | 8,619 | 2,724 | 283.4 |
| Star Wars Battlefront II | 398 | 2,156 | 1,015 | 173.2 |
| Watch Dogs | 428 | 2,131 | 1,002 | 170 |
| Titanfall 2 | 662 | 2,760 | 1,283 | 163.6 |
| Rainbow Six Siege | 26,086 | 91,821 | 58,288 | 112.8 |

## 5. Hafta içi vs hafta sonu ortalaması

| oyun | hafta_sonu | hafta_ici |
|---|---|---|
| Rainbow Six Siege | 67,927 | 54,235 |
| Star Wars Battlefront II | 1,237 | 922 |
| Titanfall 2 | 1,580 | 1,158 |
| Watch Dogs | 1,196 | 920 |
| Watch Dogs 2 | 3,286 | 2,488 |

## 6. Mağaza verisi: fiyat, indirim, yorum puanı + anlık oyuncu (JOIN)

| oyun | anlik_oyuncu | fiyat | para_birimi | indirim_yuzde | toplam_yorum | olumlu_yuzde | steam_puani |
|---|---|---|---|---|---|---|---|
| Rainbow Six Siege | 73,484 | 0 | FREE | 0 | – | – | – |
| Star Wars Battlefront II | 1,437 | 39.99 | USD | 0 | – | – | – |
| Watch Dogs 2 | 1,060 | 39.99 | USD | 0 | – | – | – |
| Titanfall 2 | 957 | 29.99 | USD | 0 | – | – | – |
| Watch Dogs | 553 | 15.99 | USD | 0 | – | – | – |

## 7. İndirim etkisi: indirimli günlerde oyuncu sayısı artıyor mu? (JOIN + koşullu AVG)

| oyun | indirimli_gun | normal_gun | max_indirim_yuzde | ort_indirimli | ort_normal | fark_yuzde |
|---|---|---|---|---|---|---|
| Watch Dogs 2 | 4 | 22 | 95 | 5,047 | 2,375 | 112.5 |
| Watch Dogs | 4 | 22 | 90 | 1,603 | 913 | 75.5 |
| Titanfall 2 | 4 | 22 | 85 | 1,741 | 1,199 | 45.2 |
| Star Wars Battlefront II | 4 | 22 | 75 | 913 | 1,020 | -10.5 |
| Rainbow Six Siege | 0 | 26 | 0 | – | 57,442 | – |

## 8. İndirim × oyuncu sayısı korelasyonu (Pearson r, Python)

| oyun | gun_sayisi | pearson_r | yorum |
|---|---|---|---|
| Rainbow Six Siege | 26 | – | hesaplanamadı (indirim hiç değişmedi) |
| Star Wars Battlefront II | 26 | -0.205 | zayıf negatif |
| Titanfall 2 | 26 | +0.582 | orta pozitif |
| Watch Dogs | 26 | +0.636 | güçlü pozitif |
| Watch Dogs 2 | 26 | +0.735 | güçlü pozitif |

> r ≈ +1: indirim arttıkça oyuncu artıyor · r ≈ 0: ilişki yok · r ≈ −1: ters ilişki. Korelasyon nedensellik değildir; birkaç günlük veriyle sonuç güvenilir olmaz.
