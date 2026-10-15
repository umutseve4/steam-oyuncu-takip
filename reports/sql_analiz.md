# 🔎 SQL Analizi

_Otomatik üretildi: 15.10.2026 18:07 UTC · sorgular: [`queries.sql`](../queries.sql)_

## 1. Her oyunun en kalabalık olduğu saat (UTC, ortalamaya göre)

| oyun | zirve_saat_utc | zirve_saat_tr | ort_oyuncu | olcum |
|---|---|---|---|---|
| Rainbow Six Siege | 20:00 | 23:00 | 78,793 | 3 |
| Watch Dogs 2 | 14:00 | 17:00 | 8,384 | 2 |
| Titanfall 2 | 14:00 | 17:00 | 2,552 | 2 |
| Watch Dogs | 14:00 | 17:00 | 2,072 | 2 |
| Star Wars Battlefront II | 20:00 | 23:00 | 1,328 | 3 |

## 2. Günlük ortalama ve günlük değişim (%) — LAG window function

| oyun | gun | gunluk_ort | degisim_yuzde |
|---|---|---|---|
| Rainbow Six Siege | 2026-10-15 | 50,925 | -3 |
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
| Star Wars Battlefront II | 2026-10-15 | 758 | -6.7 |
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
| Titanfall 2 | 2026-10-15 | 1,113 | 3.4 |
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
| Watch Dogs | 2026-10-15 | 902 | -5.2 |
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

## 3. Her ölçümde oyunların sıralaması (son 5 ölçüm) — DENSE_RANK

| zaman_utc | oyun | oyuncu | sira |
|---|---|---|---|
| 2026-10-15T18:07:04+00:00 | Rainbow Six Siege | 65,539 | 1 |
| 2026-10-15T18:07:04+00:00 | Watch Dogs 2 | 2,250 | 2 |
| 2026-10-15T18:07:04+00:00 | Watch Dogs | 1,191 | 3 |
| 2026-10-15T18:07:04+00:00 | Star Wars Battlefront II | 1,111 | 4 |
| 2026-10-15T18:07:04+00:00 | Titanfall 2 | 1,044 | 5 |
| 2026-10-15T13:12:51+00:00 | Rainbow Six Siege | 40,723 | 1 |
| 2026-10-15T13:12:51+00:00 | Watch Dogs 2 | 4,196 | 2 |
| 2026-10-15T13:12:51+00:00 | Titanfall 2 | 1,625 | 3 |
| 2026-10-15T13:12:51+00:00 | Watch Dogs | 1,104 | 4 |
| 2026-10-15T13:12:51+00:00 | Star Wars Battlefront II | 669 | 5 |
| 2026-10-15T07:10:50+00:00 | Rainbow Six Siege | 29,412 | 1 |
| 2026-10-15T07:10:50+00:00 | Watch Dogs 2 | 1,954 | 2 |
| 2026-10-15T07:10:50+00:00 | Titanfall 2 | 826 | 3 |
| 2026-10-15T07:10:50+00:00 | Watch Dogs | 581 | 4 |
| 2026-10-15T07:10:50+00:00 | Star Wars Battlefront II | 398 | 5 |
| 2026-10-15T01:18:42+00:00 | Rainbow Six Siege | 68,025 | 1 |
| 2026-10-15T01:18:42+00:00 | Watch Dogs 2 | 1,403 | 2 |
| 2026-10-15T01:18:42+00:00 | Titanfall 2 | 955 | 3 |
| 2026-10-15T01:18:42+00:00 | Star Wars Battlefront II | 855 | 4 |
| 2026-10-15T01:18:42+00:00 | Watch Dogs | 731 | 5 |
| 2026-10-14T22:08:27+00:00 | Rainbow Six Siege | 61,736 | 1 |
| 2026-10-14T22:08:27+00:00 | Watch Dogs 2 | 1,439 | 2 |
| 2026-10-14T22:08:27+00:00 | Titanfall 2 | 876 | 3 |
| 2026-10-14T22:08:27+00:00 | Star Wars Battlefront II | 863 | 4 |
| 2026-10-14T22:08:27+00:00 | Watch Dogs | 854 | 5 |

