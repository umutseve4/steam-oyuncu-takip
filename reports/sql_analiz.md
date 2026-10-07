# 🔎 SQL Analizi

_Otomatik üretildi: 07.10.2026 21:07 UTC · sorgular: [`queries.sql`](../queries.sql)_

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
| Rainbow Six Siege | 2026-10-07 | 52,319 | -1.9 |
| Rainbow Six Siege | 2026-10-06 | 53,345 | -4.7 |
| Rainbow Six Siege | 2026-10-05 | 55,958 | 3.7 |
| Rainbow Six Siege | 2026-10-03 | 53,977 | -21.5 |
| Rainbow Six Siege | 2026-10-02 | 68,763 | – |
| Star Wars Battlefront II | 2026-10-07 | 891 | 7.2 |
| Star Wars Battlefront II | 2026-10-06 | 831 | -22.5 |
| Star Wars Battlefront II | 2026-10-05 | 1,072 | 16 |
| Star Wars Battlefront II | 2026-10-03 | 924 | -6.7 |
| Star Wars Battlefront II | 2026-10-02 | 990 | – |
| Titanfall 2 | 2026-10-07 | 1,620 | -9 |
| Titanfall 2 | 2026-10-06 | 1,781 | -16.3 |
| Titanfall 2 | 2026-10-05 | 2,129 | -9.9 |
| Titanfall 2 | 2026-10-03 | 2,363 | 97.2 |
| Titanfall 2 | 2026-10-02 | 1,198 | – |
| Watch Dogs | 2026-10-07 | 1,427 | -8.3 |
| Watch Dogs | 2026-10-06 | 1,556 | -24.2 |
| Watch Dogs | 2026-10-05 | 2,052 | 13.2 |
| Watch Dogs | 2026-10-03 | 1,812 | 31.3 |
| Watch Dogs | 2026-10-02 | 1,380 | – |
| Watch Dogs 2 | 2026-10-07 | 4,385 | -13.1 |
| Watch Dogs 2 | 2026-10-06 | 5,045 | -27.8 |
| Watch Dogs 2 | 2026-10-05 | 6,991 | 2.2 |
| Watch Dogs 2 | 2026-10-03 | 6,841 | 170.3 |
| Watch Dogs 2 | 2026-10-02 | 2,531 | – |

## 3. Her ölçümde oyunların sıralaması (son 5 ölçüm) — DENSE_RANK

| zaman_utc | oyun | oyuncu | sira |
|---|---|---|---|
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
| 2026-10-06T20:06:57+00:00 | Rainbow Six Siege | 66,634 | 1 |
| 2026-10-06T20:06:57+00:00 | Watch Dogs 2 | 3,604 | 2 |
| 2026-10-06T20:06:57+00:00 | Watch Dogs | 1,666 | 3 |
| 2026-10-06T20:06:57+00:00 | Titanfall 2 | 1,430 | 4 |
| 2026-10-06T20:06:57+00:00 | Star Wars Battlefront II | 1,084 | 5 |

## 4. Oynaklık: hangi oyunun oyuncu sayısı en çok dalgalanıyor? (max-min / ortalama)

| oyun | min | max | ort | dalga_yuzde |
|---|---|---|---|---|
| Watch Dogs 2 | 2,190 | 8,619 | 5,224 | 123.1 |
| Star Wars Battlefront II | 462 | 1,307 | 913 | 92.5 |
| Titanfall 2 | 1,197 | 2,559 | 1,830 | 74.4 |
| Rainbow Six Siege | 29,614 | 68,763 | 54,715 | 71.6 |
| Watch Dogs | 1,162 | 2,084 | 1,618 | 57 |

## 5. Hafta içi vs hafta sonu ortalaması

| oyun | hafta_sonu | hafta_ici |
|---|---|---|
| Rainbow Six Siege | 53,977 | 54,849 |
| Star Wars Battlefront II | 924 | 911 |
| Titanfall 2 | 2,363 | 1,733 |
| Watch Dogs | 1,812 | 1,583 |
| Watch Dogs 2 | 6,841 | 4,930 |

## 6. Mağaza verisi: fiyat, indirim, yorum puanı + anlık oyuncu (JOIN)

| oyun | anlik_oyuncu | fiyat | para_birimi | indirim_yuzde | toplam_yorum | olumlu_yuzde | steam_puani |
|---|---|---|---|---|---|---|---|
| Rainbow Six Siege | 63,774 | 0 | FREE | 0 | 1,560,172 | 82.1 | Very Positive |
| Watch Dogs 2 | 2,563 | 1.99 | USD | 95 | 104,429 | 82.1 | Very Positive |
| Watch Dogs | 1,411 | 1.59 | USD | 90 | 53,654 | 79.8 | Mostly Positive |
| Titanfall 2 | 1,258 | 4.49 | USD | 85 | 287,795 | 95.7 | Overwhelmingly Positive |
| Star Wars Battlefront II | 1,160 | 9.99 | USD | 75 | 100,324 | 88.3 | Very Positive |

## 7. İndirim etkisi: indirimli günlerde oyuncu sayısı artıyor mu? (JOIN + koşullu AVG)

| oyun | indirimli_gun | normal_gun | max_indirim_yuzde | ort_indirimli | ort_normal | fark_yuzde |
|---|---|---|---|---|---|---|
| Watch Dogs 2 | 3 | 0 | 95 | 5,473 | – | – |
| Watch Dogs | 3 | 0 | 90 | 1,678 | – | – |
| Titanfall 2 | 3 | 0 | 85 | 1,843 | – | – |
| Star Wars Battlefront II | 3 | 0 | 75 | 931 | – | – |
| Rainbow Six Siege | 0 | 3 | 0 | – | 53,874 | – |

## 8. İndirim × oyuncu sayısı korelasyonu (Pearson r, Python)

| oyun | gun_sayisi | pearson_r | yorum |
|---|---|---|---|
| Rainbow Six Siege | 3 | – | hesaplanamadı (indirim hiç değişmedi) |
| Star Wars Battlefront II | 3 | – | hesaplanamadı (indirim hiç değişmedi) |
| Titanfall 2 | 3 | – | hesaplanamadı (indirim hiç değişmedi) |
| Watch Dogs | 3 | – | hesaplanamadı (indirim hiç değişmedi) |
| Watch Dogs 2 | 3 | – | hesaplanamadı (indirim hiç değişmedi) |

> r ≈ +1: indirim arttıkça oyuncu artıyor · r ≈ 0: ilişki yok · r ≈ −1: ters ilişki. Korelasyon nedensellik değildir; birkaç günlük veriyle sonuç güvenilir olmaz.
