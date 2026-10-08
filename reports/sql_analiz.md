# 🔎 SQL Analizi

_Otomatik üretildi: 08.10.2026 01:39 UTC · sorgular: [`queries.sql`](../queries.sql)_

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
| Rainbow Six Siege | 2026-10-08 | 68,630 | 31.2 |
| Rainbow Six Siege | 2026-10-07 | 52,319 | -1.9 |
| Rainbow Six Siege | 2026-10-06 | 53,345 | -4.7 |
| Rainbow Six Siege | 2026-10-05 | 55,958 | 3.7 |
| Rainbow Six Siege | 2026-10-03 | 53,977 | -21.5 |
| Rainbow Six Siege | 2026-10-02 | 68,763 | – |
| Star Wars Battlefront II | 2026-10-08 | 957 | 7.4 |
| Star Wars Battlefront II | 2026-10-07 | 891 | 7.2 |
| Star Wars Battlefront II | 2026-10-06 | 831 | -22.5 |
| Star Wars Battlefront II | 2026-10-05 | 1,072 | 16 |
| Star Wars Battlefront II | 2026-10-03 | 924 | -6.7 |
| Star Wars Battlefront II | 2026-10-02 | 990 | – |
| Titanfall 2 | 2026-10-08 | 1,278 | -21.1 |
| Titanfall 2 | 2026-10-07 | 1,620 | -9 |
| Titanfall 2 | 2026-10-06 | 1,781 | -16.3 |
| Titanfall 2 | 2026-10-05 | 2,129 | -9.9 |
| Titanfall 2 | 2026-10-03 | 2,363 | 97.2 |
| Titanfall 2 | 2026-10-02 | 1,198 | – |
| Watch Dogs | 2026-10-08 | 1,158 | -18.9 |
| Watch Dogs | 2026-10-07 | 1,427 | -8.3 |
| Watch Dogs | 2026-10-06 | 1,556 | -24.2 |
| Watch Dogs | 2026-10-05 | 2,052 | 13.2 |
| Watch Dogs | 2026-10-03 | 1,812 | 31.3 |
| Watch Dogs | 2026-10-02 | 1,380 | – |
| Watch Dogs 2 | 2026-10-08 | 2,311 | -47.3 |
| Watch Dogs 2 | 2026-10-07 | 4,385 | -13.1 |
| Watch Dogs 2 | 2026-10-06 | 5,045 | -27.8 |
| Watch Dogs 2 | 2026-10-05 | 6,991 | 2.2 |
| Watch Dogs 2 | 2026-10-03 | 6,841 | 170.3 |
| Watch Dogs 2 | 2026-10-02 | 2,531 | – |

## 3. Her ölçümde oyunların sıralaması (son 5 ölçüm) — DENSE_RANK

| zaman_utc | oyun | oyuncu | sira |
|---|---|---|---|
| 2026-10-08T01:39:19+00:00 | Rainbow Six Siege | 68,630 | 1 |
| 2026-10-08T01:39:19+00:00 | Watch Dogs 2 | 2,311 | 2 |
| 2026-10-08T01:39:19+00:00 | Titanfall 2 | 1,278 | 3 |
| 2026-10-08T01:39:19+00:00 | Watch Dogs | 1,158 | 4 |
| 2026-10-08T01:39:19+00:00 | Star Wars Battlefront II | 957 | 5 |
| 2026-10-07T21:07:32+00:00 | Rainbow Six Siege | 63,774 | 1 |
| 2026-10-07T21:07:32+00:00 | Watch Dogs 2 | 2,563 | 2 |
| 2026-10-07T21:07:32+00:00 | Watch Dogs | 1,411 | 3 |
| 2026-10-07T21:07:32+00:00 | Titanfall 2 | 1,258 | 4 |
| 2026-10-07T21:07:32+00:00 | Star Wars Battlefront II | 1,160 | 5 |
| 2026-10-07T15:22:23+00:00 | Rainbow Six Siege | 49,572 | 1 |
| 2026-10-07T15:22:23+00:00 | Watch Dogs 2 | 7,237 | 2 |
| 2026-10-07T15:22:23+00:00 | Titanfall 2 | 2,249 | 3 |
| 2026-10-07T15:22:23+00:00 | Watch Dogs | 1,959 | 4 |
| 2026-10-07T15:22:23+00:00 | Star Wars Battlefront II | 986 | 5 |
| 2026-10-07T07:01:32+00:00 | Rainbow Six Siege | 30,089 | 1 |
| 2026-10-07T07:01:32+00:00 | Watch Dogs 2 | 5,551 | 2 |
| 2026-10-07T07:01:32+00:00 | Titanfall 2 | 1,777 | 3 |
| 2026-10-07T07:01:32+00:00 | Watch Dogs | 1,175 | 4 |
| 2026-10-07T07:01:32+00:00 | Star Wars Battlefront II | 512 | 5 |
| 2026-10-07T00:30:04+00:00 | Rainbow Six Siege | 65,841 | 1 |
| 2026-10-07T00:30:04+00:00 | Watch Dogs 2 | 2,190 | 2 |
| 2026-10-07T00:30:04+00:00 | Titanfall 2 | 1,197 | 3 |
| 2026-10-07T00:30:04+00:00 | Watch Dogs | 1,162 | 4 |
| 2026-10-07T00:30:04+00:00 | Star Wars Battlefront II | 907 | 5 |

