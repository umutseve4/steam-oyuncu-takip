# 🔎 SQL Analizi

_Otomatik üretildi: 07.11.2026 00:47 UTC · sorgular: [`queries.sql`](../queries.sql)_

## 1. Her oyunun en kalabalık olduğu saat (UTC, ortalamaya göre)

| oyun | zirve_saat_utc | zirve_saat_tr | ort_oyuncu | olcum |
|---|---|---|---|---|
| Rainbow Six Siege | 20:00 | 23:00 | 76,094 | 10 |
| Watch Dogs 2 | 13:00 | 16:00 | 5,572 | 3 |
| Titanfall 2 | 13:00 | 16:00 | 2,013 | 3 |
| Watch Dogs | 15:00 | 18:00 | 1,662 | 5 |
| Star Wars Battlefront II | 19:00 | 22:00 | 1,481 | 5 |

## 2. Günlük ortalama ve günlük değişim (%) — LAG window function

| oyun | gun | gunluk_ort | degisim_yuzde |
|---|---|---|---|
| Rainbow Six Siege | 2026-11-07 | 64,061 | 28.9 |
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
| Star Wars Battlefront II | 2026-11-07 | 1,183 | 21.2 |
| Star Wars Battlefront II | 2026-11-06 | 976 | 4.5 |
| Star Wars Battlefront II | 2026-11-05 | 934 | -5.3 |
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

## 3. Her ölçümde oyunların sıralaması (son 5 ölçüm) — DENSE_RANK

| zaman_utc | oyun | oyuncu | sira |
|---|---|---|---|
| 2026-11-07T00:45:37+00:00 | Rainbow Six Siege | 64,061 | 1 |
| 2026-11-07T00:45:37+00:00 | Star Wars Battlefront II | 1,183 | 2 |
| 2026-11-07T00:45:37+00:00 | Titanfall 2 | 922 | 3 |
| 2026-11-07T00:45:37+00:00 | Watch Dogs 2 | 811 | 4 |
| 2026-11-07T00:45:37+00:00 | Watch Dogs | 427 | 5 |
| 2026-11-06T20:46:04+00:00 | Rainbow Six Siege | 65,729 | 1 |
| 2026-11-06T20:46:04+00:00 | Star Wars Battlefront II | 1,494 | 2 |
| 2026-11-06T20:46:04+00:00 | Watch Dogs 2 | 1,066 | 3 |
| 2026-11-06T20:46:04+00:00 | Titanfall 2 | 957 | 4 |
| 2026-11-06T20:46:04+00:00 | Watch Dogs | 580 | 5 |
| 2026-11-06T14:52:37+00:00 | Rainbow Six Siege | 47,020 | 1 |
| 2026-11-06T14:52:37+00:00 | Watch Dogs 2 | 2,637 | 2 |
| 2026-11-06T14:52:37+00:00 | Titanfall 2 | 1,529 | 3 |
| 2026-11-06T14:52:37+00:00 | Star Wars Battlefront II | 879 | 4 |
| 2026-11-06T14:52:37+00:00 | Watch Dogs | 731 | 5 |
| 2026-11-06T06:24:38+00:00 | Rainbow Six Siege | 36,391 | 1 |
| 2026-11-06T06:24:38+00:00 | Watch Dogs 2 | 1,074 | 2 |
| 2026-11-06T06:24:38+00:00 | Titanfall 2 | 796 | 3 |
| 2026-11-06T06:24:38+00:00 | Star Wars Battlefront II | 554 | 4 |
| 2026-11-06T06:24:38+00:00 | Watch Dogs | 359 | 5 |
| 2026-11-05T23:58:52+00:00 | Rainbow Six Siege | 55,976 | 1 |
| 2026-11-05T23:58:52+00:00 | Star Wars Battlefront II | 944 | 2 |
| 2026-11-05T23:58:52+00:00 | Watch Dogs 2 | 721 | 3 |
| 2026-11-05T23:58:52+00:00 | Titanfall 2 | 675 | 4 |
| 2026-11-05T23:58:52+00:00 | Watch Dogs | 412 | 5 |

## 4. Oynaklık: hangi oyunun oyuncu sayısı en çok dalgalanıyor? (max-min / ortalama)

| oyun | min | max | ort | dalga_yuzde |
|---|---|---|---|---|
| Watch Dogs 2 | 721 | 8,619 | 2,505 | 315.3 |
| Watch Dogs | 359 | 2,131 | 926 | 191.3 |
| Star Wars Battlefront II | 398 | 2,156 | 1,026 | 171.4 |
| Titanfall 2 | 640 | 2,760 | 1,244 | 170.4 |
| Rainbow Six Siege | 24,741 | 91,821 | 57,678 | 116.3 |

## 5. Hafta içi vs hafta sonu ortalaması

| oyun | hafta_sonu | hafta_ici |
|---|---|---|
| Rainbow Six Siege | 66,714 | 53,633 |
| Star Wars Battlefront II | 1,243 | 929 |
| Titanfall 2 | 1,523 | 1,120 |
| Watch Dogs | 1,090 | 853 |
| Watch Dogs 2 | 2,982 | 2,291 |

## 6. Mağaza verisi: fiyat, indirim, yorum puanı + anlık oyuncu (JOIN)

| oyun | anlik_oyuncu | fiyat | para_birimi | indirim_yuzde | toplam_yorum | olumlu_yuzde | steam_puani |
|---|---|---|---|---|---|---|---|
| Rainbow Six Siege | 64,061 | 0 | FREE | 0 | – | – | – |
| Star Wars Battlefront II | 1,183 | 39.99 | USD | 0 | – | – | – |
| Titanfall 2 | 922 | 29.99 | USD | 0 | – | – | – |
| Watch Dogs 2 | 811 | 39.99 | USD | 0 | – | – | – |
| Watch Dogs | 427 | 15.99 | USD | 0 | – | – | – |

## 7. İndirim etkisi: indirimli günlerde oyuncu sayısı artıyor mu? (JOIN + koşullu AVG)

| oyun | indirimli_gun | normal_gun | max_indirim_yuzde | ort_indirimli | ort_normal | fark_yuzde |
|---|---|---|---|---|---|---|
| Watch Dogs 2 | 4 | 30 | 95 | 5,047 | 2,116 | 138.5 |
| Watch Dogs | 4 | 30 | 90 | 1,603 | 818 | 95.9 |
| Titanfall 2 | 4 | 30 | 85 | 1,741 | 1,156 | 50.5 |
| Star Wars Battlefront II | 4 | 30 | 75 | 913 | 1,033 | -11.6 |
| Rainbow Six Siege | 0 | 34 | 0 | – | 56,895 | – |

## 8. İndirim × oyuncu sayısı korelasyonu (Pearson r, Python)

| oyun | gun_sayisi | pearson_r | yorum |
|---|---|---|---|
| Rainbow Six Siege | 34 | – | hesaplanamadı (indirim hiç değişmedi) |
| Star Wars Battlefront II | 34 | -0.216 | zayıf negatif |
| Titanfall 2 | 34 | +0.575 | orta pozitif |
| Watch Dogs | 34 | +0.635 | güçlü pozitif |
| Watch Dogs 2 | 34 | +0.725 | güçlü pozitif |

> r ≈ +1: indirim arttıkça oyuncu artıyor · r ≈ 0: ilişki yok · r ≈ −1: ters ilişki. Korelasyon nedensellik değildir; birkaç günlük veriyle sonuç güvenilir olmaz.
