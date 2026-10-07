# 🔎 SQL Analizi

_Otomatik üretildi: 07.10.2026 00:30 UTC · sorgular: [`queries.sql`](../queries.sql)_

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
| Rainbow Six Siege | 2026-10-07 | 65,841 | 23.4 |
| Rainbow Six Siege | 2026-10-06 | 53,345 | -4.7 |
| Rainbow Six Siege | 2026-10-05 | 55,958 | 3.7 |
| Rainbow Six Siege | 2026-10-03 | 53,977 | -21.5 |
| Rainbow Six Siege | 2026-10-02 | 68,763 | – |
| Star Wars Battlefront II | 2026-10-07 | 907 | 9.1 |
| Star Wars Battlefront II | 2026-10-06 | 831 | -22.5 |
| Star Wars Battlefront II | 2026-10-05 | 1,072 | 16 |
| Star Wars Battlefront II | 2026-10-03 | 924 | -6.7 |
| Star Wars Battlefront II | 2026-10-02 | 990 | – |
| Titanfall 2 | 2026-10-07 | 1,197 | -32.8 |
| Titanfall 2 | 2026-10-06 | 1,781 | -16.3 |
| Titanfall 2 | 2026-10-05 | 2,129 | -9.9 |
| Titanfall 2 | 2026-10-03 | 2,363 | 97.2 |
| Titanfall 2 | 2026-10-02 | 1,198 | – |
| Watch Dogs | 2026-10-07 | 1,162 | -25.3 |
| Watch Dogs | 2026-10-06 | 1,556 | -24.2 |
| Watch Dogs | 2026-10-05 | 2,052 | 13.2 |
| Watch Dogs | 2026-10-03 | 1,812 | 31.3 |
| Watch Dogs | 2026-10-02 | 1,380 | – |
| Watch Dogs 2 | 2026-10-07 | 2,190 | -56.6 |
| Watch Dogs 2 | 2026-10-06 | 5,045 | -27.8 |
| Watch Dogs 2 | 2026-10-05 | 6,991 | 2.2 |
| Watch Dogs 2 | 2026-10-03 | 6,841 | 170.3 |
| Watch Dogs 2 | 2026-10-02 | 2,531 | – |

## 3. Her ölçümde oyunların sıralaması (son 5 ölçüm) — DENSE_RANK

| zaman_utc | oyun | oyuncu | sira |
|---|---|---|---|
| 2026-10-07T00:30:04+00:00 | Rainbow Six Siege | 65,841 | 1 |
| 2026-10-07T00:30:04+00:00 | Watch Dogs 2 | 2,190 | 2 |
| 2026-10-07T00:30:04+00:00 | Titanfall 2 | 1,197 | 3 |
| 2026-10-07T00:30:04+00:00 | Watch Dogs | 1,162 | 4 |
| 2026-10-07T00:30:04+00:00 | Star Wars Battlefront II | 907 | 5 |
| 2026-10-06T20:06:57+00:00 | Rainbow Six Siege | 66,634 | 1 |
| 2026-10-06T20:06:57+00:00 | Watch Dogs 2 | 3,604 | 2 |
| 2026-10-06T20:06:57+00:00 | Watch Dogs | 1,666 | 3 |
| 2026-10-06T20:06:57+00:00 | Titanfall 2 | 1,430 | 4 |
| 2026-10-06T20:06:57+00:00 | Star Wars Battlefront II | 1,084 | 5 |
| 2026-10-06T14:55:32+00:00 | Rainbow Six Siege | 48,494 | 1 |
| 2026-10-06T14:55:32+00:00 | Watch Dogs 2 | 8,148 | 2 |
| 2026-10-06T14:55:32+00:00 | Titanfall 2 | 2,545 | 3 |
| 2026-10-06T14:55:32+00:00 | Watch Dogs | 2,084 | 4 |
| 2026-10-06T14:55:32+00:00 | Star Wars Battlefront II | 876 | 5 |
| 2026-10-06T07:22:42+00:00 | Rainbow Six Siege | 29,614 | 1 |
| 2026-10-06T07:22:42+00:00 | Watch Dogs 2 | 6,030 | 2 |
| 2026-10-06T07:22:42+00:00 | Titanfall 2 | 1,893 | 3 |
| 2026-10-06T07:22:42+00:00 | Watch Dogs | 1,240 | 4 |
| 2026-10-06T07:22:42+00:00 | Star Wars Battlefront II | 462 | 5 |
| 2026-10-06T00:41:24+00:00 | Rainbow Six Siege | 68,638 | 1 |
| 2026-10-06T00:41:24+00:00 | Watch Dogs 2 | 2,396 | 2 |
| 2026-10-06T00:41:24+00:00 | Titanfall 2 | 1,256 | 3 |
| 2026-10-06T00:41:24+00:00 | Watch Dogs | 1,233 | 4 |
| 2026-10-06T00:41:24+00:00 | Star Wars Battlefront II | 903 | 5 |

