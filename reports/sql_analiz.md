# 🔎 SQL Analizi

_Otomatik üretildi: 14.10.2026 22:08 UTC · sorgular: [`queries.sql`](../queries.sql)_

## 1. Her oyunun en kalabalık olduğu saat (UTC, ortalamaya göre)

| oyun | zirve_saat_utc | zirve_saat_tr | ort_oyuncu | olcum |
|---|---|---|---|---|
| Rainbow Six Siege | 20:00 | 23:00 | 78,793 | 3 |
| Watch Dogs 2 | 14:00 | 17:00 | 8,384 | 2 |
| Titanfall 2 | 14:00 | 17:00 | 2,552 | 2 |
| Watch Dogs | 14:00 | 17:00 | 2,072 | 2 |
| Star Wars Battlefront II | 18:00 | 21:00 | 1,363 | 3 |

## 2. Günlük ortalama ve günlük değişim (%) — LAG window function

| oyun | gun | gunluk_ort | degisim_yuzde |
|---|---|---|---|
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
| Star Wars Battlefront II | 2026-10-14 | 812 | 1.8 |
| Star Wars Battlefront II | 2026-10-13 | 798 | -17 |
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
| Titanfall 2 | 2026-10-14 | 1,076 | -1.2 |
| Titanfall 2 | 2026-10-13 | 1,089 | -4.3 |
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
| Watch Dogs | 2026-10-14 | 951 | -4.5 |
| Watch Dogs | 2026-10-13 | 996 | -14.1 |
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
| Watch Dogs 2 | 2026-10-14 | 2,354 | -0.9 |
| Watch Dogs 2 | 2026-10-13 | 2,375 | -3.1 |

## 3. Her ölçümde oyunların sıralaması (son 5 ölçüm) — DENSE_RANK

| zaman_utc | oyun | oyuncu | sira |
|---|---|---|---|
| 2026-10-14T22:08:27+00:00 | Rainbow Six Siege | 61,736 | 1 |
| 2026-10-14T22:08:27+00:00 | Watch Dogs 2 | 1,439 | 2 |
| 2026-10-14T22:08:27+00:00 | Titanfall 2 | 876 | 3 |
| 2026-10-14T22:08:27+00:00 | Star Wars Battlefront II | 863 | 4 |
| 2026-10-14T22:08:27+00:00 | Watch Dogs | 854 | 5 |
| 2026-10-14T18:24:44+00:00 | Rainbow Six Siege | 61,144 | 1 |
| 2026-10-14T18:24:44+00:00 | Watch Dogs 2 | 2,306 | 2 |
| 2026-10-14T18:24:44+00:00 | Watch Dogs | 1,211 | 3 |
| 2026-10-14T18:24:44+00:00 | Star Wars Battlefront II | 1,160 | 4 |
| 2026-10-14T18:24:44+00:00 | Titanfall 2 | 1,092 | 5 |
| 2026-10-14T13:28:50+00:00 | Rainbow Six Siege | 41,546 | 1 |
| 2026-10-14T13:28:50+00:00 | Watch Dogs 2 | 4,487 | 2 |
| 2026-10-14T13:28:50+00:00 | Titanfall 2 | 1,655 | 3 |
| 2026-10-14T13:28:50+00:00 | Watch Dogs | 1,282 | 4 |
| 2026-10-14T13:28:50+00:00 | Star Wars Battlefront II | 782 | 5 |
| 2026-10-14T07:19:30+00:00 | Rainbow Six Siege | 29,348 | 1 |
| 2026-10-14T07:19:30+00:00 | Watch Dogs 2 | 2,157 | 2 |
| 2026-10-14T07:19:30+00:00 | Titanfall 2 | 851 | 3 |
| 2026-10-14T07:19:30+00:00 | Watch Dogs | 652 | 4 |
| 2026-10-14T07:19:30+00:00 | Star Wars Battlefront II | 424 | 5 |
| 2026-10-14T01:00:35+00:00 | Rainbow Six Siege | 68,640 | 1 |
| 2026-10-14T01:00:35+00:00 | Watch Dogs 2 | 1,383 | 2 |
| 2026-10-14T01:00:35+00:00 | Titanfall 2 | 907 | 3 |
| 2026-10-14T01:00:35+00:00 | Star Wars Battlefront II | 830 | 4 |
| 2026-10-14T01:00:35+00:00 | Watch Dogs | 757 | 5 |

