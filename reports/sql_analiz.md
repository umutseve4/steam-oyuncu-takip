# 🔎 SQL Analizi

_Otomatik üretildi: 05.10.2026 18:11 UTC · sorgular: [`queries.sql`](../queries.sql)_

## 1. Her oyunun en kalabalık olduğu saat (UTC, ortalamaya göre)

| oyun | zirve_saat_utc | zirve_saat_tr | ort_oyuncu | olcum |
|---|---|---|---|---|
| Rainbow Six Siege | 23:00 | 02:00 | 68,763 | 1 |
| Watch Dogs 2 | 14:00 | 17:00 | 8,619 | 1 |
| Titanfall 2 | 14:00 | 17:00 | 2,559 | 1 |
| Watch Dogs | 14:00 | 17:00 | 2,059 | 1 |
| Star Wars Battlefront II | 18:00 | 21:00 | 1,307 | 1 |

## 2. Günlük ortalama ve günlük değişim (%) — LAG window function

| oyun | gun | gunluk_ort | degisim_yuzde |
|---|---|---|---|
| Rainbow Six Siege | 2026-10-05 | 55,958 | 3.7 |
| Rainbow Six Siege | 2026-10-03 | 53,977 | -21.5 |
| Rainbow Six Siege | 2026-10-02 | 68,763 | – |
| Star Wars Battlefront II | 2026-10-05 | 1,072 | 16 |
| Star Wars Battlefront II | 2026-10-03 | 924 | -6.7 |
| Star Wars Battlefront II | 2026-10-02 | 990 | – |
| Titanfall 2 | 2026-10-05 | 2,129 | -9.9 |
| Titanfall 2 | 2026-10-03 | 2,363 | 97.2 |
| Titanfall 2 | 2026-10-02 | 1,198 | – |
| Watch Dogs | 2026-10-05 | 2,052 | 13.2 |
| Watch Dogs | 2026-10-03 | 1,812 | 31.3 |
| Watch Dogs | 2026-10-02 | 1,380 | – |
| Watch Dogs 2 | 2026-10-05 | 6,991 | 2.2 |
| Watch Dogs 2 | 2026-10-03 | 6,841 | 170.3 |
| Watch Dogs 2 | 2026-10-02 | 2,531 | – |

## 3. Her ölçümde oyunların sıralaması (son 5 ölçüm) — DENSE_RANK

| zaman_utc | oyun | oyuncu | sira |
|---|---|---|---|
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
| 2026-10-03T10:17:14+00:00 | Rainbow Six Siege | 40,971 | 1 |
| 2026-10-03T10:17:14+00:00 | Watch Dogs 2 | 7,887 | 2 |
| 2026-10-03T10:17:14+00:00 | Titanfall 2 | 2,505 | 3 |
| 2026-10-03T10:17:14+00:00 | Watch Dogs | 1,977 | 4 |
| 2026-10-03T10:17:14+00:00 | Star Wars Battlefront II | 903 | 5 |
| 2026-10-03T04:41:41+00:00 | Rainbow Six Siege | 66,983 | 1 |
| 2026-10-03T04:41:41+00:00 | Watch Dogs 2 | 5,794 | 2 |
| 2026-10-03T04:41:41+00:00 | Titanfall 2 | 2,221 | 3 |
| 2026-10-03T04:41:41+00:00 | Watch Dogs | 1,646 | 4 |
| 2026-10-03T04:41:41+00:00 | Star Wars Battlefront II | 945 | 5 |
| 2026-10-02T23:38:31+00:00 | Rainbow Six Siege | 68,763 | 1 |
| 2026-10-02T23:38:31+00:00 | Watch Dogs 2 | 2,531 | 2 |
| 2026-10-02T23:38:31+00:00 | Watch Dogs | 1,380 | 3 |
| 2026-10-02T23:38:31+00:00 | Titanfall 2 | 1,198 | 4 |
| 2026-10-02T23:38:31+00:00 | Star Wars Battlefront II | 990 | 5 |

