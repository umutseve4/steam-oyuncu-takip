# 🔎 SQL Analizi

_Otomatik üretildi: 20.11.2026 11:08 UTC · sorgular: [`queries.sql`](../queries.sql)_

## 1. Her oyunun en kalabalık olduğu saat (UTC, ortalamaya göre)

| oyun | zirve_saat_utc | zirve_saat_tr | ort_oyuncu | olcum |
|---|---|---|---|---|
| Rainbow Six Siege | 20:00 | 23:00 | 74,665 | 11 |
| Watch Dogs 2 | 15:00 | 18:00 | 5,075 | 5 |
| Titanfall 2 | 15:00 | 18:00 | 1,972 | 5 |
| Watch Dogs | 15:00 | 18:00 | 1,662 | 5 |
| Star Wars Battlefront II | 19:00 | 22:00 | 1,481 | 5 |

## 2. Günlük ortalama ve günlük değişim (%) — LAG window function

| oyun | gun | gunluk_ort | degisim_yuzde |
|---|---|---|---|
| Rainbow Six Siege | 2026-11-20 | 39,927 | -12.9 |
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
| Star Wars Battlefront II | 2026-11-20 | 721 | -13.8 |

## 3. Her ölçümde oyunların sıralaması (son 5 ölçüm) — DENSE_RANK

| zaman_utc | oyun | oyuncu | sira |
|---|---|---|---|
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
| 2026-11-19T12:40:30+00:00 | Rainbow Six Siege | 28,988 | 1 |
| 2026-11-19T12:40:30+00:00 | Watch Dogs 2 | 2,713 | 2 |
| 2026-11-19T12:40:30+00:00 | Titanfall 2 | 980 | 3 |
| 2026-11-19T12:40:30+00:00 | Watch Dogs | 638 | 4 |
| 2026-11-19T12:40:30+00:00 | Star Wars Battlefront II | 504 | 5 |
| 2026-11-19T03:01:19+00:00 | Rainbow Six Siege | 56,679 | 1 |
| 2026-11-19T03:01:19+00:00 | Watch Dogs 2 | 1,176 | 2 |
| 2026-11-19T03:01:19+00:00 | Star Wars Battlefront II | 926 | 3 |
| 2026-11-19T03:01:19+00:00 | Titanfall 2 | 827 | 4 |
| 2026-11-19T03:01:19+00:00 | Watch Dogs | 464 | 5 |

## 4. Oynaklık: hangi oyunun oyuncu sayısı en çok dalgalanıyor? (max-min / ortalama)

| oyun | min | max | ort | dalga_yuzde |
|---|---|---|---|---|
| Watch Dogs 2 | 685 | 8,619 | 2,242 | 353.9 |
| Watch Dogs | 315 | 2,131 | 831 | 218.6 |
| Titanfall 2 | 628 | 2,760 | 1,182 | 180.4 |
| Star Wars Battlefront II | 398 | 2,156 | 1,019 | 172.6 |
| Rainbow Six Siege | 23,921 | 91,821 | 56,492 | 120.2 |

## 5. Hafta içi vs hafta sonu ortalaması

| oyun | hafta_sonu | hafta_ici |
|---|---|---|
| Rainbow Six Siege | 65,264 | 52,428 |
| Star Wars Battlefront II | 1,238 | 917 |
| Titanfall 2 | 1,444 | 1,061 |
| Watch Dogs | 973 | 765 |
| Watch Dogs 2 | 2,643 | 2,056 |

## 6. Mağaza verisi: fiyat, indirim, yorum puanı + anlık oyuncu (JOIN)

| oyun | anlik_oyuncu | fiyat | para_birimi | indirim_yuzde | toplam_yorum | olumlu_yuzde | steam_puani |
|---|---|---|---|---|---|---|---|
| Rainbow Six Siege | 26,645 | 0 | FREE | 0 | – | – | – |
| Watch Dogs 2 | 2,990 | 5.99 | USD | 85 | – | – | – |
| Titanfall 2 | 1,544 | 4.49 | USD | 85 | – | – | – |
| Watch Dogs | 635 | 3.99 | USD | 75 | – | – | – |
| Star Wars Battlefront II | 520 | 7.99 | USD | 80 | – | – | – |

## 7. İndirim etkisi: indirimli günlerde oyuncu sayısı artıyor mu? (JOIN + koşullu AVG)

| oyun | indirimli_gun | normal_gun | max_indirim_yuzde | ort_indirimli | ort_normal | fark_yuzde |
|---|---|---|---|---|---|---|
| Watch Dogs 2 | 6 | 41 | 95 | 4,036 | 1,904 | 112 |
| Watch Dogs | 6 | 41 | 90 | 1,265 | 735 | 72.2 |
| Titanfall 2 | 5 | 42 | 85 | 1,646 | 1,096 | 50.2 |
| Star Wars Battlefront II | 5 | 42 | 80 | 875 | 1,016 | -13.9 |
| Rainbow Six Siege | 0 | 47 | 0 | – | 55,220 | – |

## 8. İndirim × oyuncu sayısı korelasyonu (Pearson r, Python)

| oyun | gun_sayisi | pearson_r | yorum |
|---|---|---|---|
| Rainbow Six Siege | 47 | – | hesaplanamadı (indirim hiç değişmedi) |
| Star Wars Battlefront II | 47 | -0.249 | zayıf negatif |
| Titanfall 2 | 47 | +0.532 | orta pozitif |
| Watch Dogs | 47 | +0.500 | orta pozitif |
| Watch Dogs 2 | 47 | +0.609 | güçlü pozitif |

> r ≈ +1: indirim arttıkça oyuncu artıyor · r ≈ 0: ilişki yok · r ≈ −1: ters ilişki. Korelasyon nedensellik değildir; birkaç günlük veriyle sonuç güvenilir olmaz.
