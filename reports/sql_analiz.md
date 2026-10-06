# 🔎 SQL Analizi

_Otomatik üretildi: 06.10.2026 14:55 UTC · sorgular: [`queries.sql`](../queries.sql)_

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
| Rainbow Six Siege | 2026-10-06 | 48,915 | -12.6 |
| Rainbow Six Siege | 2026-10-05 | 55,958 | 3.7 |
| Rainbow Six Siege | 2026-10-03 | 53,977 | -21.5 |
| Rainbow Six Siege | 2026-10-02 | 68,763 | – |
| Star Wars Battlefront II | 2026-10-06 | 747 | -30.3 |
| Star Wars Battlefront II | 2026-10-05 | 1,072 | 16 |
| Star Wars Battlefront II | 2026-10-03 | 924 | -6.7 |
| Star Wars Battlefront II | 2026-10-02 | 990 | – |
| Titanfall 2 | 2026-10-06 | 1,898 | -10.9 |
| Titanfall 2 | 2026-10-05 | 2,129 | -9.9 |
| Titanfall 2 | 2026-10-03 | 2,363 | 97.2 |
| Titanfall 2 | 2026-10-02 | 1,198 | – |
| Watch Dogs | 2026-10-06 | 1,519 | -26 |
| Watch Dogs | 2026-10-05 | 2,052 | 13.2 |
| Watch Dogs | 2026-10-03 | 1,812 | 31.3 |
| Watch Dogs | 2026-10-02 | 1,380 | – |
| Watch Dogs 2 | 2026-10-06 | 5,525 | -21 |
| Watch Dogs 2 | 2026-10-05 | 6,991 | 2.2 |
| Watch Dogs 2 | 2026-10-03 | 6,841 | 170.3 |
| Watch Dogs 2 | 2026-10-02 | 2,531 | – |

## 3. Her ölçümde oyunların sıralaması (son 5 ölçüm) — DENSE_RANK

| zaman_utc | oyun | oyuncu | sira |
|---|---|---|---|
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
| 2026-10-05T18:11:07+00:00 | Rainbow Six Siege | 64,385 | 1 |
| 2026-10-05T18:11:07+00:00 | Watch Dogs 2 | 5,362 | 2 |
| 2026-10-05T18:11:07+00:00 | Watch Dogs | 2,045 | 3 |
| 2026-10-05T18:11:07+00:00 | Titanfall 2 | 1,698 | 4 |
| 2026-10-05T18:11:07+00:00 | Star Wars Battlefront II | 1,307 | 5 |
| 2026-10-05T14:26:14+00:00 | Rainbow Six Siege | 47,531 | 1 |
| 2026-10-05T14:26:14+00:00 | Watch Dogs 2 | 8,619 | 2 |
| 2026-10-05T14:26:14+00:00 | Titanfall 2 | 2,559 | 3 |
| 2026-10-05T14:26:14+00:00 | Watch Dogs | 2,059 | 4 |
| 2026-10-05T14:26:14+00:00 | Star Wars Battlefront II | 836 | 5 |

## 4. Oynaklık: hangi oyunun oyuncu sayısı en çok dalgalanıyor? (max-min / ortalama)

| oyun | min | max | ort | dalga_yuzde |
|---|---|---|---|---|
| Watch Dogs 2 | 2,396 | 8,619 | 5,846 | 106.5 |
| Star Wars Battlefront II | 462 | 1,307 | 903 | 93.6 |
| Rainbow Six Siege | 29,614 | 68,763 | 54,422 | 71.9 |
| Titanfall 2 | 1,198 | 2,559 | 1,984 | 68.6 |
| Watch Dogs | 1,233 | 2,084 | 1,708 | 49.8 |

## 5. Hafta içi vs hafta sonu ortalaması

| oyun | hafta_sonu | hafta_ici |
|---|---|---|
| Rainbow Six Siege | 53,977 | 54,571 |
| Star Wars Battlefront II | 924 | 896 |
| Titanfall 2 | 2,363 | 1,858 |
| Watch Dogs | 1,812 | 1,674 |
| Watch Dogs 2 | 6,841 | 5,514 |

## 6. Mağaza verisi: fiyat, indirim, yorum puanı + anlık oyuncu (JOIN)

| oyun | anlik_oyuncu | fiyat | para_birimi | indirim_yuzde | toplam_yorum | olumlu_yuzde | steam_puani |
|---|---|---|---|---|---|---|---|
| Rainbow Six Siege | 48,494 | 0 | FREE | 0 | 1,559,893 | 82.1 | Very Positive |
| Watch Dogs 2 | 8,148 | 1.99 | USD | 95 | 104,286 | 82.1 | Very Positive |
| Titanfall 2 | 2,545 | 4.49 | USD | 85 | 287,685 | 95.7 | Overwhelmingly Positive |
| Watch Dogs | 2,084 | 1.59 | USD | 90 | 53,591 | 79.7 | Mostly Positive |
| Star Wars Battlefront II | 876 | 9.99 | USD | 75 | 100,305 | 88.3 | Very Positive |

## 7. İndirim etkisi: indirimli günlerde oyuncu sayısı artıyor mu? (JOIN + koşullu AVG)

| oyun | indirimli_gun | normal_gun | max_indirim_yuzde | ort_indirimli | ort_normal | fark_yuzde |
|---|---|---|---|---|---|---|
| Watch Dogs 2 | 2 | 0 | 95 | 6,258 | – | – |
| Watch Dogs | 2 | 0 | 90 | 1,786 | – | – |
| Titanfall 2 | 2 | 0 | 85 | 2,013 | – | – |
| Star Wars Battlefront II | 2 | 0 | 75 | 909 | – | – |
| Rainbow Six Siege | 0 | 2 | 0 | – | 52,437 | – |

## 8. İndirim × oyuncu sayısı korelasyonu (Pearson r, Python)

| oyun | gun_sayisi | pearson_r | yorum |
|---|---|---|---|
| Rainbow Six Siege | 2 | – | hesaplanamadı (en az 3 günlük mağaza verisi gerekli) |
| Star Wars Battlefront II | 2 | – | hesaplanamadı (en az 3 günlük mağaza verisi gerekli) |
| Titanfall 2 | 2 | – | hesaplanamadı (en az 3 günlük mağaza verisi gerekli) |
| Watch Dogs | 2 | – | hesaplanamadı (en az 3 günlük mağaza verisi gerekli) |
| Watch Dogs 2 | 2 | – | hesaplanamadı (en az 3 günlük mağaza verisi gerekli) |

> r ≈ +1: indirim arttıkça oyuncu artıyor · r ≈ 0: ilişki yok · r ≈ −1: ters ilişki. Korelasyon nedensellik değildir; birkaç günlük veriyle sonuç güvenilir olmaz.
