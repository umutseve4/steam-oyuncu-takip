# 🔎 SQL Analizi

_Otomatik üretildi: 08.11.2026 21:00 UTC · sorgular: [`queries.sql`](../queries.sql)_

## 1. Her oyunun en kalabalık olduğu saat (UTC, ortalamaya göre)

| oyun | zirve_saat_utc | zirve_saat_tr | ort_oyuncu | olcum |
|---|---|---|---|---|
| Rainbow Six Siege | 20:00 | 23:00 | 76,094 | 10 |
| Watch Dogs 2 | 15:00 | 18:00 | 5,075 | 5 |
| Titanfall 2 | 13:00 | 16:00 | 1,985 | 4 |
| Watch Dogs | 15:00 | 18:00 | 1,662 | 5 |
| Star Wars Battlefront II | 18:00 | 21:00 | 1,484 | 13 |

## 2. Günlük ortalama ve günlük değişim (%) — LAG window function

| oyun | gun | gunluk_ort | degisim_yuzde |
|---|---|---|---|
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
| Star Wars Battlefront II | 2026-11-08 | 1,291 | 0.9 |
| Star Wars Battlefront II | 2026-11-07 | 1,280 | 31.1 |
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

## 3. Her ölçümde oyunların sıralaması (son 5 ölçüm) — DENSE_RANK

| zaman_utc | oyun | oyuncu | sira |
|---|---|---|---|
| 2026-11-08T21:00:04+00:00 | Rainbow Six Siege | 80,011 | 1 |
| 2026-11-08T21:00:04+00:00 | Star Wars Battlefront II | 1,696 | 2 |
| 2026-11-08T21:00:04+00:00 | Watch Dogs 2 | 1,113 | 3 |
| 2026-11-08T21:00:04+00:00 | Titanfall 2 | 1,074 | 4 |
| 2026-11-08T21:00:04+00:00 | Watch Dogs | 641 | 5 |
| 2026-11-08T16:38:08+00:00 | Rainbow Six Siege | 61,368 | 1 |
| 2026-11-08T16:38:08+00:00 | Watch Dogs 2 | 1,746 | 2 |
| 2026-11-08T16:38:08+00:00 | Star Wars Battlefront II | 1,506 | 3 |
| 2026-11-08T16:38:08+00:00 | Titanfall 2 | 1,181 | 4 |
| 2026-11-08T16:38:08+00:00 | Watch Dogs | 771 | 5 |
| 2026-11-08T10:00:03+00:00 | Rainbow Six Siege | 36,262 | 1 |
| 2026-11-08T10:00:03+00:00 | Watch Dogs 2 | 2,151 | 2 |
| 2026-11-08T10:00:03+00:00 | Titanfall 2 | 1,334 | 3 |
| 2026-11-08T10:00:03+00:00 | Star Wars Battlefront II | 780 | 4 |
| 2026-11-08T10:00:03+00:00 | Watch Dogs | 631 | 5 |
| 2026-11-08T02:10:32+00:00 | Rainbow Six Siege | 66,798 | 1 |
| 2026-11-08T02:10:32+00:00 | Star Wars Battlefront II | 1,182 | 2 |
| 2026-11-08T02:10:32+00:00 | Titanfall 2 | 1,181 | 3 |
| 2026-11-08T02:10:32+00:00 | Watch Dogs 2 | 1,134 | 4 |
| 2026-11-08T02:10:32+00:00 | Watch Dogs | 479 | 5 |
| 2026-11-07T22:35:10+00:00 | Rainbow Six Siege | 75,913 | 1 |
| 2026-11-07T22:35:10+00:00 | Star Wars Battlefront II | 1,660 | 2 |
| 2026-11-07T22:35:10+00:00 | Watch Dogs 2 | 1,092 | 3 |
| 2026-11-07T22:35:10+00:00 | Titanfall 2 | 1,075 | 4 |
| 2026-11-07T22:35:10+00:00 | Watch Dogs | 596 | 5 |

## 4. Oynaklık: hangi oyunun oyuncu sayısı en çok dalgalanıyor? (max-min / ortalama)

| oyun | min | max | ort | dalga_yuzde |
|---|---|---|---|---|
| Watch Dogs 2 | 721 | 8,619 | 2,467 | 320.2 |
| Watch Dogs | 359 | 2,131 | 913 | 194.1 |
| Titanfall 2 | 640 | 2,760 | 1,246 | 170.1 |
| Star Wars Battlefront II | 398 | 2,156 | 1,039 | 169.1 |
| Rainbow Six Siege | 24,741 | 91,821 | 57,864 | 115.9 |

## 5. Hafta içi vs hafta sonu ortalaması

| oyun | hafta_sonu | hafta_ici |
|---|---|---|
| Rainbow Six Siege | 65,942 | 53,633 |
| Star Wars Battlefront II | 1,251 | 929 |
| Titanfall 2 | 1,488 | 1,120 |
| Watch Dogs | 1,027 | 853 |
| Watch Dogs 2 | 2,802 | 2,291 |

## 6. Mağaza verisi: fiyat, indirim, yorum puanı + anlık oyuncu (JOIN)

| oyun | anlik_oyuncu | fiyat | para_birimi | indirim_yuzde | toplam_yorum | olumlu_yuzde | steam_puani |
|---|---|---|---|---|---|---|---|
| Rainbow Six Siege | 80,011 | 0 | FREE | 0 | – | – | – |
| Star Wars Battlefront II | 1,696 | 39.99 | USD | 0 | – | – | – |
| Watch Dogs 2 | 1,113 | 39.99 | USD | 0 | – | – | – |
| Titanfall 2 | 1,074 | 29.99 | USD | 0 | – | – | – |
| Watch Dogs | 641 | 15.99 | USD | 0 | – | – | – |

## 7. İndirim etkisi: indirimli günlerde oyuncu sayısı artıyor mu? (JOIN + koşullu AVG)

| oyun | indirimli_gun | normal_gun | max_indirim_yuzde | ort_indirimli | ort_normal | fark_yuzde |
|---|---|---|---|---|---|---|
| Watch Dogs 2 | 4 | 31 | 95 | 5,047 | 2,127 | 137.3 |
| Watch Dogs | 4 | 31 | 90 | 1,603 | 819 | 95.7 |
| Titanfall 2 | 4 | 31 | 85 | 1,741 | 1,169 | 48.9 |
| Star Wars Battlefront II | 4 | 31 | 75 | 913 | 1,045 | -12.6 |
| Rainbow Six Siege | 0 | 35 | 0 | – | 56,961 | – |

## 8. İndirim × oyuncu sayısı korelasyonu (Pearson r, Python)

| oyun | gun_sayisi | pearson_r | yorum |
|---|---|---|---|
| Rainbow Six Siege | 35 | – | hesaplanamadı (indirim hiç değişmedi) |
| Star Wars Battlefront II | 35 | -0.226 | zayıf negatif |
| Titanfall 2 | 35 | +0.571 | orta pozitif |
| Watch Dogs | 35 | +0.641 | güçlü pozitif |
| Watch Dogs 2 | 35 | +0.732 | güçlü pozitif |

> r ≈ +1: indirim arttıkça oyuncu artıyor · r ≈ 0: ilişki yok · r ≈ −1: ters ilişki. Korelasyon nedensellik değildir; birkaç günlük veriyle sonuç güvenilir olmaz.