## 4. Oynaklık: hangi oyunun oyuncu sayısı en çok dalgalanıyor? (max-min / ortalama)

| oyun | min | max | ort | dalga_yuzde |
|---|---|---|---|---|
| Watch Dogs 2 | 1,383 | 8,619 | 3,920 | 184.6 |
| Star Wars Battlefront II | 402 | 1,623 | 952 | 128.3 |
| Titanfall 2 | 851 | 2,760 | 1,542 | 123.8 |
| Rainbow Six Siege | 26,086 | 91,436 | 57,336 | 114 |
| Watch Dogs | 652 | 2,131 | 1,396 | 106 |

## 5. Hafta içi vs hafta sonu ortalaması

| oyun | hafta_sonu | hafta_ici |
|---|---|---|
| Rainbow Six Siege | 64,648 | 54,742 |
| Star Wars Battlefront II | 1,133 | 887 |
| Titanfall 2 | 1,863 | 1,428 |
| Watch Dogs | 1,613 | 1,319 |
| Watch Dogs 2 | 4,659 | 3,657 |

## 6. Mağaza verisi: fiyat, indirim, yorum puanı + anlık oyuncu (JOIN)

| oyun | anlik_oyuncu | fiyat | para_birimi | indirim_yuzde | toplam_yorum | olumlu_yuzde | steam_puani |
|---|---|---|---|---|---|---|---|
| Rainbow Six Siege | 61,736 | 0 | FREE | 0 | 1,562,242 | 82.1 | Very Positive |
| Watch Dogs 2 | 1,439 | 39.99 | USD | 0 | 105,049 | 82.1 | Very Positive |
| Titanfall 2 | 876 | 29.99 | USD | 0 | 288,272 | 95.7 | Overwhelmingly Positive |
| Star Wars Battlefront II | 863 | 39.99 | USD | 0 | 100,441 | 88.3 | Very Positive |
| Watch Dogs | 854 | 15.99 | USD | 0 | 53,927 | 79.8 | Mostly Positive |

## 7. İndirim etkisi: indirimli günlerde oyuncu sayısı artıyor mu? (JOIN + koşullu AVG)

| oyun | indirimli_gun | normal_gun | max_indirim_yuzde | ort_indirimli | ort_normal | fark_yuzde |
|---|---|---|---|---|---|---|
| Watch Dogs 2 | 4 | 6 | 95 | 5,047 | 3,235 | 56 |
| Watch Dogs | 4 | 6 | 90 | 1,603 | 1,282 | 25 |
| Titanfall 2 | 4 | 6 | 85 | 1,741 | 1,399 | 24.4 |
| Star Wars Battlefront II | 4 | 6 | 75 | 913 | 986 | -7.4 |
| Rainbow Six Siege | 0 | 10 | 0 | – | 57,108 | – |

## 8. İndirim × oyuncu sayısı korelasyonu (Pearson r, Python)

| oyun | gun_sayisi | pearson_r | yorum |
|---|---|---|---|
| Rainbow Six Siege | 10 | – | hesaplanamadı (indirim hiç değişmedi) |
| Star Wars Battlefront II | 10 | -0.255 | zayıf negatif |
| Titanfall 2 | 10 | +0.504 | orta pozitif |
| Watch Dogs | 10 | +0.511 | orta pozitif |
| Watch Dogs 2 | 10 | +0.661 | güçlü pozitif |

> r ≈ +1: indirim arttıkça oyuncu artıyor · r ≈ 0: ilişki yok · r ≈ −1: ters ilişki. Korelasyon nedensellik değildir; birkaç günlük veriyle sonuç güvenilir olmaz.
