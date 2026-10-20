# 🔎 SQL Analizi

_Otomatik üretildi: 20.10.2026 00:10 UTC · sorgular: [`queries.sql`](../queries.sql)_

## 1. Her oyunun en kalabalık olduğu saat (UTC, ortalamaya göre)

| oyun | zirve_saat_utc | zirve_saat_tr | ort_oyuncu | olcum |
|---|---|---|---|---|
| Rainbow Six Siege | 19:00 | 22:00 | 88,045 | 1 |
| Watch Dogs 2 | 14:00 | 17:00 | 6,398 | 4 |
| Titanfall 2 | 04:00 | 07:00 | 2,221 | 1 |
| Watch Dogs | 15:00 | 18:00 | 1,836 | 4 |
| Star Wars Battlefront II | 19:00 | 22:00 | 1,468 | 1 |

## 2. Günlük ortalama ve günlük değişim (%) — LAG window function

| oyun | gun | gunluk_ort | degisim_yuzde |
|---|---|---|---|
| Rainbow Six Siege | 2026-10-20 | 68,024 | 17.6 |
| Rainbow Six Siege | 2026-10-19 | 57,819 | -18.8 |
| Rainbow Six Siege | 2026-10-18 | 71,219 | 2.3 |
| Rainbow Six Siege | 2026-10-17 | 69,613 | 15 |
| Rainbow Six Siege | 2026-10-16 | 60,516 | 11.3 |
| Rainbow Six Siege | 2026-10-15 | 54,362 | 3.6 |
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
| Star Wars Battlefront II | 2026-10-20 | 867 | 10.2 |
| Star Wars Battlefront II | 2026-10-19 | 787 | -27.6 |
| Star Wars Battlefront II | 2026-10-18 | 1,087 | -0.9 |
| Star Wars Battlefront II | 2026-10-17 | 1,097 | 30 |
| Star Wars Battlefront II | 2026-10-16 | 844 | 8.8 |
| Star Wars Battlefront II | 2026-10-15 | 776 | -4.4 |
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
| Titanfall 2 | 2026-10-20 | 777 | -29 |
| Titanfall 2 | 2026-10-19 | 1,094 | -24.4 |
| Titanfall 2 | 2026-10-18 | 1,447 | -13.4 |
| Titanfall 2 | 2026-10-17 | 1,671 | 47.9 |
| Titanfall 2 | 2026-10-16 | 1,130 | 7.1 |
| Titanfall 2 | 2026-10-15 | 1,055 | -2 |
| Titanfall 2 | 2026-10-14 | 1,076 | -1.2 |
| Titanfall 2 | 2026-10-13 | 1,089 | -4.3 |
| Titanfall 2 | 2026-10-12 | 1,138 | -36.7 |
| Titanfall 2 | 2026-10-11 | 1,798 | 4.8 |
| Titanfall 2 | 2026-10-10 | 1,715 | 8.6 |
| Titanfall 2 | 2026-10-09 | 1,579 | 10.2 |
| Titanfall 2 | 2026-10-08 | 1,433 | -11.5 |
| Titanfall 2 | 2026-10-07 | 1,620 | -9 |

## 3. Her ölçümde oyunların sıralaması (son 5 ölçüm) — DENSE_RANK

| zaman_utc | oyun | oyuncu | sira |
|---|---|---|---|
| 2026-10-20T00:10:12+00:00 | Rainbow Six Siege | 68,024 | 1 |
| 2026-10-20T00:10:12+00:00 | Watch Dogs 2 | 1,006 | 2 |
| 2026-10-20T00:10:12+00:00 | Star Wars Battlefront II | 867 | 3 |
| 2026-10-20T00:10:12+00:00 | Titanfall 2 | 777 | 4 |
| 2026-10-20T00:10:12+00:00 | Watch Dogs | 607 | 5 |
| 2026-10-19T20:27:50+00:00 | Rainbow Six Siege | 70,527 | 1 |
| 2026-10-19T20:27:50+00:00 | Watch Dogs 2 | 1,511 | 2 |
| 2026-10-19T20:27:50+00:00 | Star Wars Battlefront II | 986 | 3 |
| 2026-10-19T20:27:50+00:00 | Titanfall 2 | 928 | 4 |
| 2026-10-19T20:27:50+00:00 | Watch Dogs | 809 | 5 |
| 2026-10-19T14:29:10+00:00 | Rainbow Six Siege | 49,414 | 1 |
| 2026-10-19T14:29:10+00:00 | Watch Dogs 2 | 3,966 | 2 |
| 2026-10-19T14:29:10+00:00 | Titanfall 2 | 1,677 | 3 |
| 2026-10-19T14:29:10+00:00 | Watch Dogs | 1,099 | 4 |
| 2026-10-19T14:29:10+00:00 | Star Wars Battlefront II | 784 | 5 |
| 2026-10-19T06:00:34+00:00 | Rainbow Six Siege | 35,319 | 1 |
| 2026-10-19T06:00:34+00:00 | Watch Dogs 2 | 1,674 | 2 |
| 2026-10-19T06:00:34+00:00 | Titanfall 2 | 847 | 3 |
| 2026-10-19T06:00:34+00:00 | Watch Dogs | 554 | 4 |
| 2026-10-19T06:00:34+00:00 | Star Wars Battlefront II | 483 | 5 |
| 2026-10-19T00:58:23+00:00 | Rainbow Six Siege | 76,017 | 1 |
| 2026-10-19T00:58:23+00:00 | Watch Dogs 2 | 1,248 | 2 |
| 2026-10-19T00:58:23+00:00 | Titanfall 2 | 924 | 3 |
| 2026-10-19T00:58:23+00:00 | Star Wars Battlefront II | 895 | 4 |
| 2026-10-19T00:58:23+00:00 | Watch Dogs | 717 | 5 |

