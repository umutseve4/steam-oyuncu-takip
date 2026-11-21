# 🔎 SQL Analizi

_Otomatik üretildi: 21.11.2026 01:15 UTC · sorgular: [`queries.sql`](../queries.sql)_

## 1. Her oyunun en kalabalık olduğu saat (UTC, ortalamaya göre)

| oyun | zirve_saat_utc | zirve_saat_tr | ort_oyuncu | olcum |
|---|---|---|---|---|
| Rainbow Six Siege | 20:00 | 23:00 | 74,665 | 11 |
| Watch Dogs 2 | 15:00 | 18:00 | 5,075 | 5 |
| Titanfall 2 | 15:00 | 18:00 | 1,972 | 5 |
| Watch Dogs | 15:00 | 18:00 | 1,662 | 5 |
| Star Wars Battlefront II | 19:00 | 22:00 | 1,482 | 6 |

## 2. Günlük ortalama ve günlük değişim (%) — LAG window function

| oyun | gun | gunluk_ort | degisim_yuzde |
|---|---|---|---|
| Rainbow Six Siege | 2026-11-21 | 55,143 | 23.5 |
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
| Rainbow Six Siege | 2026-10-07 | 52,319 | -1.9 |
| Rainbow Six Siege | 2026-10-06 | 53,345 | -4.7 |
| Rainbow Six Siege | 2026-10-05 | 55,958 | 3.7 |
| Rainbow Six Siege | 2026-10-03 | 53,977 | -21.5 |
| Rainbow Six Siege | 2026-10-02 | 68,763 | – |

## 3. Her ölçümde oyunların sıralaması (son 5 ölçüm) — DENSE_RANK

| zaman_utc | oyun | oyuncu | sira |
|---|---|---|---|
| 2026-11-21T01:13:48+00:00 | Rainbow Six Siege | 55,143 | 1 |
| 2026-11-21T01:13:48+00:00 | Watch Dogs 2 | 1,662 | 2 |
| 2026-11-21T01:13:48+00:00 | Titanfall 2 | 1,366 | 3 |
| 2026-11-21T01:13:48+00:00 | Star Wars Battlefront II | 1,119 | 4 |
| 2026-11-21T01:13:48+00:00 | Watch Dogs | 674 | 5 |
| 2026-11-20T19:49:50+00:00 | Rainbow Six Siege | 54,087 | 1 |
| 2026-11-20T19:49:50+00:00 | Watch Dogs 2 | 2,487 | 2 |
| 2026-11-20T19:49:50+00:00 | Star Wars Battlefront II | 1,483 | 3 |
| 2026-11-20T19:49:50+00:00 | Titanfall 2 | 1,395 | 4 |
| 2026-11-20T19:49:50+00:00 | Watch Dogs | 958 | 5 |
| 2026-11-20T11:08:22+00:00 | Rainbow Six Siege | 26,645 | 1 |
| 2026-11-20T11:08:22+00:00 | Watch Dogs 2 | 2,990 | 2 |
| 2026-11-20T11:08:22+00:00 | Titanfall 2 | 1,544 | 3 |
| 2026-11-20T11:08:22+00:00 | Watch Dogs | 635 | 4 |
| 2026-11-20T11:08:22+00:00 | Star Wars Battlefront II | 520 | 5 |
| 2026-11-20T02:53:51+00:00 | Rainbow Six Siege | 53,209 | 1 |
| 2026-11-20T02:53:51+00:00 | Watch Dogs 2 | 1,507 | 2 |
| 2026-11-20T02:53:51+00:00 | Titanfall 2 | 994 | 3 |
| 2026-11-20T02:53:51+00:00 | Star Wars Battlefront II | 921 | 4 |
| 2026-11-20T02:53:51+00:00 | Watch Dogs | 556 | 5 |
| 2026-11-19T21:15:29+00:00 | Rainbow Six Siege | 51,818 | 1 |
| 2026-11-19T21:15:29+00:00 | Watch Dogs 2 | 1,450 | 2 |
| 2026-11-19T21:15:29+00:00 | Star Wars Battlefront II | 1,077 | 3 |
| 2026-11-19T21:15:29+00:00 | Titanfall 2 | 770 | 4 |
| 2026-11-19T21:15:29+00:00 | Watch Dogs | 655 | 5 |

