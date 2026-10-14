# 🔎 SQL Analizi

_Otomatik üretildi: 14.10.2026 07:19 UTC · sorgular: [`queries.sql`](../queries.sql)_

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
| Rainbow Six Siege | 2026-10-14 | 48,994 | -8 |
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
| Star Wars Battlefront II | 2026-10-14 | 627 | -21.4 |
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
| Titanfall 2 | 2026-10-14 | 879 | -19.3 |
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
| Watch Dogs | 2026-10-14 | 705 | -29.2 |
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
| Watch Dogs 2 | 2026-10-14 | 1,770 | -25.5 |
| Watch Dogs 2 | 2026-10-13 | 2,375 | -3.1 |

## 3. Her ölçümde oyunların sıralaması (son 5 ölçüm) — DENSE_RANK

| zaman_utc | oyun | oyuncu | sira |
|---|---|---|---|
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
| 2026-10-13T21:05:49+00:00 | Rainbow Six Siege | 64,532 | 1 |
| 2026-10-13T21:05:49+00:00 | Watch Dogs 2 | 1,737 | 2 |
| 2026-10-13T21:05:49+00:00 | Watch Dogs | 1,004 | 3 |
| 2026-10-13T21:05:49+00:00 | Star Wars Battlefront II | 984 | 4 |
| 2026-10-13T21:05:49+00:00 | Titanfall 2 | 966 | 5 |
| 2026-10-13T15:45:43+00:00 | Rainbow Six Siege | 50,165 | 1 |
| 2026-10-13T15:45:43+00:00 | Watch Dogs 2 | 3,858 | 2 |
| 2026-10-13T15:45:43+00:00 | Titanfall 2 | 1,435 | 3 |
| 2026-10-13T15:45:43+00:00 | Watch Dogs | 1,324 | 4 |
| 2026-10-13T15:45:43+00:00 | Star Wars Battlefront II | 885 | 5 |
| 2026-10-13T07:32:21+00:00 | Rainbow Six Siege | 28,645 | 1 |
| 2026-10-13T07:32:21+00:00 | Watch Dogs 2 | 2,304 | 2 |
| 2026-10-13T07:32:21+00:00 | Titanfall 2 | 918 | 3 |
| 2026-10-13T07:32:21+00:00 | Watch Dogs | 695 | 4 |
| 2026-10-13T07:32:21+00:00 | Star Wars Battlefront II | 402 | 5 |

## 4. Oynaklık: hangi oyunun oyuncu sayısı en çok dalgalanıyor? (max-min / ortalama)

| oyun | min | max | ort | dalga_yuzde |
|---|---|---|---|---|
| Watch Dogs 2 | 1,383 | 8,619 | 4,010 | 180.4 |
| Star Wars Battlefront II | 402 | 1,623 | 953 | 128.1 |
| Titanfall 2 | 851 | 2,760 | 1,567 | 121.8 |
| Rainbow Six Siege | 26,086 | 91,436 | 57,531 | 113.6 |
| Watch Dogs | 652 | 2,131 | 1,417 | 104.3 |

## 5. Hafta içi vs hafta sonu ortalaması

| oyun | hafta_sonu | hafta_ici |
|---|---|---|
| Rainbow Six Siege | 64,648 | 54,735 |
| Star Wars Battlefront II | 1,133 | 882 |
| Titanfall 2 | 1,863 | 1,451 |
| Watch Dogs | 1,613 | 1,341 |
| Watch Dogs 2 | 4,659 | 3,755 |

## 6. Mağaza verisi: fiyat, indirim, yorum puanı + anlık oyuncu (JOIN)

| oyun | anlik_oyuncu | fiyat | para_birimi | indirim_yuzde | toplam_yorum | olumlu_yuzde | steam_puani |
|---|---|---|---|---|---|---|---|
| Rainbow Six Siege | 29,348 | 0 | FREE | 0 | 1,562,242 | 82.1 | Very Positive |
| Watch Dogs 2 | 2,157 | 39.99 | USD | 0 | 105,049 | 82.1 | Very Positive |
| Titanfall 2 | 851 | 29.99 | USD | 0 | 288,272 | 95.7 | Overwhelmingly Positive |
| Watch Dogs | 652 | 15.99 | USD | 0 | 53,927 | 79.8 | Mostly Positive |
| Star Wars Battlefront II | 424 | 39.99 | USD | 0 | 100,441 | 88.3 | Very Positive |

## 7. İndirim etkisi: indirimli günlerde oyuncu sayısı artıyor mu? (JOIN + koşullu AVG)

| oyun | indirimli_gun | normal_gun | max_indirim_yuzde | ort_indirimli | ort_normal | fark_yuzde |
|---|---|---|---|---|---|---|
| Watch Dogs 2 | 4 | 6 | 95 | 5,047 | 3,137 | 60.9 |
| Watch Dogs | 4 | 6 | 90 | 1,603 | 1,241 | 29.1 |
| Titanfall 2 | 4 | 6 | 85 | 1,741 | 1,366 | 27.4 |
| Star Wars Battlefront II | 4 | 6 | 75 | 913 | 955 | -4.4 |
| Rainbow Six Siege | 0 | 10 | 0 | – | 56,759 | – |

## 8. İndirim × oyuncu sayısı korelasyonu (Pearson r, Python)

| oyun | gun_sayisi | pearson_r | yorum |
|---|---|---|---|
| Rainbow Six Siege | 10 | – | hesaplanamadı (indirim hiç değişmedi) |
| Star Wars Battlefront II | 10 | -0.123 | çok zayıf negatif |
| Titanfall 2 | 10 | +0.505 | orta pozitif |
| Watch Dogs | 10 | +0.506 | orta pozitif |
| Watch Dogs 2 | 10 | +0.658 | güçlü pozitif |

> r ≈ +1: indirim arttıkça oyuncu artıyor · r ≈ 0: ilişki yok · r ≈ −1: ters ilişki. Korelasyon nedensellik değildir; birkaç günlük veriyle sonuç güvenilir olmaz.
