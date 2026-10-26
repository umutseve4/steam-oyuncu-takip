# 🔎 SQL Analizi

_Otomatik üretildi: 26.10.2026 10:52 UTC · sorgular: [`queries.sql`](../queries.sql)_

## 1. Her oyunun en kalabalık olduğu saat (UTC, ortalamaya göre)

| oyun | zirve_saat_utc | zirve_saat_tr | ort_oyuncu | olcum |
|---|---|---|---|---|
| Rainbow Six Siege | 20:00 | 23:00 | 78,514 | 8 |
| Watch Dogs 2 | 15:00 | 18:00 | 5,577 | 4 |
| Titanfall 2 | 13:00 | 16:00 | 2,013 | 3 |
| Watch Dogs | 15:00 | 18:00 | 1,836 | 4 |
| Star Wars Battlefront II | 18:00 | 21:00 | 1,486 | 6 |

## 2. Günlük ortalama ve günlük değişim (%) — LAG window function

| oyun | gun | gunluk_ort | degisim_yuzde |
|---|---|---|---|
| Rainbow Six Siege | 2026-10-26 | 37,851 | -45.7 |
| Rainbow Six Siege | 2026-10-25 | 69,753 | 4.5 |
| Rainbow Six Siege | 2026-10-24 | 66,776 | 18.2 |
| Rainbow Six Siege | 2026-10-23 | 56,497 | 9 |
| Rainbow Six Siege | 2026-10-22 | 51,832 | 0.8 |
| Rainbow Six Siege | 2026-10-21 | 51,423 | -1.5 |
| Rainbow Six Siege | 2026-10-20 | 52,203 | -9.7 |
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
| Star Wars Battlefront II | 2026-10-26 | 715 | -53.2 |
| Star Wars Battlefront II | 2026-10-25 | 1,527 | 7.2 |
| Star Wars Battlefront II | 2026-10-24 | 1,425 | 25.3 |
| Star Wars Battlefront II | 2026-10-23 | 1,137 | 21.9 |
| Star Wars Battlefront II | 2026-10-22 | 933 | 7.1 |
| Star Wars Battlefront II | 2026-10-21 | 871 | 11.1 |
| Star Wars Battlefront II | 2026-10-20 | 784 | -0.4 |
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
| Titanfall 2 | 2026-10-26 | 932 | -30.7 |
| Titanfall 2 | 2026-10-25 | 1,345 | -3.3 |

## 3. Her ölçümde oyunların sıralaması (son 5 ölçüm) — DENSE_RANK

| zaman_utc | oyun | oyuncu | sira |
|---|---|---|---|
| 2026-10-26T10:52:28+00:00 | Rainbow Six Siege | 29,127 | 1 |
| 2026-10-26T10:52:28+00:00 | Watch Dogs 2 | 1,999 | 2 |
| 2026-10-26T10:52:28+00:00 | Titanfall 2 | 970 | 3 |
| 2026-10-26T10:52:28+00:00 | Star Wars Battlefront II | 662 | 4 |
| 2026-10-26T10:52:28+00:00 | Watch Dogs | 545 | 5 |
| 2026-10-26T04:32:18+00:00 | Rainbow Six Siege | 46,575 | 1 |
| 2026-10-26T04:32:18+00:00 | Watch Dogs 2 | 1,321 | 2 |
| 2026-10-26T04:32:18+00:00 | Titanfall 2 | 894 | 3 |
| 2026-10-26T04:32:18+00:00 | Star Wars Battlefront II | 768 | 4 |
| 2026-10-26T04:32:18+00:00 | Watch Dogs | 456 | 5 |
| 2026-10-25T23:58:33+00:00 | Rainbow Six Siege | 77,729 | 1 |
| 2026-10-25T23:58:33+00:00 | Star Wars Battlefront II | 1,436 | 2 |
| 2026-10-25T23:58:33+00:00 | Watch Dogs 2 | 1,064 | 3 |
| 2026-10-25T23:58:33+00:00 | Titanfall 2 | 886 | 4 |
| 2026-10-25T23:58:33+00:00 | Watch Dogs | 619 | 5 |
| 2026-10-25T21:33:46+00:00 | Rainbow Six Siege | 84,054 | 1 |
| 2026-10-25T21:33:46+00:00 | Star Wars Battlefront II | 1,793 | 2 |
| 2026-10-25T21:33:46+00:00 | Watch Dogs 2 | 1,399 | 3 |
| 2026-10-25T21:33:46+00:00 | Titanfall 2 | 1,096 | 4 |
| 2026-10-25T21:33:46+00:00 | Watch Dogs | 792 | 5 |
| 2026-10-25T18:16:43+00:00 | Rainbow Six Siege | 82,657 | 1 |
| 2026-10-25T18:16:43+00:00 | Star Wars Battlefront II | 2,156 | 2 |
| 2026-10-25T18:16:43+00:00 | Watch Dogs 2 | 2,061 | 3 |
| 2026-10-25T18:16:43+00:00 | Titanfall 2 | 1,249 | 4 |
| 2026-10-25T18:16:43+00:00 | Watch Dogs | 1,084 | 5 |

