# 🔎 SQL Analizi

_Otomatik üretildi: 06.11.2026 20:46 UTC · sorgular: [`queries.sql`](../queries.sql)_

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
| Star Wars Battlefront II | 2026-10-24 | 1,425 | 25.3 |
| Star Wars Battlefront II | 2026-10-23 | 1,137 | 21.9 |

## 3. Her ölçümde oyunların sıralaması (son 5 ölçüm) — DENSE_RANK

| zaman_utc | oyun | oyuncu | sira |
|---|---|---|---|
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
| 2026-11-05T18:36:24+00:00 | Rainbow Six Siege | 52,259 | 1 |
| 2026-11-05T18:36:24+00:00 | Star Wars Battlefront II | 1,205 | 2 |
| 2026-11-05T18:36:24+00:00 | Watch Dogs 2 | 1,153 | 3 |
| 2026-11-05T18:36:24+00:00 | Titanfall 2 | 860 | 4 |
| 2026-11-05T18:36:24+00:00 | Watch Dogs | 546 | 5 |

## 4. Oynaklık: hangi oyunun oyuncu sayısı en çok dalgalanıyor? (max-min / ortalama)

| oyun | min | max | ort | dalga_yuzde |
|---|---|---|---|---|
| Watch Dogs 2 | 721 | 8,619 | 2,516 | 313.9 |
| Watch Dogs | 359 | 2,131 | 929 | 190.6 |
| Star Wars Battlefront II | 398 | 2,156 | 1,025 | 171.5 |
| Titanfall 2 | 640 | 2,760 | 1,247 | 170.1 |
| Rainbow Six Siege | 24,741 | 91,821 | 57,636 | 116.4 |

## 5. Hafta içi vs hafta sonu ortalaması

| oyun | hafta_sonu | hafta_ici |
|---|---|---|
| Rainbow Six Siege | 66,771 | 53,633 |
| Star Wars Battlefront II | 1,244 | 929 |
| Titanfall 2 | 1,536 | 1,120 |
| Watch Dogs | 1,104 | 853 |
| Watch Dogs 2 | 3,029 | 2,291 |

## 6. Mağaza verisi: fiyat, indirim, yorum puanı + anlık oyuncu (JOIN)

| oyun | anlik_oyuncu | fiyat | para_birimi | indirim_yuzde | toplam_yorum | olumlu_yuzde | steam_puani |
|---|---|---|---|---|---|---|---|
| Rainbow Six Siege | 65,729 | 0 | FREE | 0 | – | – | – |
| Star Wars Battlefront II | 1,494 | 39.99 | USD | 0 | – | – | – |
| Watch Dogs 2 | 1,066 | 39.99 | USD | 0 | – | – | – |
| Titanfall 2 | 957 | 29.99 | USD | 0 | – | – | – |
| Watch Dogs | 580 | 15.99 | USD | 0 | – | – | – |

## 7. İndirim etkisi: indirimli günlerde oyuncu sayısı artıyor mu? (JOIN + koşullu AVG)

| oyun | indirimli_gun | normal_gun | max_indirim_yuzde | ort_indirimli | ort_normal | fark_yuzde |
|---|---|---|---|---|---|---|
| Watch Dogs 2 | 4 | 29 | 95 | 5,047 | 2,161 | 133.5 |
| Watch Dogs | 4 | 29 | 90 | 1,603 | 832 | 92.7 |
| Titanfall 2 | 4 | 29 | 85 | 1,741 | 1,165 | 49.5 |
| Star Wars Battlefront II | 4 | 29 | 75 | 913 | 1,028 | -11.2 |
| Rainbow Six Siege | 0 | 33 | 0 | – | 56,678 | – |

## 8. İndirim × oyuncu sayısı korelasyonu (Pearson r, Python)

| oyun | gun_sayisi | pearson_r | yorum |
|---|---|---|---|
| Rainbow Six Siege | 33 | – | hesaplanamadı (indirim hiç değişmedi) |
| Star Wars Battlefront II | 33 | -0.209 | zayıf negatif |
| Titanfall 2 | 33 | +0.574 | orta pozitif |
| Watch Dogs | 33 | +0.638 | güçlü pozitif |
| Watch Dogs 2 | 33 | +0.731 | güçlü pozitif |

> r ≈ +1: indirim arttıkça oyuncu artıyor · r ≈ 0: ilişki yok · r ≈ −1: ters ilişki. Korelasyon nedensellik değildir; birkaç günlük veriyle sonuç güvenilir olmaz.