## 4. Oynaklık: hangi oyunun oyuncu sayısı en çok dalgalanıyor? (max-min / ortalama)

| oyun | min | max | ort | dalga_yuzde |
|---|---|---|---|---|
| Watch Dogs 2 | 1,006 | 8,619 | 3,366 | 226.2 |
| Titanfall 2 | 777 | 2,760 | 1,438 | 137.9 |
| Star Wars Battlefront II | 398 | 1,623 | 945 | 129.6 |
| Watch Dogs | 554 | 2,131 | 1,226 | 128.6 |
| Rainbow Six Siege | 26,086 | 91,821 | 59,980 | 109.6 |

## 5. Hafta içi vs hafta sonu ortalaması

| oyun | hafta_sonu | hafta_ici |
|---|---|---|
| Rainbow Six Siege | 67,806 | 55,983 |
| Star Wars Battlefront II | 1,110 | 861 |
| Titanfall 2 | 1,694 | 1,308 |
| Watch Dogs | 1,360 | 1,157 |
| Watch Dogs 2 | 3,791 | 3,149 |

## 6. Mağaza verisi: fiyat, indirim, yorum puanı + anlık oyuncu (JOIN)

| oyun | anlik_oyuncu | fiyat | para_birimi | indirim_yuzde | toplam_yorum | olumlu_yuzde | steam_puani |
|---|---|---|---|---|---|---|---|
| Rainbow Six Siege | 68,024 | 0 | FREE | 0 | 1,564,084 | 82.1 | Very Positive |
| Watch Dogs 2 | 1,006 | 39.99 | USD | 0 | 105,403 | 82.1 | Very Positive |
| Star Wars Battlefront II | 867 | 39.99 | USD | 0 | 100,500 | 88.3 | Very Positive |
| Titanfall 2 | 777 | 29.99 | USD | 0 | 288,567 | 95.7 | Overwhelmingly Positive |
| Watch Dogs | 607 | 15.99 | USD | 0 | 54,095 | 79.8 | Mostly Positive |

## 7. İndirim etkisi: indirimli günlerde oyuncu sayısı artıyor mu? (JOIN + koşullu AVG)

| oyun | indirimli_gun | normal_gun | max_indirim_yuzde | ort_indirimli | ort_normal | fark_yuzde |
|---|---|---|---|---|---|---|
| Watch Dogs 2 | 4 | 12 | 95 | 5,047 | 2,771 | 82.1 |
| Watch Dogs | 4 | 12 | 90 | 1,603 | 1,097 | 46.1 |
| Titanfall 2 | 4 | 12 | 85 | 1,741 | 1,297 | 34.2 |
| Star Wars Battlefront II | 4 | 12 | 75 | 913 | 948 | -3.6 |
| Rainbow Six Siege | 0 | 16 | 0 | – | 59,540 | – |

## 8. İndirim × oyuncu sayısı korelasyonu (Pearson r, Python)

| oyun | gun_sayisi | pearson_r | yorum |
|---|---|---|---|
| Rainbow Six Siege | 16 | – | hesaplanamadı (indirim hiç değişmedi) |
| Star Wars Battlefront II | 16 | -0.107 | çok zayıf negatif |
| Titanfall 2 | 16 | +0.538 | orta pozitif |
| Watch Dogs | 16 | +0.605 | güçlü pozitif |
| Watch Dogs 2 | 16 | +0.703 | güçlü pozitif |

> r ≈ +1: indirim arttıkça oyuncu artıyor · r ≈ 0: ilişki yok · r ≈ −1: ters ilişki. Korelasyon nedensellik değildir; birkaç günlük veriyle sonuç güvenilir olmaz.
