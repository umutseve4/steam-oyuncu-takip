# 🔎 SQL Analizi

_Otomatik üretildi: 12.11.2026 18:45 UTC · sorgular: [`queries.sql`](../queries.sql)_

## 1. Her oyunun en kalabalık olduğu saat (UTC, ortalamaya göre)

| oyun | zirve_saat_utc | zirve_saat_tr | ort_oyuncu | olcum |
|---|---|---|---|---|
| Rainbow Six Siege | 20:00 | 23:00 | 76,094 | 10 |
| Watch Dogs 2 | 15:00 | 18:00 | 5,075 | 5 |
| Titanfall 2 | 15:00 | 18:00 | 1,972 | 5 |
| Watch Dogs | 15:00 | 18:00 | 1,662 | 5 |
| Star Wars Battlefront II | 19:00 | 22:00 | 1,481 | 5 |

## 2. Günlük ortalama ve günlük değişim (%) — LAG window function

| oyun | gun | gunluk_ort | degisim_yuzde |
|---|---|---|---|
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
| Star Wars Battlefront II | 2026-11-12 | 893 | -5.7 |
| Star Wars Battlefront II | 2026-11-11 | 947 | 12.3 |
| Star Wars Battlefront II | 2026-11-10 | 843 | -10.5 |
| Star Wars Battlefront II | 2026-11-09 | 942 | -27 |
| Star Wars Battlefront II | 2026-11-08 | 1,291 | 0.9 |
| Star Wars Battlefront II | 2026-11-07 | 1,280 | 31.1 |
| Star Wars Battlefront II | 2026-11-06 | 976 | 4.5 |
| Star Wars Battlefront II | 2026-11-05 | 934 | -5.3 |
| Star Wars Battlefront II | 2026-11-04 | 986 | 0.7 |

## 3. Her ölçümde oyunların sıralaması (son 5 ölçüm) — DENSE_RANK

| zaman_utc | oyun | oyuncu | sira |
|---|---|---|---|
| 2026-11-12T18:45:06+00:00 | Rainbow Six Siege | 49,041 | 1 |
| 2026-11-12T18:45:06+00:00 | Star Wars Battlefront II | 1,186 | 2 |
| 2026-11-12T18:45:06+00:00 | Watch Dogs 2 | 1,091 | 3 |
| 2026-11-12T18:45:06+00:00 | Titanfall 2 | 788 | 4 |
| 2026-11-12T18:45:06+00:00 | Watch Dogs | 518 | 5 |
| 2026-11-12T10:47:56+00:00 | Rainbow Six Siege | 25,591 | 1 |
| 2026-11-12T10:47:56+00:00 | Watch Dogs 2 | 1,371 | 2 |
| 2026-11-12T10:47:56+00:00 | Titanfall 2 | 774 | 3 |
| 2026-11-12T10:47:56+00:00 | Star Wars Battlefront II | 473 | 4 |
| 2026-11-12T10:47:56+00:00 | Watch Dogs | 384 | 5 |
| 2026-11-12T02:46:25+00:00 | Rainbow Six Siege | 62,287 | 1 |
| 2026-11-12T02:46:25+00:00 | Star Wars Battlefront II | 1,020 | 2 |
| 2026-11-12T02:46:25+00:00 | Watch Dogs 2 | 871 | 3 |
| 2026-11-12T02:46:25+00:00 | Titanfall 2 | 799 | 4 |
| 2026-11-12T02:46:25+00:00 | Watch Dogs | 369 | 5 |
| 2026-11-11T21:10:00+00:00 | Rainbow Six Siege | 67,582 | 1 |
| 2026-11-11T21:10:00+00:00 | Star Wars Battlefront II | 1,306 | 2 |
| 2026-11-11T21:10:00+00:00 | Watch Dogs 2 | 912 | 3 |
| 2026-11-11T21:10:00+00:00 | Titanfall 2 | 878 | 4 |
| 2026-11-11T21:10:00+00:00 | Watch Dogs | 471 | 5 |
| 2026-11-11T13:52:35+00:00 | Rainbow Six Siege | 38,847 | 1 |
| 2026-11-11T13:52:35+00:00 | Watch Dogs 2 | 2,088 | 2 |
| 2026-11-11T13:52:35+00:00 | Titanfall 2 | 1,227 | 3 |
| 2026-11-11T13:52:35+00:00 | Star Wars Battlefront II | 835 | 4 |
| 2026-11-11T13:52:35+00:00 | Watch Dogs | 618 | 5 |

