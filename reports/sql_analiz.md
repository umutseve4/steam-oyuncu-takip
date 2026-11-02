# 🔎 SQL Analizi

_Otomatik üretildi: 02.11.2026 20:40 UTC · sorgular: [`queries.sql`](../queries.sql)_

## 1. Her oyunun en kalabalık olduğu saat (UTC, ortalamaya göre)

| oyun | zirve_saat_utc | zirve_saat_tr | ort_oyuncu | olcum |
|---|---|---|---|---|
| Rainbow Six Siege | 20:00 | 23:00 | 77,246 | 9 |
| Watch Dogs 2 | 13:00 | 16:00 | 5,572 | 3 |
| Titanfall 2 | 13:00 | 16:00 | 2,013 | 3 |
| Watch Dogs | 15:00 | 18:00 | 1,662 | 5 |
| Star Wars Battlefront II | 18:00 | 21:00 | 1,514 | 10 |

## 2. Günlük ortalama ve günlük değişim (%) — LAG window function

| oyun | gun | gunluk_ort | degisim_yuzde |
|---|---|---|---|
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
| Star Wars Battlefront II | 2026-11-02 | 958 | -25.2 |
| Star Wars Battlefront II | 2026-11-01 | 1,280 | 1.1 |
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

## 3. Her ölçümde oyunların sıralaması (son 5 ölçüm) — DENSE_RANK

| zaman_utc | oyun | oyuncu | sira |
|---|---|---|---|
| 2026-11-02T20:40:45+00:00 | Rainbow Six Siege | 67,099 | 1 |
| 2026-11-02T20:40:45+00:00 | Star Wars Battlefront II | 1,301 | 2 |
| 2026-11-02T20:40:45+00:00 | Watch Dogs 2 | 1,190 | 3 |
| 2026-11-02T20:40:45+00:00 | Titanfall 2 | 858 | 4 |
| 2026-11-02T20:40:45+00:00 | Watch Dogs | 683 | 5 |
| 2026-11-02T10:45:34+00:00 | Rainbow Six Siege | 26,959 | 1 |
| 2026-11-02T10:45:34+00:00 | Watch Dogs 2 | 1,556 | 2 |
| 2026-11-02T10:45:34+00:00 | Titanfall 2 | 966 | 3 |
| 2026-11-02T10:45:34+00:00 | Watch Dogs | 458 | 4 |
| 2026-11-02T10:45:34+00:00 | Star Wars Battlefront II | 453 | 5 |
| 2026-11-02T02:12:51+00:00 | Rainbow Six Siege | 70,658 | 1 |
| 2026-11-02T02:12:51+00:00 | Star Wars Battlefront II | 1,119 | 2 |
| 2026-11-02T02:12:51+00:00 | Watch Dogs 2 | 989 | 3 |
| 2026-11-02T02:12:51+00:00 | Titanfall 2 | 925 | 4 |
| 2026-11-02T02:12:51+00:00 | Watch Dogs | 507 | 5 |
| 2026-11-01T22:38:30+00:00 | Rainbow Six Siege | 73,576 | 1 |
| 2026-11-01T22:38:30+00:00 | Star Wars Battlefront II | 1,407 | 2 |
| 2026-11-01T22:38:30+00:00 | Watch Dogs 2 | 1,068 | 3 |
| 2026-11-01T22:38:30+00:00 | Titanfall 2 | 1,011 | 4 |
| 2026-11-01T22:38:30+00:00 | Watch Dogs | 631 | 5 |
| 2026-11-01T18:22:27+00:00 | Rainbow Six Siege | 76,807 | 1 |
| 2026-11-01T18:22:27+00:00 | Star Wars Battlefront II | 1,770 | 2 |
| 2026-11-01T18:22:27+00:00 | Watch Dogs 2 | 1,668 | 3 |
| 2026-11-01T18:22:27+00:00 | Titanfall 2 | 1,242 | 4 |
| 2026-11-01T18:22:27+00:00 | Watch Dogs | 857 | 5 |

## 4. Oynaklık: hangi oyunun oyuncu sayısı en çok dalgalanıyor? (max-min / ortalama)

| oyun | min | max | ort | dalga_yuzde |
|---|---|---|---|---|
| Watch Dogs 2 | 899 | 8,619 | 2,643 | 292.1 |
| Watch Dogs | 428 | 2,131 | 974 | 174.9 |
| Star Wars Battlefront II | 398 | 2,156 | 1,031 | 170.6 |
| Titanfall 2 | 662 | 2,760 | 1,280 | 164 |
| Rainbow Six Siege | 26,086 | 91,821 | 58,459 | 112.4 |

## 5. Hafta içi vs hafta sonu ortalaması

| oyun | hafta_sonu | hafta_ici |
|---|---|---|
| Rainbow Six Siege | 66,771 | 54,257 |
| Star Wars Battlefront II | 1,244 | 923 |
| Titanfall 2 | 1,536 | 1,150 |
| Watch Dogs | 1,104 | 907 |
| Watch Dogs 2 | 3,029 | 2,447 |

## 6. Mağaza verisi: fiyat, indirim, yorum puanı + anlık oyuncu (JOIN)

| oyun | anlik_oyuncu | fiyat | para_birimi | indirim_yuzde | toplam_yorum | olumlu_yuzde | steam_puani |
|---|---|---|---|---|---|---|---|
| Rainbow Six Siege | 67,099 | 0 | FREE | 0 | – | – | – |
| Star Wars Battlefront II | 1,301 | 39.99 | USD | 0 | – | – | – |
| Watch Dogs 2 | 1,190 | 39.99 | USD | 0 | – | – | – |
| Titanfall 2 | 858 | 29.99 | USD | 0 | – | – | – |
| Watch Dogs | 683 | 15.99 | USD | 0 | – | – | – |

## 7. İndirim etkisi: indirimli günlerde oyuncu sayısı artıyor mu? (JOIN + koşullu AVG)

| oyun | indirimli_gun | normal_gun | max_indirim_yuzde | ort_indirimli | ort_normal | fark_yuzde |
|---|---|---|---|---|---|---|
| Watch Dogs 2 | 4 | 25 | 95 | 5,047 | 2,298 | 119.6 |
| Watch Dogs | 4 | 25 | 90 | 1,603 | 884 | 81.3 |
| Titanfall 2 | 4 | 25 | 85 | 1,741 | 1,200 | 45.1 |
| Star Wars Battlefront II | 4 | 25 | 75 | 913 | 1,038 | -12 |
| Rainbow Six Siege | 0 | 29 | 0 | – | 57,677 | – |

## 8. İndirim × oyuncu sayısı korelasyonu (Pearson r, Python)

| oyun | gun_sayisi | pearson_r | yorum |
|---|---|---|---|
| Rainbow Six Siege | 29 | – | hesaplanamadı (indirim hiç değişmedi) |
| Star Wars Battlefront II | 29 | -0.225 | zayıf negatif |
| Titanfall 2 | 29 | +0.572 | orta pozitif |
| Watch Dogs | 29 | +0.642 | güçlü pozitif |
| Watch Dogs 2 | 29 | +0.737 | güçlü pozitif |

> r ≈ +1: indirim arttıkça oyuncu artıyor · r ≈ 0: ilişki yok · r ≈ −1: ters ilişki. Korelasyon nedensellik değildir; birkaç günlük veriyle sonuç güvenilir olmaz.