## 4. Oynaklık: hangi oyunun oyuncu sayısı en çok dalgalanıyor? (max-min / ortalama)

| oyun | min | max | ort | dalga_yuzde |
|---|---|---|---|---|
| Watch Dogs 2 | 899 | 8,619 | 2,939 | 262.7 |
| Star Wars Battlefront II | 398 | 2,156 | 1,002 | 175.4 |
| Watch Dogs | 456 | 2,131 | 1,076 | 155.7 |
| Titanfall 2 | 698 | 2,760 | 1,340 | 153.9 |
| Rainbow Six Siege | 26,086 | 91,821 | 59,096 | 111.2 |

## 5. Hafta içi vs hafta sonu ortalaması

| oyun | hafta_sonu | hafta_ici |
|---|---|---|
| Rainbow Six Siege | 67,927 | 54,360 |
| Star Wars Battlefront II | 1,237 | 876 |
| Titanfall 2 | 1,580 | 1,211 |
| Watch Dogs | 1,196 | 1,011 |
| Watch Dogs 2 | 3,286 | 2,753 |

## 6. Mağaza verisi: fiyat, indirim, yorum puanı + anlık oyuncu (JOIN)

| oyun | anlik_oyuncu | fiyat | para_birimi | indirim_yuzde | toplam_yorum | olumlu_yuzde | steam_puani |
|---|---|---|---|---|---|---|---|
| Rainbow Six Siege | 29,127 | 0 | FREE | 0 | – | – | – |
| Watch Dogs 2 | 1,999 | 39.99 | USD | 0 | – | – | – |
| Titanfall 2 | 970 | 29.99 | USD | 0 | – | – | – |
| Star Wars Battlefront II | 662 | 39.99 | USD | 0 | – | – | – |
| Watch Dogs | 545 | 15.99 | USD | 0 | – | – | – |

## 7. İndirim etkisi: indirimli günlerde oyuncu sayısı artıyor mu? (JOIN + koşullu AVG)

| oyun | indirimli_gun | normal_gun | max_indirim_yuzde | ort_indirimli | ort_normal | fark_yuzde |
|---|---|---|---|---|---|---|
| Watch Dogs 2 | 4 | 18 | 95 | 5,047 | 2,567 | 96.6 |
| Watch Dogs | 4 | 18 | 90 | 1,603 | 983 | 63 |
| Titanfall 2 | 4 | 18 | 85 | 1,741 | 1,249 | 39.4 |
| Star Wars Battlefront II | 4 | 18 | 75 | 913 | 994 | -8.1 |
| Rainbow Six Siege | 0 | 22 | 0 | – | 57,770 | – |

## 8. İndirim × oyuncu sayısı korelasyonu (Pearson r, Python)

| oyun | gun_sayisi | pearson_r | yorum |
|---|---|---|---|
| Rainbow Six Siege | 22 | – | hesaplanamadı (indirim hiç değişmedi) |
| Star Wars Battlefront II | 22 | -0.149 | çok zayıf negatif |
| Titanfall 2 | 22 | +0.568 | orta pozitif |
| Watch Dogs | 22 | +0.632 | güçlü pozitif |
| Watch Dogs 2 | 22 | +0.738 | güçlü pozitif |

> r ≈ +1: indirim arttıkça oyuncu artıyor · r ≈ 0: ilişki yok · r ≈ −1: ters ilişki. Korelasyon nedensellik değildir; birkaç günlük veriyle sonuç güvenilir olmaz.