## 4. Oynaklık: hangi oyunun oyuncu sayısı en çok dalgalanıyor? (max-min / ortalama)

| oyun | min | max | ort | dalga_yuzde |
|---|---|---|---|---|
| Watch Dogs 2 | 2,190 | 8,619 | 5,256 | 122.3 |
| Star Wars Battlefront II | 462 | 1,307 | 921 | 91.7 |
| Titanfall 2 | 1,197 | 2,559 | 1,850 | 73.6 |
| Rainbow Six Siege | 29,614 | 68,763 | 56,785 | 68.9 |
| Watch Dogs | 1,162 | 2,084 | 1,649 | 55.9 |

## 5. Hafta içi vs hafta sonu ortalaması

| oyun | hafta_sonu | hafta_ici |
|---|---|---|
| Rainbow Six Siege | 53,977 | 57,488 |
| Star Wars Battlefront II | 924 | 921 |
| Titanfall 2 | 2,363 | 1,722 |
| Watch Dogs | 1,812 | 1,609 |
| Watch Dogs 2 | 6,841 | 4,860 |

## 6. Mağaza verisi: fiyat, indirim, yorum puanı + anlık oyuncu (JOIN)

| oyun | anlik_oyuncu | fiyat | para_birimi | indirim_yuzde | toplam_yorum | olumlu_yuzde | steam_puani |
|---|---|---|---|---|---|---|---|
| Rainbow Six Siege | 65,841 | 0 | FREE | 0 | 1,560,172 | 82.1 | Very Positive |
| Watch Dogs 2 | 2,190 | 1.99 | USD | 95 | 104,429 | 82.1 | Very Positive |
| Titanfall 2 | 1,197 | 4.49 | USD | 85 | 287,795 | 95.7 | Overwhelmingly Positive |
| Watch Dogs | 1,162 | 1.59 | USD | 90 | 53,654 | 79.8 | Mostly Positive |
| Star Wars Battlefront II | 907 | 9.99 | USD | 75 | 100,324 | 88.3 | Very Positive |

## 7. İndirim etkisi: indirimli günlerde oyuncu sayısı artıyor mu? (JOIN + koşullu AVG)

| oyun | indirimli_gun | normal_gun | max_indirim_yuzde | ort_indirimli | ort_normal | fark_yuzde |
|---|---|---|---|---|---|---|
| Watch Dogs 2 | 3 | 0 | 95 | 4,742 | – | – |
| Watch Dogs | 3 | 0 | 90 | 1,590 | – | – |
| Titanfall 2 | 3 | 0 | 85 | 1,702 | – | – |
| Star Wars Battlefront II | 3 | 0 | 75 | 937 | – | – |
| Rainbow Six Siege | 0 | 3 | 0 | – | 58,381 | – |

## 8. İndirim × oyuncu sayısı korelasyonu (Pearson r, Python)

| oyun | gun_sayisi | pearson_r | yorum |
|---|---|---|---|
| Rainbow Six Siege | 3 | – | hesaplanamadı (indirim hiç değişmedi) |
| Star Wars Battlefront II | 3 | – | hesaplanamadı (indirim hiç değişmedi) |
| Titanfall 2 | 3 | – | hesaplanamadı (indirim hiç değişmedi) |
| Watch Dogs | 3 | – | hesaplanamadı (indirim hiç değişmedi) |
| Watch Dogs 2 | 3 | – | hesaplanamadı (indirim hiç değişmedi) |

> r ≈ +1: indirim arttıkça oyuncu artıyor · r ≈ 0: ilişki yok · r ≈ −1: ters ilişki. Korelasyon nedensellik değildir; birkaç günlük veriyle sonuç güvenilir olmaz.
