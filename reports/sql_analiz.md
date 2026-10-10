# 🔎 SQL Analizi

_Otomatik üretildi: 10.10.2026 18:21 UTC · sorgular: [`queries.sql`](../queries.sql)_

## 1. Her oyunun en kalabalık olduğu saat (UTC, ortalamaya göre)

| oyun | zirve_saat_utc | zirve_saat_tr | ort_oyuncu | olcum |
|---|---|---|---|---|
| Rainbow Six Siege | 20:00 | 23:00 | 72,472 | 2 |
| Watch Dogs 2 | 14:00 | 17:00 | 8,384 | 2 |
| Titanfall 2 | 13:00 | 16:00 | 2,760 | 1 |
| Watch Dogs | 13:00 | 16:00 | 2,093 | 1 |
| Star Wars Battlefront II | 18:00 | 21:00 | 1,465 | 2 |

## 2. Günlük ortalama ve günlük değişim (%) — LAG window function

| oyun | gun | gunluk_ort | degisim_yuzde |
|---|---|---|---|
| Rainbow Six Siege | 2026-10-10 | 62,328 | 7.7 |
| Rainbow Six Siege | 2026-10-09 | 57,891 | 10.8 |
| Rainbow Six Siege | 2026-10-08 | 52,254 | -0.1 |
| Rainbow Six Siege | 2026-10-07 | 52,319 | -1.9 |
| Rainbow Six Siege | 2026-10-06 | 53,345 | -4.7 |
| Rainbow Six Siege | 2026-10-05 | 55,958 | 3.7 |
| Rainbow Six Siege | 2026-10-03 | 53,977 | -21.5 |
| Rainbow Six Siege | 2026-10-02 | 68,763 | – |
| Star Wars Battlefront II | 2026-10-10 | 1,094 | 11.9 |
| Star Wars Battlefront II | 2026-10-09 | 978 | 13.9 |
| Star Wars Battlefront II | 2026-10-08 | 859 | -3.6 |
| Star Wars Battlefront II | 2026-10-07 | 891 | 7.2 |
| Star Wars Battlefront II | 2026-10-06 | 831 | -22.5 |
| Star Wars Battlefront II | 2026-10-05 | 1,072 | 16 |
| Star Wars Battlefront II | 2026-10-03 | 924 | -6.7 |
| Star Wars Battlefront II | 2026-10-02 | 990 | – |
| Titanfall 2 | 2026-10-10 | 1,801 | 14.1 |
| Titanfall 2 | 2026-10-09 | 1,579 | 10.2 |
| Titanfall 2 | 2026-10-08 | 1,433 | -11.5 |
| Titanfall 2 | 2026-10-07 | 1,620 | -9 |
| Titanfall 2 | 2026-10-06 | 1,781 | -16.3 |
| Titanfall 2 | 2026-10-05 | 2,129 | -9.9 |
| Titanfall 2 | 2026-10-03 | 2,363 | 97.2 |
| Titanfall 2 | 2026-10-02 | 1,198 | – |
| Watch Dogs | 2026-10-10 | 1,556 | 8.2 |
| Watch Dogs | 2026-10-09 | 1,438 | 4.5 |
| Watch Dogs | 2026-10-08 | 1,376 | -3.6 |
| Watch Dogs | 2026-10-07 | 1,427 | -8.3 |
| Watch Dogs | 2026-10-06 | 1,556 | -24.2 |
| Watch Dogs | 2026-10-05 | 2,052 | 13.2 |
| Watch Dogs | 2026-10-03 | 1,812 | 31.3 |
| Watch Dogs | 2026-10-02 | 1,380 | – |
| Watch Dogs 2 | 2026-10-10 | 4,519 | 17 |
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
| 2026-10-10T18:21:22+00:00 | Rainbow Six Siege | 79,757 | 1 |
| 2026-10-10T18:21:22+00:00 | Watch Dogs 2 | 4,186 | 2 |
| 2026-10-10T18:21:22+00:00 | Watch Dogs | 1,873 | 3 |
| 2026-10-10T18:21:22+00:00 | Titanfall 2 | 1,751 | 4 |
| 2026-10-10T18:21:22+00:00 | Star Wars Battlefront II | 1,623 | 5 |
| 2026-10-10T13:27:22+00:00 | Rainbow Six Siege | 59,539 | 1 |
| 2026-10-10T13:27:22+00:00 | Watch Dogs 2 | 8,034 | 2 |
| 2026-10-10T13:27:22+00:00 | Titanfall 2 | 2,760 | 3 |
| 2026-10-10T13:27:22+00:00 | Watch Dogs | 2,093 | 4 |
| 2026-10-10T13:27:22+00:00 | Star Wars Battlefront II | 1,132 | 5 |
| 2026-10-10T06:51:30+00:00 | Rainbow Six Siege | 45,132 | 1 |
| 2026-10-10T06:51:30+00:00 | Watch Dogs 2 | 3,919 | 2 |
| 2026-10-10T06:51:30+00:00 | Titanfall 2 | 1,466 | 3 |
| 2026-10-10T06:51:30+00:00 | Watch Dogs | 1,117 | 4 |
| 2026-10-10T06:51:30+00:00 | Star Wars Battlefront II | 655 | 5 |
| 2026-10-10T00:37:46+00:00 | Rainbow Six Siege | 64,882 | 1 |
| 2026-10-10T00:37:46+00:00 | Watch Dogs 2 | 1,938 | 2 |
| 2026-10-10T00:37:46+00:00 | Titanfall 2 | 1,225 | 3 |
| 2026-10-10T00:37:46+00:00 | Watch Dogs | 1,139 | 4 |
| 2026-10-10T00:37:46+00:00 | Star Wars Battlefront II | 966 | 5 |
| 2026-10-09T20:47:37+00:00 | Rainbow Six Siege | 78,309 | 1 |
| 2026-10-09T20:47:37+00:00 | Watch Dogs 2 | 2,727 | 2 |
| 2026-10-09T20:47:37+00:00 | Watch Dogs | 1,511 | 3 |
| 2026-10-09T20:47:37+00:00 | Titanfall 2 | 1,453 | 4 |
| 2026-10-09T20:47:37+00:00 | Star Wars Battlefront II | 1,327 | 5 |