## 4. Oynaklık: hangi oyunun oyuncu sayısı en çok dalgalanıyor? (max-min / ortalama)

| oyun | min | max | ort | dalga_yuzde |
|---|---|---|---|---|
| Watch Dogs 2 | 1,383 | 8,619 | 3,792 | 190.8 |
| Star Wars Battlefront II | 398 | 1,623 | 935 | 131 |
| Titanfall 2 | 826 | 2,760 | 1,504 | 128.6 |
| Rainbow Six Siege | 26,086 | 91,436 | 56,779 | 115.1 |
| Watch Dogs | 581 | 2,131 | 1,353 | 114.6 |

## 5. Hafta içi vs hafta sonu ortalaması

| oyun | hafta_sonu | hafta_ici |
|---|---|---|
| Rainbow Six Siege | 64,648 | 54,306 |
| Star Wars Battlefront II | 1,133 | 873 |
| Titanfall 2 | 1,863 | 1,392 |
| Watch Dogs | 1,613 | 1,271 |
| Watch Dogs 2 | 4,659 | 3,519 |

## 6. Mağaza verisi: fiyat, indirim, yorum puanı + anlık oyuncu (JOIN)

| oyun | anlik_oyuncu | fiyat | para_birimi | indirim_yuzde | toplam_yorum | olumlu_yuzde | steam_puani |
|---|---|---|---|---|---|---|---|
| Rainbow Six Siege | 65,539 | 0 | FREE | 0 | 1,562,508 | 82.1 | Very Positive |
| Watch Dogs 2 | 2,250 | 39.99 | USD | 0 | 105,099 | 82.1 | Very Positive |
| Watch Dogs | 1,191 | 15.99 | USD | 0 | 53,962 | 79.8 | Mostly Positive |
| Star Wars Battlefront II | 1,111 | 39.99 | USD | 0 | 100,454 | 88.3 | Very Positive |
| Titanfall 2 | 1,044 | 29.99 | USD | 0 | 288,324 | 95.7 | Overwhelmingly Positive |

## 7. İndirim etkisi: indirimli günlerde oyuncu sayısı artıyor mu? (JOIN + koşullu AVG)

| oyun | indirimli_gun | normal_gun | max_indirim_yuzde | ort_indirimli | ort_normal | fark_yuzde |
|---|---|---|---|---|---|---|
| Watch Dogs 2 | 4 | 7 | 95 | 5,047 | 3,123 | 61.6 |
| Watch Dogs | 4 | 7 | 90 | 1,603 | 1,228 | 30.5 |
| Titanfall 2 | 4 | 7 | 85 | 1,741 | 1,358 | 28.2 |
| Star Wars Battlefront II | 4 | 7 | 75 | 913 | 953 | -4.2 |
| Rainbow Six Siege | 0 | 11 | 0 | – | 56,546 | – |

## 8. İndirim × oyuncu sayısı korelasyonu (Pearson r, Python)

| oyun | gun_sayisi | pearson_r | yorum |
|---|---|---|---|
| Rainbow Six Siege | 11 | – | hesaplanamadı (indirim hiç değişmedi) |
| Star Wars Battlefront II | 11 | -0.133 | çok zayıf negatif |
| Titanfall 2 | 11 | +0.543 | orta pozitif |
| Watch Dogs | 11 | +0.551 | orta pozitif |
| Watch Dogs 2 | 11 | +0.684 | güçlü pozitif |

> r ≈ +1: indirim arttıkça oyuncu artıyor · r ≈ 0: ilişki yok · r ≈ −1: ters ilişki. Korelasyon nedensellik değildir; birkaç günlük veriyle sonuç güvenilir olmaz.
