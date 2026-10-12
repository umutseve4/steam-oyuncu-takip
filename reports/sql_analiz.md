# 🔎 SQL Analizi

_Otomatik üretildi: 12.10.2026 17:36 UTC · sorgular: [`queries.sql`](../queries.sql)_

## 1. Her oyunun en kalabalık olduğu saat (UTC, ortalamaya göre)

| oyun | zirve_saat_utc | zirve_saat_tr | ort_oyuncu | olcum |
|---|---|---|---|---|
| Rainbow Six Siege | 22:00 | 01:00 | 79,447 | 1 |
| Watch Dogs 2 | 14:00 | 17:00 | 8,384 | 2 |
| Titanfall 2 | 13:00 | 16:00 | 2,760 | 1 |
| Watch Dogs | 13:00 | 16:00 | 2,093 | 1 |
| Star Wars Battlefront II | 18:00 | 21:00 | 1,465 | 2 |

## 2. Günlük ortalama ve günlük değişim (%) — LAG window function

| oyun | gun | gunluk_ort | degisim_yuzde |
|---|---|---|---|
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
| Star Wars Battlefront II | 2026-10-12 | 961 | -20.9 |
| Star Wars Battlefront II | 2026-10-11 | 1,215 | 5.6 |
| Star Wars Battlefront II | 2026-10-10 | 1,151 | 17.7 |
| Star Wars Battlefront II | 2026-10-09 | 978 | 13.9 |
| Star Wars Battlefront II | 2026-10-08 | 859 | -3.6 |
| Star Wars Battlefront II | 2026-10-07 | 891 | 7.2 |
| Star Wars Battlefront II | 2026-10-06 | 831 | -22.5 |
| Star Wars Battlefront II | 2026-10-05 | 1,072 | 16 |
| Star Wars Battlefront II | 2026-10-03 | 924 | -6.7 |
| Star Wars Battlefront II | 2026-10-02 | 990 | – |
| Titanfall 2 | 2026-10-12 | 1,138 | -36.7 |
| Titanfall 2 | 2026-10-11 | 1,798 | 4.8 |
| Titanfall 2 | 2026-10-10 | 1,715 | 8.6 |
| Titanfall 2 | 2026-10-09 | 1,579 | 10.2 |
| Titanfall 2 | 2026-10-08 | 1,433 | -11.5 |
| Titanfall 2 | 2026-10-07 | 1,620 | -9 |
| Titanfall 2 | 2026-10-06 | 1,781 | -16.3 |
| Titanfall 2 | 2026-10-05 | 2,129 | -9.9 |
| Titanfall 2 | 2026-10-03 | 2,363 | 97.2 |
| Titanfall 2 | 2026-10-02 | 1,198 | – |
| Watch Dogs | 2026-10-12 | 1,159 | -28.9 |
| Watch Dogs | 2026-10-11 | 1,631 | 7.3 |
| Watch Dogs | 2026-10-10 | 1,520 | 5.7 |
| Watch Dogs | 2026-10-09 | 1,438 | 4.5 |
| Watch Dogs | 2026-10-08 | 1,376 | -3.6 |
| Watch Dogs | 2026-10-07 | 1,427 | -8.3 |
| Watch Dogs | 2026-10-06 | 1,556 | -24.2 |
| Watch Dogs | 2026-10-05 | 2,052 | 13.2 |
| Watch Dogs | 2026-10-03 | 1,812 | 31.3 |
| Watch Dogs | 2026-10-02 | 1,380 | – |
| Watch Dogs 2 | 2026-10-12 | 2,450 | -42.5 |
| Watch Dogs 2 | 2026-10-11 | 4,262 | 3.8 |
| Watch Dogs 2 | 2026-10-10 | 4,104 | 6.3 |
| Watch Dogs 2 | 2026-10-09 | 3,862 | 2.5 |
| Watch Dogs 2 | 2026-10-08 | 3,769 | -14 |
| Watch Dogs 2 | 2026-10-07 | 4,385 | -13.1 |
| Watch Dogs 2 | 2026-10-06 | 5,045 | -27.8 |
| Watch Dogs 2 | 2026-10-05 | 6,991 | 2.2 |
| Watch Dogs 2 | 2026-10-03 | 6,841 | 170.3 |
| Watch Dogs 2 | 2026-10-02 | 2,531 | – |

## 3. Her ölçümde oyunların sıralaması (son 5 ölçüm) — DENSE_RANK

