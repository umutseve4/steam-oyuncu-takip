# 🔎 SQL Analizi

_Otomatik üretildi: 12.10.2026 07:07 UTC · sorgular: [`queries.sql`](../queries.sql)_

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
| Rainbow Six Siege | 2026-10-12 | 53,725 | -21.7 |
| Rainbow Six Siege | 2026-10-11 | 68,604 | 4.3 |
| Rainbow Six Siege | 2026-10-10 | 65,751 | 13.6 |
| Rainbow Six Siege | 2026-10-09 | 57,891 | 10.8 |
| Rainbow Six Siege | 2026-10-08 | 52,254 | -0.1 |
| Rainbow Six Siege | 2026-10-07 | 52,319 | -1.9 |
| Rainbow Six Siege | 2026-10-06 | 53,345 | -4.7 |
| Rainbow Six Siege | 2026-10-05 | 55,958 | 3.7 |
| Rainbow Six Siege | 2026-10-03 | 53,977 | -21.5 |
| Rainbow Six Siege | 2026-10-02 | 68,763 | – |
| Star Wars Battlefront II | 2026-10-12 | 784 | -35.5 |
| Star Wars Battlefront II | 2026-10-11 | 1,215 | 5.6 |
| Star Wars Battlefront II | 2026-10-10 | 1,151 | 17.7 |
| Star Wars Battlefront II | 2026-10-09 | 978 | 13.9 |
| Star Wars Battlefront II | 2026-10-08 | 859 | -3.6 |
| Star Wars Battlefront II | 2026-10-07 | 891 | 7.2 |
| Star Wars Battlefront II | 2026-10-06 | 831 | -22.5 |
| Star Wars Battlefront II | 2026-10-05 | 1,072 | 16 |
| Star Wars Battlefront II | 2026-10-03 | 924 | -6.7 |
| Star Wars Battlefront II | 2026-10-02 | 990 | – |
| Titanfall 2 | 2026-10-12 | 1,034 | -42.5 |
| Titanfall 2 | 2026-10-11 | 1,798 | 4.8 |
| Titanfall 2 | 2026-10-10 | 1,715 | 8.6 |
| Titanfall 2 | 2026-10-09 | 1,579 | 10.2 |
| Titanfall 2 | 2026-10-08 | 1,433 | -11.5 |
| Titanfall 2 | 2026-10-07 | 1,620 | -9 |
| Titanfall 2 | 2026-10-06 | 1,781 | -16.3 |
| Titanfall 2 | 2026-10-05 | 2,129 | -9.9 |
| Titanfall 2 | 2026-10-03 | 2,363 | 97.2 |
| Titanfall 2 | 2026-10-02 | 1,198 | – |
| Watch Dogs | 2026-10-12 | 936 | -42.6 |
| Watch Dogs | 2026-10-11 | 1,631 | 7.3 |
| Watch Dogs | 2026-10-10 | 1,520 | 5.7 |
| Watch Dogs | 2026-10-09 | 1,438 | 4.5 |
| Watch Dogs | 2026-10-08 | 1,376 | -3.6 |
| Watch Dogs | 2026-10-07 | 1,427 | -8.3 |
| Watch Dogs | 2026-10-06 | 1,556 | -24.2 |
| Watch Dogs | 2026-10-05 | 2,052 | 13.2 |
| Watch Dogs | 2026-10-03 | 1,812 | 31.3 |
| Watch Dogs | 2026-10-02 | 1,380 | – |
| Watch Dogs 2 | 2026-10-12 | 1,983 | -53.5 |
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
| 2026-10-11T08:33:03+00:00 | Rainbow Six Siege | 41,239 | 1 |
| 2026-10-11T08:33:03+00:00 | Watch Dogs 2 | 6,157 | 2 |
| 2026-10-11T08:33:03+00:00 | Titanfall 2 | 2,059 | 3 |
| 2026-10-11T08:33:03+00:00 | Watch Dogs | 1,522 | 4 |
| 2026-10-11T08:33:03+00:00 | Star Wars Battlefront II | 776 | 5 |

## 4. Oynaklık: hangi oyunun oyuncu sayısı en çok dalgalanıyor? (max-min / ortalama)

| oyun | min | max | ort | dalga_yuzde |
|---|---|---|---|---|
| Watch Dogs 2 | 1,691 | 8,619 | 4,374 | 158.4 |
| Star Wars Battlefront II | 439 | 1,623 | 981 | 120.6 |
| Rainbow Six Siege | 26,086 | 91,436 | 58,203 | 112.3 |
| Titanfall 2 | 951 | 2,760 | 1,677 | 107.9 |
| Watch Dogs | 808 | 2,131 | 1,509 | 87.7 |

## 5. Hafta içi vs hafta sonu ortalaması

| oyun | hafta_sonu | hafta_ici |
|---|---|---|
| Rainbow Six Siege | 64,648 | 54,827 |
| Star Wars Battlefront II | 1,133 | 902 |
| Titanfall 2 | 1,863 | 1,580 |
| Watch Dogs | 1,613 | 1,454 |
| Watch Dogs 2 | 4,659 | 4,225 |

## 6. Mağaza verisi: fiyat, indirim, yorum puanı + anlık oyuncu (JOIN)

| oyun | anlik_oyuncu | fiyat | para_birimi | indirim_yuzde | toplam_yorum | olumlu_yuzde | steam_puani |
|---|---|---|---|---|---|---|---|
| Rainbow Six Siege | 34,643 | 0 | FREE | 0 | 1,561,696 | 82.1 | Very Positive |
| Watch Dogs 2 | 2,275 | 39.99 | USD | 0 | 104,918 | 82.1 | Very Positive |
| Titanfall 2 | 951 | 29.99 | USD | 0 | 288,170 | 95.7 | Overwhelmingly Positive |
| Watch Dogs | 808 | 15.99 | USD | 0 | 53,853 | 79.8 | Mostly Positive |
| Star Wars Battlefront II | 474 | 39.99 | USD | 0 | 100,418 | 88.3 | Very Positive |

## 7. İndirim etkisi: indirimli günlerde oyuncu sayısı artıyor mu? (JOIN + koşullu AVG)

| oyun | indirimli_gun | normal_gun | max_indirim_yuzde | ort_indirimli | ort_normal | fark_yuzde |
|---|---|---|---|---|---|---|
| Watch Dogs 2 | 4 | 4 | 95 | 5,047 | 3,553 | 42.1 |
| Watch Dogs | 4 | 4 | 90 | 1,603 | 1,381 | 16 |
| Titanfall 2 | 4 | 4 | 85 | 1,741 | 1,531 | 13.7 |
| Star Wars Battlefront II | 4 | 4 | 75 | 913 | 1,032 | -11.5 |
| Rainbow Six Siege | 0 | 8 | 0 | – | 57,481 | – |

## 8. İndirim × oyuncu sayısı korelasyonu (Pearson r, Python)

| oyun | gun_sayisi | pearson_r | yorum |
|---|---|---|---|
| Rainbow Six Siege | 8 | – | hesaplanamadı (indirim hiç değişmedi) |
| Star Wars Battlefront II | 8 | -0.401 | orta negatif |
| Titanfall 2 | 8 | +0.353 | zayıf pozitif |
| Watch Dogs | 8 | +0.383 | zayıf pozitif |
| Watch Dogs 2 | 8 | +0.571 | orta pozitif |

> r ≈ +1: indirim arttıkça oyuncu artıyor · r ≈ 0: ilişki yok · r ≈ −1: ters ilişki. Korelasyon nedensellik değildir; birkaç günlük veriyle sonuç güvenilir olmaz.
