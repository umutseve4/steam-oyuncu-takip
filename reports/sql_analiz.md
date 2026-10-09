# 🔎 SQL Analizi

_Otomatik üretildi: 09.10.2026 20:47 UTC · sorgular: [`queries.sql`](../queries.sql)_

## 1. Her oyunun en kalabalık olduğu saat (UTC, ortalamaya göre)

| oyun | zirve_saat_utc | zirve_saat_tr | ort_oyuncu | olcum |
|---|---|---|---|---|
| Rainbow Six Siege | 20:00 | 23:00 | 72,472 | 2 |
| Watch Dogs 2 | 14:00 | 17:00 | 8,384 | 2 |
| Titanfall 2 | 14:00 | 17:00 | 2,552 | 2 |
| Watch Dogs | 14:00 | 17:00 | 2,072 | 2 |
| Star Wars Battlefront II | 18:00 | 21:00 | 1,307 | 1 |

## 2. Günlük ortalama ve günlük değişim (%) — LAG window function

| oyun | gun | gunluk_ort | degisim_yuzde |
|---|---|---|---|
| Rainbow Six Siege | 2026-10-09 | 57,891 | 10.8 |
| Rainbow Six Siege | 2026-10-08 | 52,254 | -0.1 |
| Rainbow Six Siege | 2026-10-07 | 52,319 | -1.9 |
| Rainbow Six Siege | 2026-10-06 | 53,345 | -4.7 |
| Rainbow Six Siege | 2026-10-05 | 55,958 | 3.7 |
| Rainbow Six Siege | 2026-10-03 | 53,977 | -21.5 |
| Rainbow Six Siege | 2026-10-02 | 68,763 | – |
| Star Wars Battlefront II | 2026-10-09 | 978 | 13.9 |
| Star Wars Battlefront II | 2026-10-08 | 859 | -3.6 |
| Star Wars Battlefront II | 2026-10-07 | 891 | 7.2 |
| Star Wars Battlefront II | 2026-10-06 | 831 | -22.5 |
| Star Wars Battlefront II | 2026-10-05 | 1,072 | 16 |
| Star Wars Battlefront II | 2026-10-03 | 924 | -6.7 |
| Star Wars Battlefront II | 2026-10-02 | 990 | – |
| Titanfall 2 | 2026-10-09 | 1,579 | 10.2 |
| Titanfall 2 | 2026-10-08 | 1,433 | -11.5 |
| Titanfall 2 | 2026-10-07 | 1,620 | -9 |
| Titanfall 2 | 2026-10-06 | 1,781 | -16.3 |
| Titanfall 2 | 2026-10-05 | 2,129 | -9.9 |
| Titanfall 2 | 2026-10-03 | 2,363 | 97.2 |
| Titanfall 2 | 2026-10-02 | 1,198 | – |
| Watch Dogs | 2026-10-09 | 1,438 | 4.5 |
| Watch Dogs | 2026-10-08 | 1,376 | -3.6 |
| Watch Dogs | 2026-10-07 | 1,427 | -8.3 |
| Watch Dogs | 2026-10-06 | 1,556 | -24.2 |
| Watch Dogs | 2026-10-05 | 2,052 | 13.2 |
| Watch Dogs | 2026-10-03 | 1,812 | 31.3 |
| Watch Dogs | 2026-10-02 | 1,380 | – |
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
| 2026-10-09T20:47:37+00:00 | Rainbow Six Siege | 78,309 | 1 |
| 2026-10-09T20:47:37+00:00 | Watch Dogs 2 | 2,727 | 2 |
| 2026-10-09T20:47:37+00:00 | Watch Dogs | 1,511 | 3 |
| 2026-10-09T20:47:37+00:00 | Titanfall 2 | 1,453 | 4 |
| 2026-10-09T20:47:37+00:00 | Star Wars Battlefront II | 1,327 | 5 |
| 2026-10-09T15:59:07+00:00 | Rainbow Six Siege | 58,051 | 1 |
| 2026-10-09T15:59:07+00:00 | Watch Dogs 2 | 5,688 | 2 |
| 2026-10-09T15:59:07+00:00 | Titanfall 2 | 2,047 | 3 |
| 2026-10-09T15:59:07+00:00 | Watch Dogs | 1,931 | 4 |
| 2026-10-09T15:59:07+00:00 | Star Wars Battlefront II | 1,163 | 5 |
| 2026-10-09T08:44:04+00:00 | Rainbow Six Siege | 28,534 | 1 |
| 2026-10-09T08:44:04+00:00 | Watch Dogs 2 | 4,734 | 2 |
| 2026-10-09T08:44:04+00:00 | Titanfall 2 | 1,444 | 3 |
| 2026-10-09T08:44:04+00:00 | Watch Dogs | 1,141 | 4 |
| 2026-10-09T08:44:04+00:00 | Star Wars Battlefront II | 524 | 5 |
| 2026-10-09T01:52:34+00:00 | Rainbow Six Siege | 66,670 | 1 |
| 2026-10-09T01:52:34+00:00 | Watch Dogs 2 | 2,299 | 2 |
| 2026-10-09T01:52:34+00:00 | Titanfall 2 | 1,370 | 3 |
| 2026-10-09T01:52:34+00:00 | Watch Dogs | 1,169 | 4 |
| 2026-10-09T01:52:34+00:00 | Star Wars Battlefront II | 899 | 5 |
| 2026-10-08T21:54:08+00:00 | Rainbow Six Siege | 61,543 | 1 |
| 2026-10-08T21:54:08+00:00 | Watch Dogs 2 | 2,237 | 2 |
| 2026-10-08T21:54:08+00:00 | Watch Dogs | 1,298 | 3 |
| 2026-10-08T21:54:08+00:00 | Titanfall 2 | 1,238 | 4 |
| 2026-10-08T21:54:08+00:00 | Star Wars Battlefront II | 992 | 5 |

