# 🔎 SQL Analizi

_Otomatik üretildi: 09.10.2026 08:44 UTC · sorgular: [`queries.sql`](../queries.sql)_

## 1. Her oyunun en kalabalık olduğu saat (UTC, ortalamaya göre)

| oyun | zirve_saat_utc | zirve_saat_tr | ort_oyuncu | olcum |
|---|---|---|---|---|
| Rainbow Six Siege | 23:00 | 02:00 | 68,763 | 1 |
| Watch Dogs 2 | 14:00 | 17:00 | 8,384 | 2 |
| Titanfall 2 | 14:00 | 17:00 | 2,552 | 2 |
| Watch Dogs | 14:00 | 17:00 | 2,072 | 2 |
| Star Wars Battlefront II | 18:00 | 21:00 | 1,307 | 1 |

## 2. Günlük ortalama ve günlük değişim (%) — LAG window function

| oyun | gun | gunluk_ort | degisim_yuzde |
|---|---|---|---|
| Rainbow Six Siege | 2026-10-09 | 47,602 | -8.9 |
| Rainbow Six Siege | 2026-10-08 | 52,254 | -0.1 |
| Rainbow Six Siege | 2026-10-07 | 52,319 | -1.9 |
| Rainbow Six Siege | 2026-10-06 | 53,345 | -4.7 |
| Rainbow Six Siege | 2026-10-05 | 55,958 | 3.7 |
| Rainbow Six Siege | 2026-10-03 | 53,977 | -21.5 |
| Rainbow Six Siege | 2026-10-02 | 68,763 | – |
| Star Wars Battlefront II | 2026-10-09 | 712 | -17.1 |
| Star Wars Battlefront II | 2026-10-08 | 859 | -3.6 |
| Star Wars Battlefront II | 2026-10-07 | 891 | 7.2 |
| Star Wars Battlefront II | 2026-10-06 | 831 | -22.5 |
| Star Wars Battlefront II | 2026-10-05 | 1,072 | 16 |
| Star Wars Battlefront II | 2026-10-03 | 924 | -6.7 |
| Star Wars Battlefront II | 2026-10-02 | 990 | – |
| Titanfall 2 | 2026-10-09 | 1,407 | -1.8 |
| Titanfall 2 | 2026-10-08 | 1,433 | -11.5 |
| Titanfall 2 | 2026-10-07 | 1,620 | -9 |
| Titanfall 2 | 2026-10-06 | 1,781 | -16.3 |
| Titanfall 2 | 2026-10-05 | 2,129 | -9.9 |
| Titanfall 2 | 2026-10-03 | 2,363 | 97.2 |
| Titanfall 2 | 2026-10-02 | 1,198 | – |
| Watch Dogs | 2026-10-09 | 1,155 | -16.1 |
| Watch Dogs | 2026-10-08 | 1,376 | -3.6 |
| Watch Dogs | 2026-10-07 | 1,427 | -8.3 |
| Watch Dogs | 2026-10-06 | 1,556 | -24.2 |
| Watch Dogs | 2026-10-05 | 2,052 | 13.2 |
| Watch Dogs | 2026-10-03 | 1,812 | 31.3 |
| Watch Dogs | 2026-10-02 | 1,380 | – |
| Watch Dogs 2 | 2026-10-09 | 3,517 | -6.7 |
| Watch Dogs 2 | 2026-10-08 | 3,769 | -14 |
| Watch Dogs 2 | 2026-10-07 | 4,385 | -13.1 |
| Watch Dogs 2 | 2026-10-06 | 5,045 | -27.8 |
| Watch Dogs 2 | 2026-10-05 | 6,991 | 2.2 |
| Watch Dogs 2 | 2026-10-03 | 6,841 | 170.3 |
| Watch Dogs 2 | 2026-10-02 | 2,531 | – |

## 3. Her ölçümde oyunların sıralaması (son 5 ölçüm) — DENSE_RANK