## 4. Oynaklık: hangi oyunun oyuncu sayısı en çok dalgalanıyor? (max-min / ortalama)

| oyun | min | max | ort | dalga_yuzde |
|---|---|---|---|---|
| Watch Dogs 2 | 702 | 8,619 | 2,362 | 335.2 |
| Watch Dogs | 315 | 2,131 | 877 | 207.2 |
| Titanfall 2 | 628 | 2,760 | 1,214 | 175.6 |
| Star Wars Battlefront II | 398 | 2,156 | 1,029 | 170.8 |
| Rainbow Six Siege | 23,921 | 91,821 | 57,130 | 118.9 |

## 5. Hafta içi vs hafta sonu ortalaması

| oyun | hafta_sonu | hafta_ici |
|---|---|---|
| Rainbow Six Siege | 65,942 | 53,023 |
| Star Wars Battlefront II | 1,251 | 926 |
| Titanfall 2 | 1,488 | 1,087 |
| Watch Dogs | 1,027 | 806 |
| Watch Dogs 2 | 2,802 | 2,157 |

## 6. Mağaza verisi: fiyat, indirim, yorum puanı + anlık oyuncu (JOIN)

| oyun | anlik_oyuncu | fiyat | para_birimi | indirim_yuzde | toplam_yorum | olumlu_yuzde | steam_puani |
|---|---|---|---|---|---|---|---|
| Rainbow Six Siege | 49,041 | 0 | FREE | 0 | – | – | – |
| Star Wars Battlefront II | 1,186 | 39.99 | USD | 0 | – | – | – |
| Watch Dogs 2 | 1,091 | 39.99 | USD | 0 | – | – | – |
| Titanfall 2 | 788 | 29.99 | USD | 0 | – | – | – |
| Watch Dogs | 518 | 15.99 | USD | 0 | – | – | – |

## 7. İndirim etkisi: indirimli günlerde oyuncu sayısı artıyor mu? (JOIN + koşullu AVG)

| oyun | indirimli_gun | normal_gun | max_indirim_yuzde | ort_indirimli | ort_normal | fark_yuzde |
|---|---|---|---|---|---|---|
| Watch Dogs 2 | 4 | 35 | 95 | 5,047 | 2,009 | 151.3 |
| Watch Dogs | 4 | 35 | 90 | 1,603 | 775 | 106.9 |
| Titanfall 2 | 4 | 35 | 85 | 1,741 | 1,130 | 54.1 |
| Star Wars Battlefront II | 4 | 35 | 75 | 913 | 1,029 | -11.2 |
| Rainbow Six Siege | 0 | 39 | 0 | – | 56,057 | – |

## 8. İndirim × oyuncu sayısı korelasyonu (Pearson r, Python)

| oyun | gun_sayisi | pearson_r | yorum |
|---|---|---|---|
| Rainbow Six Siege | 39 | – | hesaplanamadı (indirim hiç değişmedi) |
| Star Wars Battlefront II | 39 | -0.195 | çok zayıf negatif |
| Titanfall 2 | 39 | +0.565 | orta pozitif |
| Watch Dogs | 39 | +0.634 | güçlü pozitif |
| Watch Dogs 2 | 39 | +0.724 | güçlü pozitif |

> r ≈ +1: indirim arttıkça oyuncu artıyor · r ≈ 0: ilişki yok · r ≈ −1: ters ilişki. Korelasyon nedensellik değildir; birkaç günlük veriyle sonuç güvenilir olmaz.