## 4. Oynaklık: hangi oyunun oyuncu sayısı en çok dalgalanıyor? (max-min / ortalama)

| oyun | min | max | ort | dalga_yuzde |
|---|---|---|---|---|
| Watch Dogs 2 | 2,190 | 8,619 | 4,687 | 137.2 |
| Star Wars Battlefront II | 439 | 1,327 | 915 | 97 |
| Rainbow Six Siege | 26,086 | 78,309 | 54,851 | 95.2 |
| Titanfall 2 | 1,197 | 2,559 | 1,706 | 79.8 |
| Watch Dogs | 1,077 | 2,084 | 1,538 | 65.5 |

## 5. Hafta içi vs hafta sonu ortalaması

| oyun | hafta_sonu | hafta_ici |
|---|---|---|
| Rainbow Six Siege | 53,977 | 54,943 |
| Star Wars Battlefront II | 924 | 914 |
| Titanfall 2 | 2,363 | 1,637 |
| Watch Dogs | 1,812 | 1,509 |
| Watch Dogs 2 | 6,841 | 4,461 |

## 6. Mağaza verisi: fiyat, indirim, yorum puanı + anlık oyuncu (JOIN)

| oyun | anlik_oyuncu | fiyat | para_birimi | indirim_yuzde | toplam_yorum | olumlu_yuzde | steam_puani |
|---|---|---|---|---|---|---|---|
| Rainbow Six Siege | 78,309 | 0 | FREE | 0 | 1,560,721 | 82.1 | Very Positive |
| Watch Dogs 2 | 2,727 | 39.99 | USD | 0 | 104,634 | 82.1 | Very Positive |
| Watch Dogs | 1,511 | 15.99 | USD | 0 | 53,744 | 79.8 | Mostly Positive |
| Titanfall 2 | 1,453 | 29.99 | USD | 0 | 287,960 | 95.7 | Overwhelmingly Positive |
| Star Wars Battlefront II | 1,327 | 39.99 | USD | 0 | 100,357 | 88.3 | Very Positive |

## 7. İndirim etkisi: indirimli günlerde oyuncu sayısı artıyor mu? (JOIN + koşullu AVG)

| oyun | indirimli_gun | normal_gun | max_indirim_yuzde | ort_indirimli | ort_normal | fark_yuzde |
|---|---|---|---|---|---|---|
| Watch Dogs 2 | 4 | 1 | 95 | 5,047 | 3,862 | 30.7 |
| Watch Dogs | 4 | 1 | 90 | 1,603 | 1,438 | 11.4 |
| Titanfall 2 | 4 | 1 | 85 | 1,741 | 1,579 | 10.3 |
| Star Wars Battlefront II | 4 | 1 | 75 | 913 | 978 | -6.6 |
| Rainbow Six Siege | 0 | 5 | 0 | – | 54,353 | – |

## 8. İndirim × oyuncu sayısı korelasyonu (Pearson r, Python)

| oyun | gun_sayisi | pearson_r | yorum |
|---|---|---|---|
| Rainbow Six Siege | 5 | – | hesaplanamadı (indirim hiç değişmedi) |
| Star Wars Battlefront II | 5 | -0.296 | zayıf negatif |
| Titanfall 2 | 5 | +0.273 | zayıf pozitif |
| Watch Dogs | 5 | +0.265 | zayıf pozitif |
| Watch Dogs 2 | 5 | +0.402 | orta pozitif |

> r ≈ +1: indirim arttıkça oyuncu artıyor · r ≈ 0: ilişki yok · r ≈ −1: ters ilişki. Korelasyon nedensellik değildir; birkaç günlük veriyle sonuç güvenilir olmaz.