| zaman_utc | oyun | oyuncu | sira |
|---|---|---|---|
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
| 2026-10-08T16:15:18+00:00 | Rainbow Six Siege | 52,756 | 1 |
| 2026-10-08T16:15:18+00:00 | Watch Dogs 2 | 5,659 | 2 |
| 2026-10-08T16:15:18+00:00 | Watch Dogs | 1,969 | 3 |
| 2026-10-08T16:15:18+00:00 | Titanfall 2 | 1,805 | 4 |
| 2026-10-08T16:15:18+00:00 | Star Wars Battlefront II | 1,049 | 5 |
| 2026-10-08T08:38:43+00:00 | Rainbow Six Siege | 26,086 | 1 |
| 2026-10-08T08:38:43+00:00 | Watch Dogs 2 | 4,870 | 2 |
| 2026-10-08T08:38:43+00:00 | Titanfall 2 | 1,411 | 3 |
| 2026-10-08T08:38:43+00:00 | Watch Dogs | 1,077 | 4 |
| 2026-10-08T08:38:43+00:00 | Star Wars Battlefront II | 439 | 5 |

## 4. Oynaklık: hangi oyunun oyuncu sayısı en çok dalgalanıyor? (max-min / ortalama)

| oyun | min | max | ort | dalga_yuzde |
|---|---|---|---|---|
| Watch Dogs 2 | 2,190 | 8,619 | 4,738 | 135.7 |
| Star Wars Battlefront II | 439 | 1,307 | 881 | 98.6 |
| Titanfall 2 | 1,197 | 2,559 | 1,702 | 80 |
| Rainbow Six Siege | 26,086 | 68,763 | 53,448 | 79.8 |
| Watch Dogs | 1,077 | 2,084 | 1,518 | 66.3 |

## 5. Hafta içi vs hafta sonu ortalaması

| oyun | hafta_sonu | hafta_ici |
|---|---|---|
| Rainbow Six Siege | 53,977 | 53,386 |
| Star Wars Battlefront II | 924 | 875 |
| Titanfall 2 | 2,363 | 1,624 |
| Watch Dogs | 1,812 | 1,484 |
| Watch Dogs 2 | 6,841 | 4,491 |

## 6. Mağaza verisi: fiyat, indirim, yorum puanı + anlık oyuncu (JOIN)

| oyun | anlik_oyuncu | fiyat | para_birimi | indirim_yuzde | toplam_yorum | olumlu_yuzde | steam_puani |
|---|---|---|---|---|---|---|---|
| Rainbow Six Siege | 28,534 | 0 | FREE | 0 | 1,560,721 | 82.1 | Very Positive |
| Watch Dogs 2 | 4,734 | 39.99 | USD | 0 | 104,634 | 82.1 | Very Positive |
| Titanfall 2 | 1,444 | 29.99 | USD | 0 | 287,960 | 95.7 | Overwhelmingly Positive |
| Watch Dogs | 1,141 | 15.99 | USD | 0 | 53,744 | 79.8 | Mostly Positive |
| Star Wars Battlefront II | 524 | 39.99 | USD | 0 | 100,357 | 88.3 | Very Positive |

## 7. İndirim etkisi: indirimli günlerde oyuncu sayısı artıyor mu? (JOIN + koşullu AVG)

| oyun | indirimli_gun | normal_gun | max_indirim_yuzde | ort_indirimli | ort_normal | fark_yuzde |
|---|---|---|---|---|---|---|
| Watch Dogs 2 | 4 | 1 | 95 | 5,047 | 3,517 | 43.5 |
| Watch Dogs | 4 | 1 | 90 | 1,603 | 1,155 | 38.7 |
| Star Wars Battlefront II | 4 | 1 | 75 | 913 | 712 | 28.4 |
| Titanfall 2 | 4 | 1 | 85 | 1,741 | 1,407 | 23.7 |
| Rainbow Six Siege | 0 | 5 | 0 | – | 52,296 | – |

## 8. İndirim × oyuncu sayısı korelasyonu (Pearson r, Python)

| oyun | gun_sayisi | pearson_r | yorum |
|---|---|---|---|
| Rainbow Six Siege | 5 | – | hesaplanamadı (indirim hiç değişmedi) |
| Star Wars Battlefront II | 5 | +0.693 | güçlü pozitif |
| Titanfall 2 | 5 | +0.504 | orta pozitif |
| Watch Dogs | 5 | +0.599 | orta pozitif |
| Watch Dogs 2 | 5 | +0.493 | orta pozitif |

> r ≈ +1: indirim arttıkça oyuncu artıyor · r ≈ 0: ilişki yok · r ≈ −1: ters ilişki. Korelasyon nedensellik değildir; birkaç günlük veriyle sonuç güvenilir olmaz.
