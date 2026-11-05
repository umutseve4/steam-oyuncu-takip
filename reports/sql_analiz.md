# 🔎 SQL Analizi

_Otomatik üretildi: 05.11.2026 02:06 UTC · sorgular: [`queries.sql`](../queries.sql)_

## 1. Her oyunun en kalabalık olduğu saat (UTC, ortalamaya göre)

| oyun | zirve_saat_utc | zirve_saat_tr | ort_oyuncu | olcum |
|---|---|---|---|---|
| Rainbow Six Siege | 20:00 | 23:00 | 77,246 | 9 |
| Watch Dogs 2 | 13:00 | 16:00 | 5,572 | 3 |
| Titanfall 2 | 13:00 | 16:00 | 2,013 | 3 |
| Watch Dogs | 15:00 | 18:00 | 1,662 | 5 |
| Star Wars Battlefront II | 18:00 | 21:00 | 1,495 | 11 |

## 2. Günlük ortalama ve günlük değişim (%) — LAG window function

| oyun | gun | gunluk_ort | degisim_yuzde |
|---|---|---|---|
| Rainbow Six Siege | 2026-11-05 | 63,224 | 34.1 |
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
| Star Wars Battlefront II | 2026-11-05 | 1,085 | 10 |
| Star Wars Battlefront II | 2026-11-04 | 986 | 0.7 |
| Star Wars Battlefront II | 2026-11-03 | 979 | 2.2 |
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

## 3. Her ölçümde oyunların sıralaması (son 5 ölçüm) — DENSE_RANK

| zaman_utc | oyun | oyuncu | sira |
|---|---|---|---|
| 2026-11-05T02:04:51+00:00 | Rainbow Six Siege | 63,224 | 1 |
| 2026-11-05T02:04:51+00:00 | Star Wars Battlefront II | 1,085 | 2 |
| 2026-11-05T02:04:51+00:00 | Titanfall 2 | 781 | 3 |
| 2026-11-05T02:04:51+00:00 | Watch Dogs 2 | 764 | 4 |
| 2026-11-05T02:04:51+00:00 | Watch Dogs | 377 | 5 |
| 2026-11-04T21:08:46+00:00 | Rainbow Six Siege | 61,633 | 1 |
| 2026-11-04T21:08:46+00:00 | Star Wars Battlefront II | 1,403 | 2 |
| 2026-11-04T21:08:46+00:00 | Watch Dogs 2 | 928 | 3 |
| 2026-11-04T21:08:46+00:00 | Titanfall 2 | 828 | 4 |
| 2026-11-04T21:08:46+00:00 | Watch Dogs | 530 | 5 |
| 2026-11-04T14:04:56+00:00 | Rainbow Six Siege | 39,072 | 1 |
| 2026-11-04T14:04:56+00:00 | Watch Dogs 2 | 2,352 | 2 |
| 2026-11-04T14:04:56+00:00 | Titanfall 2 | 1,480 | 3 |
| 2026-11-04T14:04:56+00:00 | Star Wars Battlefront II | 818 | 4 |
| 2026-11-04T14:04:56+00:00 | Watch Dogs | 686 | 5 |
| 2026-11-04T05:39:43+00:00 | Rainbow Six Siege | 40,741 | 1 |
| 2026-11-04T05:39:43+00:00 | Watch Dogs 2 | 1,221 | 2 |
| 2026-11-04T05:39:43+00:00 | Titanfall 2 | 877 | 3 |
| 2026-11-04T05:39:43+00:00 | Star Wars Battlefront II | 737 | 4 |
| 2026-11-04T05:39:43+00:00 | Watch Dogs | 416 | 5 |
| 2026-11-03T23:54:56+00:00 | Rainbow Six Siege | 58,388 | 1 |
| 2026-11-03T23:54:56+00:00 | Star Wars Battlefront II | 1,009 | 2 |
| 2026-11-03T23:54:56+00:00 | Watch Dogs 2 | 756 | 3 |
| 2026-11-03T23:54:56+00:00 | Titanfall 2 | 640 | 4 |
| 2026-11-03T23:54:56+00:00 | Watch Dogs | 412 | 5 |

## 4. Oynaklık: hangi oyunun oyuncu sayısı en çok dalgalanıyor? (max-min / ortalama)

| oyun | min | max | ort | dalga_yuzde |
|---|---|---|---|---|
| Watch Dogs 2 | 756 | 8,619 | 2,564 | 306.6 |
| Watch Dogs | 377 | 2,131 | 947 | 185.2 |
| Star Wars Battlefront II | 398 | 2,156 | 1,029 | 170.9 |
| Titanfall 2 | 640 | 2,760 | 1,259 | 168.4 |
| Rainbow Six Siege | 25,644 | 91,821 | 58,075 | 114 |

## 5. Hafta içi vs hafta sonu ortalaması

| oyun | hafta_sonu | hafta_ici |
|---|---|---|
| Rainbow Six Siege | 66,771 | 54,034 |
| Star Wars Battlefront II | 1,244 | 929 |
| Titanfall 2 | 1,536 | 1,130 |
| Watch Dogs | 1,104 | 874 |
| Watch Dogs 2 | 3,029 | 2,348 |

## 6. Mağaza verisi: fiyat, indirim, yorum puanı + anlık oyuncu (JOIN)

| oyun | anlik_oyuncu | fiyat | para_birimi | indirim_yuzde | toplam_yorum | olumlu_yuzde | steam_puani |
|---|---|---|---|---|---|---|---|
| Rainbow Six Siege | 63,224 | 0 | FREE | 0 | – | – | – |
| Star Wars Battlefront II | 1,085 | 39.99 | USD | 0 | – | – | – |
| Titanfall 2 | 781 | 29.99 | USD | 0 | – | – | – |
| Watch Dogs 2 | 764 | 39.99 | USD | 0 | – | – | – |
| Watch Dogs | 377 | 15.99 | USD | 0 | – | – | – |

## 7. İndirim etkisi: indirimli günlerde oyuncu sayısı artıyor mu? (JOIN + koşullu AVG)

| oyun | indirimli_gun | normal_gun | max_indirim_yuzde | ort_indirimli | ort_normal | fark_yuzde |
|---|---|---|---|---|---|---|
| Watch Dogs 2 | 4 | 28 | 95 | 5,047 | 2,173 | 132.3 |
| Watch Dogs | 4 | 28 | 90 | 1,603 | 839 | 90.9 |
| Titanfall 2 | 4 | 28 | 85 | 1,741 | 1,167 | 49.2 |
| Star Wars Battlefront II | 4 | 28 | 75 | 913 | 1,035 | -11.8 |
| Rainbow Six Siege | 0 | 32 | 0 | – | 57,338 | – |

## 8. İndirim × oyuncu sayısı korelasyonu (Pearson r, Python)

| oyun | gun_sayisi | pearson_r | yorum |
|---|---|---|---|
| Rainbow Six Siege | 32 | – | hesaplanamadı (indirim hiç değişmedi) |
| Star Wars Battlefront II | 32 | -0.222 | zayıf negatif |
| Titanfall 2 | 32 | +0.571 | orta pozitif |
| Watch Dogs | 32 | +0.635 | güçlü pozitif |
| Watch Dogs 2 | 32 | +0.726 | güçlü pozitif |

> r ≈ +1: indirim arttıkça oyuncu artıyor · r ≈ 0: ilişki yok · r ≈ −1: ters ilişki. Korelasyon nedensellik değildir; birkaç günlük veriyle sonuç güvenilir olmaz.