## 4. Oynaklık: hangi oyunun oyuncu sayısı en çok dalgalanıyor? (max-min / ortalama)

| oyun | min | max | ort | dalga_yuzde |
|---|---|---|---|---|
| Watch Dogs 2 | 1,938 | 8,619 | 4,661 | 143.4 |
| Star Wars Battlefront II | 439 | 1,623 | 944 | 125.4 |
| Rainbow Six Siege | 26,086 | 79,757 | 56,047 | 95.8 |
| Titanfall 2 | 1,197 | 2,760 | 1,721 | 90.8 |
| Watch Dogs | 1,077 | 2,093 | 1,541 | 66 |

## 5. Hafta içi vs hafta sonu ortalaması

| oyun | hafta_sonu | hafta_ici |
|---|---|---|
| Rainbow Six Siege | 59,544 | 54,943 |
| Star Wars Battlefront II | 1,037 | 914 |
| Titanfall 2 | 1,988 | 1,637 |
| Watch Dogs | 1,641 | 1,509 |
| Watch Dogs 2 | 5,293 | 4,461 |

## 6. Mağaza verisi: fiyat, indirim, yorum puanı + anlık oyuncu (JOIN)

| oyun | anlik_oyuncu | fiyat | para_birimi | indirim_yuzde | toplam_yorum | olumlu_yuzde | steam_puani |
|---|---|---|---|---|---|---|---|
| Rainbow Six Siege | 79,757 | 0 | FREE | 0 | 1,561,003 | 82.1 | Very Positive |
| Watch Dogs 2 | 4,186 | 39.99 | USD | 0 | 104,704 | 82.1 | Very Positive |
| Watch Dogs | 1,873 | 15.99 | USD | 0 | 53,774 | 79.8 | Mostly Positive |
| Titanfall 2 | 1,751 | 29.99 | USD | 0 | 288,043 | 95.7 | Overwhelmingly Positive |
| Star Wars Battlefront II | 1,623 | 39.99 | USD | 0 | 100,372 | 88.3 | Very Positive |

## 7. İndirim etkisi: indirimli günlerde oyuncu sayısı artıyor mu? (JOIN + koşullu AVG)

| oyun | indirimli_gun | normal_gun | max_indirim_yuzde | ort_indirimli | ort_normal | fark_yuzde |
|---|---|---|---|---|---|---|
| Watch Dogs 2 | 4 | 2 | 95 | 5,047 | 4,191 | 20.4 |
| Watch Dogs | 4 | 2 | 90 | 1,603 | 1,497 | 7.1 |
| Titanfall 2 | 4 | 2 | 85 | 1,741 | 1,690 | 3 |
| Star Wars Battlefront II | 4 | 2 | 75 | 913 | 1,036 | -11.9 |
| Rainbow Six Siege | 0 | 6 | 0 | – | 55,682 | – |

## 8. İndirim × oyuncu sayısı korelasyonu (Pearson r, Python)

| oyun | gun_sayisi | pearson_r | yorum |
|---|---|---|---|
| Rainbow Six Siege | 6 | – | hesaplanamadı (indirim hiç değişmedi) |
| Star Wars Battlefront II | 6 | -0.570 | orta negatif |
| Titanfall 2 | 6 | +0.110 | çok zayıf pozitif |
| Watch Dogs | 6 | +0.220 | zayıf pozitif |
| Watch Dogs 2 | 6 | +0.373 | zayıf pozitif |

> r ≈ +1: indirim arttıkça oyuncu artıyor · r ≈ 0: ilişki yok · r ≈ −1: ters ilişki. Korelasyon nedensellik değildir; birkaç günlük veriyle sonuç güvenilir olmaz.