## 4. Oynaklık: hangi oyunun oyuncu sayısı en çok dalgalanıyor? (max-min / ortalama)

| oyun | min | max | ort | dalga_yuzde |
|---|---|---|---|---|
| Watch Dogs 2 | 2,190 | 8,619 | 5,016 | 128.2 |
| Star Wars Battlefront II | 462 | 1,307 | 916 | 92.2 |
| Titanfall 2 | 1,197 | 2,559 | 1,790 | 76.1 |
| Rainbow Six Siege | 29,614 | 68,763 | 55,709 | 70.3 |
| Watch Dogs | 1,158 | 2,084 | 1,585 | 58.4 |

## 5. Hafta içi vs hafta sonu ortalaması

| oyun | hafta_sonu | hafta_ici |
|---|---|---|
| Rainbow Six Siege | 53,977 | 55,997 |
| Star Wars Battlefront II | 924 | 915 |
| Titanfall 2 | 2,363 | 1,695 |
| Watch Dogs | 1,812 | 1,548 |
| Watch Dogs 2 | 6,841 | 4,712 |

## 6. Mağaza verisi: fiyat, indirim, yorum puanı + anlık oyuncu (JOIN)

| oyun | anlik_oyuncu | fiyat | para_birimi | indirim_yuzde | toplam_yorum | olumlu_yuzde | steam_puani |
|---|---|---|---|---|---|---|---|
| Rainbow Six Siege | 68,630 | 0 | FREE | 0 | 1,560,465 | 82.1 | Very Positive |
| Watch Dogs 2 | 2,311 | 1.99 | USD | 95 | 104,559 | 82.1 | Very Positive |
| Titanfall 2 | 1,278 | 4.49 | USD | 85 | 287,892 | 95.7 | Overwhelmingly Positive |
| Watch Dogs | 1,158 | 1.59 | USD | 90 | 53,702 | 79.8 | Mostly Positive |
| Star Wars Battlefront II | 957 | 9.99 | USD | 75 | 100,338 | 88.3 | Very Positive |

## 7. İndirim etkisi: indirimli günlerde oyuncu sayısı artıyor mu? (JOIN + koşullu AVG)

| oyun | indirimli_gun | normal_gun | max_indirim_yuzde | ort_indirimli | ort_normal | fark_yuzde |
|---|---|---|---|---|---|---|
| Watch Dogs 2 | 4 | 0 | 95 | 4,683 | – | – |
| Watch Dogs | 4 | 0 | 90 | 1,548 | – | – |
| Titanfall 2 | 4 | 0 | 85 | 1,702 | – | – |
| Star Wars Battlefront II | 4 | 0 | 75 | 938 | – | – |
| Rainbow Six Siege | 0 | 4 | 0 | – | 57,563 | – |

## 8. İndirim × oyuncu sayısı korelasyonu (Pearson r, Python)

| oyun | gun_sayisi | pearson_r | yorum |
|---|---|---|---|
| Rainbow Six Siege | 4 | – | hesaplanamadı (indirim hiç değişmedi) |
| Star Wars Battlefront II | 4 | – | hesaplanamadı (indirim hiç değişmedi) |
| Titanfall 2 | 4 | – | hesaplanamadı (indirim hiç değişmedi) |
| Watch Dogs | 4 | – | hesaplanamadı (indirim hiç değişmedi) |
| Watch Dogs 2 | 4 | – | hesaplanamadı (indirim hiç değişmedi) |

> r ≈ +1: indirim arttıkça oyuncu artıyor · r ≈ 0: ilişki yok · r ≈ −1: ters ilişki. Korelasyon nedensellik değildir; birkaç günlük veriyle sonuç güvenilir olmaz.