## 4. Oynaklık: hangi oyunun oyuncu sayısı en çok dalgalanıyor? (max-min / ortalama)

| oyun | min | max | ort | dalga_yuzde |
|---|---|---|---|---|
| Watch Dogs 2 | 685 | 8,619 | 2,240 | 354.2 |
| Watch Dogs | 315 | 2,131 | 831 | 218.7 |
| Titanfall 2 | 628 | 2,760 | 1,184 | 180.1 |
| Star Wars Battlefront II | 398 | 2,156 | 1,022 | 172.1 |
| Rainbow Six Siege | 23,921 | 91,821 | 56,473 | 120.2 |

## 5. Hafta içi vs hafta sonu ortalaması

| oyun | hafta_sonu | hafta_ici |
|---|---|---|
| Rainbow Six Siege | 65,106 | 52,440 |
| Star Wars Battlefront II | 1,236 | 921 |
| Titanfall 2 | 1,443 | 1,063 |
| Watch Dogs | 968 | 766 |
| Watch Dogs 2 | 2,628 | 2,059 |

## 6. Mağaza verisi: fiyat, indirim, yorum puanı + anlık oyuncu (JOIN)

| oyun | anlik_oyuncu | fiyat | para_birimi | indirim_yuzde | toplam_yorum | olumlu_yuzde | steam_puani |
|---|---|---|---|---|---|---|---|
| Rainbow Six Siege | 55,143 | 0 | FREE | 0 | – | – | – |
| Watch Dogs 2 | 1,662 | 5.99 | USD | 85 | – | – | – |
| Titanfall 2 | 1,366 | 4.49 | USD | 85 | – | – | – |
| Star Wars Battlefront II | 1,119 | 7.99 | USD | 80 | – | – | – |
| Watch Dogs | 674 | 3.99 | USD | 75 | – | – | – |

## 7. İndirim etkisi: indirimli günlerde oyuncu sayısı artıyor mu? (JOIN + koşullu AVG)

| oyun | indirimli_gun | normal_gun | max_indirim_yuzde | ort_indirimli | ort_normal | fark_yuzde |
|---|---|---|---|---|---|---|
| Watch Dogs 2 | 7 | 41 | 95 | 3,708 | 1,904 | 94.8 |
| Watch Dogs | 7 | 41 | 90 | 1,198 | 735 | 63 |
| Titanfall 2 | 6 | 42 | 85 | 1,607 | 1,096 | 46.6 |
| Star Wars Battlefront II | 6 | 42 | 80 | 958 | 1,016 | -5.7 |
| Rainbow Six Siege | 0 | 48 | 0 | – | 55,317 | – |

## 8. İndirim × oyuncu sayısı korelasyonu (Pearson r, Python)

| oyun | gun_sayisi | pearson_r | yorum |
|---|---|---|---|
| Rainbow Six Siege | 48 | – | hesaplanamadı (indirim hiç değişmedi) |
| Star Wars Battlefront II | 48 | -0.108 | çok zayıf negatif |
| Titanfall 2 | 48 | +0.532 | orta pozitif |
| Watch Dogs | 48 | +0.475 | orta pozitif |
| Watch Dogs 2 | 48 | +0.558 | orta pozitif |

> r ≈ +1: indirim arttıkça oyuncu artıyor · r ≈ 0: ilişki yok · r ≈ −1: ters ilişki. Korelasyon nedensellik değildir; birkaç günlük veriyle sonuç güvenilir olmaz.