| zaman_utc | oyun | oyuncu | sira |
|---|---|---|---|
| 2026-10-12T17:36:55+00:00 | Rainbow Six Siege | 70,284 | 1 |
| 2026-10-12T17:36:55+00:00 | Watch Dogs 2 | 3,384 | 2 |
| 2026-10-12T17:36:55+00:00 | Watch Dogs | 1,606 | 3 |
| 2026-10-12T17:36:55+00:00 | Titanfall 2 | 1,345 | 4 |
| 2026-10-12T17:36:55+00:00 | Star Wars Battlefront II | 1,316 | 5 |
| 2026-10-12T07:07:56+00:00 | Rainbow Six Siege | 34,643 | 1 |
| 2026-10-12T07:07:56+00:00 | Watch Dogs 2 | 2,275 | 2 |
| 2026-10-12T07:07:56+00:00 | Titanfall 2 | 951 | 3 |
| 2026-10-12T07:07:56+00:00 | Watch Dogs | 808 | 4 |
| 2026-10-12T07:07:56+00:00 | Star Wars Battlefront II | 474 | 5 |
| 2026-10-12T00:21:00+00:00 | Rainbow Six Siege | 72,806 | 1 |
| 2026-10-12T00:21:00+00:00 | Watch Dogs 2 | 1,691 | 2 |
| 2026-10-12T00:21:00+00:00 | Titanfall 2 | 1,117 | 3 |
| 2026-10-12T00:21:00+00:00 | Star Wars Battlefront II | 1,094 | 4 |
| 2026-10-12T00:21:00+00:00 | Watch Dogs | 1,064 | 5 |
| 2026-10-11T20:04:40+00:00 | Rainbow Six Siege | 91,436 | 1 |
| 2026-10-11T20:04:40+00:00 | Watch Dogs 2 | 2,783 | 2 |
| 2026-10-11T20:04:40+00:00 | Watch Dogs | 1,644 | 3 |
| 2026-10-11T20:04:40+00:00 | Star Wars Battlefront II | 1,572 | 4 |
| 2026-10-11T20:04:40+00:00 | Titanfall 2 | 1,511 | 5 |
| 2026-10-11T15:29:03+00:00 | Rainbow Six Siege | 71,104 | 1 |
| 2026-10-11T15:29:03+00:00 | Watch Dogs 2 | 5,523 | 2 |
| 2026-10-11T15:29:03+00:00 | Titanfall 2 | 2,185 | 3 |
| 2026-10-11T15:29:03+00:00 | Watch Dogs | 2,131 | 4 |
| 2026-10-11T15:29:03+00:00 | Star Wars Battlefront II | 1,408 | 5 |

## 4. Oynaklık: hangi oyunun oyuncu sayısı en çok dalgalanıyor? (max-min / ortalama)

| oyun | min | max | ort | dalga_yuzde |
|---|---|---|---|---|
| Watch Dogs 2 | 1,691 | 8,619 | 4,344 | 159.5 |
| Star Wars Battlefront II | 439 | 1,623 | 992 | 119.4 |
| Rainbow Six Siege | 26,086 | 91,436 | 58,569 | 111.6 |
| Titanfall 2 | 951 | 2,760 | 1,667 | 108.5 |
| Watch Dogs | 808 | 2,131 | 1,512 | 87.5 |

## 5. Hafta içi vs hafta sonu ortalaması

| oyun | hafta_sonu | hafta_ici |
|---|---|---|
| Rainbow Six Siege | 64,648 | 55,529 |
| Star Wars Battlefront II | 1,133 | 921 |
| Titanfall 2 | 1,863 | 1,569 |
| Watch Dogs | 1,613 | 1,461 |
| Watch Dogs 2 | 4,659 | 4,187 |

## 6. Mağaza verisi: fiyat, indirim, yorum puanı + anlık oyuncu (JOIN)

| oyun | anlik_oyuncu | fiyat | para_birimi | indirim_yuzde | toplam_yorum | olumlu_yuzde | steam_puani |
|---|---|---|---|---|---|---|---|
| Rainbow Six Siege | 70,284 | 0 | FREE | 0 | 1,561,696 | 82.1 | Very Positive |
| Watch Dogs 2 | 3,384 | 39.99 | USD | 0 | 104,918 | 82.1 | Very Positive |
| Watch Dogs | 1,606 | 15.99 | USD | 0 | 53,853 | 79.8 | Mostly Positive |
| Titanfall 2 | 1,345 | 29.99 | USD | 0 | 288,170 | 95.7 | Overwhelmingly Positive |
| Star Wars Battlefront II | 1,316 | 39.99 | USD | 0 | 100,418 | 88.3 | Very Positive |

## 7. İndirim etkisi: indirimli günlerde oyuncu sayısı artıyor mu? (JOIN + koşullu AVG)

| oyun | indirimli_gun | normal_gun | max_indirim_yuzde | ort_indirimli | ort_normal | fark_yuzde |
|---|---|---|---|---|---|---|
| Watch Dogs 2 | 4 | 4 | 95 | 5,047 | 3,670 | 37.5 |
| Titanfall 2 | 4 | 4 | 85 | 1,741 | 1,557 | 11.8 |
| Watch Dogs | 4 | 4 | 90 | 1,603 | 1,437 | 11.5 |
| Star Wars Battlefront II | 4 | 4 | 75 | 913 | 1,076 | -15.2 |
| Rainbow Six Siege | 0 | 8 | 0 | – | 58,171 | – |

## 8. İndirim × oyuncu sayısı korelasyonu (Pearson r, Python)

| oyun | gun_sayisi | pearson_r | yorum |
|---|---|---|---|
| Rainbow Six Siege | 8 | – | hesaplanamadı (indirim hiç değişmedi) |
| Star Wars Battlefront II | 8 | -0.625 | güçlü negatif |
| Titanfall 2 | 8 | +0.338 | zayıf pozitif |
| Watch Dogs | 8 | +0.344 | zayıf pozitif |
| Watch Dogs 2 | 8 | +0.569 | orta pozitif |

> r ≈ +1: indirim arttıkça oyuncu artıyor · r ≈ 0: ilişki yok · r ≈ −1: ters ilişki. Korelasyon nedensellik değildir; birkaç günlük veriyle sonuç güvenilir olmaz.