## 4. Oynaklık: hangi oyunun oyuncu sayısı en çok dalgalanıyor? (max-min / ortalama)

| oyun | min | max | ort | dalga_yuzde |
|---|---|---|---|---|
| Watch Dogs 2 | 2,531 | 8,619 | 6,039 | 100.8 |
| Titanfall 2 | 1,198 | 2,559 | 2,036 | 66.8 |
| Rainbow Six Siege | 40,971 | 68,763 | 57,727 | 48.1 |
| Star Wars Battlefront II | 836 | 1,307 | 996 | 47.3 |
| Watch Dogs | 1,380 | 2,059 | 1,821 | 37.3 |

## 5. Hafta içi vs hafta sonu ortalaması

| oyun | hafta_sonu | hafta_ici |
|---|---|---|
| Rainbow Six Siege | 53,977 | 60,226 |
| Star Wars Battlefront II | 924 | 1,044 |
| Titanfall 2 | 2,363 | 1,818 |
| Watch Dogs | 1,812 | 1,828 |
| Watch Dogs 2 | 6,841 | 5,504 |

## 6. Mağaza verisi: fiyat, indirim, yorum puanı + anlık oyuncu (JOIN)

| oyun | anlik_oyuncu | fiyat | para_birimi | indirim_yuzde | toplam_yorum | olumlu_yuzde | steam_puani |
|---|---|---|---|---|---|---|---|
| Rainbow Six Siege | 64,385 | 0 | FREE | 0 | 1,559,753 | 82.1 | Very Positive |
| Watch Dogs 2 | 5,362 | 1.99 | USD | 95 | 104,229 | 82.1 | Very Positive |
| Watch Dogs | 2,045 | 1.59 | USD | 90 | 53,574 | 79.7 | Mostly Positive |
| Titanfall 2 | 1,698 | 4.49 | USD | 85 | 287,637 | 95.7 | Overwhelmingly Positive |
| Star Wars Battlefront II | 1,307 | 9.99 | USD | 75 | 100,305 | 88.3 | Very Positive |

## 7. İndirim etkisi: indirimli günlerde oyuncu sayısı artıyor mu? (JOIN + koşullu AVG)

| oyun | indirimli_gun | normal_gun | max_indirim_yuzde | ort_indirimli | ort_normal | fark_yuzde |
|---|---|---|---|---|---|---|
| Watch Dogs 2 | 1 | 0 | 95 | 6,991 | – | – |
| Watch Dogs | 1 | 0 | 90 | 2,052 | – | – |
| Titanfall 2 | 1 | 0 | 85 | 2,129 | – | – |
| Star Wars Battlefront II | 1 | 0 | 75 | 1,072 | – | – |
| Rainbow Six Siege | 0 | 1 | 0 | – | 55,958 | – |

## 8. İndirim × oyuncu sayısı korelasyonu (Pearson r, Python)

| oyun | gun_sayisi | pearson_r | yorum |
|---|---|---|---|
| Rainbow Six Siege | 1 | – | hesaplanamadı (en az 3 günlük mağaza verisi gerekli) |
| Star Wars Battlefront II | 1 | – | hesaplanamadı (en az 3 günlük mağaza verisi gerekli) |
| Titanfall 2 | 1 | – | hesaplanamadı (en az 3 günlük mağaza verisi gerekli) |
| Watch Dogs | 1 | – | hesaplanamadı (en az 3 günlük mağaza verisi gerekli) |
| Watch Dogs 2 | 1 | – | hesaplanamadı (en az 3 günlük mağaza verisi gerekli) |

> r ≈ +1: indirim arttıkça oyuncu artıyor · r ≈ 0: ilişki yok · r ≈ −1: ters ilişki. Korelasyon nedensellik değildir; birkaç günlük veriyle sonuç güvenilir olmaz.
