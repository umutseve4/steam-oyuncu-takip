# 🔎 SQL Analizi

_Otomatik üretildi: 27.11.2026 07:42 UTC · sorgular: [`queries.sql`](../queries.sql)_

## 1. Her oyunun en kalabalık olduğu saat (UTC, ortalamaya göre)

| oyun | zirve_saat_utc | zirve_saat_tr | ort_oyuncu | olcum |
|---|---|---|---|---|
| Rainbow Six Siege | 20:00 | 23:00 | 74,665 | 11 |
| Watch Dogs 2 | 15:00 | 18:00 | 5,075 | 5 |
| Titanfall 2 | 15:00 | 18:00 | 1,972 | 5 |
| Watch Dogs | 15:00 | 18:00 | 1,662 | 5 |
| Star Wars Battlefront II | 19:00 | 22:00 | 1,554 | 7 |

## 2. Günlük ortalama ve günlük değişim (%) — LAG window function

| oyun | gun | gunluk_ort | degisim_yuzde |
|---|---|---|---|
| Rainbow Six Siege | 2026-11-27 | 34,266 | -26.3 |
| Rainbow Six Siege | 2026-11-26 | 46,508 | -1.1 |
| Rainbow Six Siege | 2026-11-25 | 47,010 | 14.6 |
| Rainbow Six Siege | 2026-11-24 | 41,036 | -11.6 |
| Rainbow Six Siege | 2026-11-23 | 46,443 | -12.9 |
| Rainbow Six Siege | 2026-11-22 | 53,345 | 3.1 |
| Rainbow Six Siege | 2026-11-21 | 51,758 | 15.9 |
| Rainbow Six Siege | 2026-11-20 | 44,647 | -2.6 |
| Rainbow Six Siege | 2026-11-19 | 45,828 | -7.9 |
| Rainbow Six Siege | 2026-11-18 | 49,750 | -2.7 |
| Rainbow Six Siege | 2026-11-17 | 51,141 | -0.8 |
| Rainbow Six Siege | 2026-11-16 | 51,545 | -17 |
| Rainbow Six Siege | 2026-11-15 | 62,105 | 5.1 |
| Rainbow Six Siege | 2026-11-14 | 59,102 | 18.9 |
| Rainbow Six Siege | 2026-11-13 | 49,726 | 9 |
| Rainbow Six Siege | 2026-11-12 | 45,640 | -10.6 |
| Rainbow Six Siege | 2026-11-11 | 51,068 | 7.6 |
| Rainbow Six Siege | 2026-11-10 | 47,464 | -1.9 |
| Rainbow Six Siege | 2026-11-09 | 48,402 | -20.8 |
| Rainbow Six Siege | 2026-11-08 | 61,110 | -1.7 |
| Rainbow Six Siege | 2026-11-07 | 62,177 | 25.1 |
| Rainbow Six Siege | 2026-11-06 | 49,713 | 1.4 |
| Rainbow Six Siege | 2026-11-05 | 49,050 | 4 |
| Rainbow Six Siege | 2026-11-04 | 47,149 | -9 |
| Rainbow Six Siege | 2026-11-03 | 51,827 | -5.6 |
| Rainbow Six Siege | 2026-11-02 | 54,905 | -12.9 |
| Rainbow Six Siege | 2026-11-01 | 63,002 | 2.9 |
| Rainbow Six Siege | 2026-10-31 | 61,236 | 13.8 |
| Rainbow Six Siege | 2026-10-30 | 53,818 | 3.7 |
| Rainbow Six Siege | 2026-10-29 | 51,878 | 5.1 |
| Rainbow Six Siege | 2026-10-28 | 49,379 | -11.8 |
| Rainbow Six Siege | 2026-10-27 | 55,996 | 13.6 |
| Rainbow Six Siege | 2026-10-26 | 49,313 | -29.3 |
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

## 3. Her ölçümde oyunların sıralaması (son 5 ölçüm) — DENSE_RANK

| zaman_utc | oyun | oyuncu | sira |
|---|---|---|---|
| 2026-11-27T07:40:14+00:00 | Rainbow Six Siege | 34,266 | 1 |
| 2026-11-27T07:40:14+00:00 | Watch Dogs 2 | 2,109 | 2 |
| 2026-11-27T07:40:14+00:00 | Titanfall 2 | 1,735 | 3 |
| 2026-11-27T07:40:14+00:00 | Star Wars Battlefront II | 677 | 4 |
| 2026-11-27T07:40:14+00:00 | Watch Dogs | 564 | 5 |
| 2026-11-26T23:37:01+00:00 | Rainbow Six Siege | 46,859 | 1 |
| 2026-11-26T23:37:01+00:00 | Watch Dogs 2 | 1,424 | 2 |
| 2026-11-26T23:37:01+00:00 | Star Wars Battlefront II | 1,102 | 3 |
| 2026-11-26T23:37:01+00:00 | Titanfall 2 | 1,098 | 4 |
| 2026-11-26T23:37:01+00:00 | Watch Dogs | 672 | 5 |
| 2026-11-26T14:51:32+00:00 | Rainbow Six Siege | 40,552 | 1 |
| 2026-11-26T14:51:32+00:00 | Watch Dogs 2 | 3,809 | 2 |
| 2026-11-26T14:51:32+00:00 | Titanfall 2 | 2,518 | 3 |
| 2026-11-26T14:51:32+00:00 | Star Wars Battlefront II | 1,064 | 4 |
| 2026-11-26T14:51:32+00:00 | Watch Dogs | 1,018 | 5 |
| 2026-11-26T04:48:09+00:00 | Rainbow Six Siege | 52,112 | 1 |
| 2026-11-26T04:48:09+00:00 | Watch Dogs 2 | 2,065 | 2 |
| 2026-11-26T04:48:09+00:00 | Titanfall 2 | 1,772 | 3 |
| 2026-11-26T04:48:09+00:00 | Star Wars Battlefront II | 1,099 | 4 |
| 2026-11-26T04:48:09+00:00 | Watch Dogs | 614 | 5 |
| 2026-11-25T22:15:35+00:00 | Rainbow Six Siege | 57,280 | 1 |
| 2026-11-25T22:15:35+00:00 | Watch Dogs 2 | 1,604 | 2 |
| 2026-11-25T22:15:35+00:00 | Star Wars Battlefront II | 1,406 | 3 |
| 2026-11-25T22:15:35+00:00 | Titanfall 2 | 1,197 | 4 |
| 2026-11-25T22:15:35+00:00 | Watch Dogs | 765 | 5 |

## 4. Oynaklık: hangi oyunun oyuncu sayısı en çok dalgalanıyor? (max-min / ortalama)

| oyun | min | max | ort | dalga_yuzde |
|---|---|---|---|---|
| Watch Dogs 2 | 685 | 8,619 | 2,265 | 350.2 |
| Watch Dogs | 0 | 2,131 | 826 | 258.1 |
| Titanfall 2 | 628 | 2,760 | 1,230 | 173.3 |
| Star Wars Battlefront II | 398 | 2,156 | 1,035 | 169.9 |
| Rainbow Six Siege | 23,921 | 91,821 | 55,704 | 121.9 |

## 5. Hafta içi vs hafta sonu ortalaması

| oyun | hafta_sonu | hafta_ici |
|---|---|---|
| Rainbow Six Siege | 63,981 | 51,816 |
| Star Wars Battlefront II | 1,254 | 932 |
| Titanfall 2 | 1,499 | 1,105 |
| Watch Dogs | 972 | 757 |
| Watch Dogs 2 | 2,686 | 2,068 |

## 6. Mağaza verisi: fiyat, indirim, yorum puanı + anlık oyuncu (JOIN)

| oyun | anlik_oyuncu | fiyat | para_birimi | indirim_yuzde | toplam_yorum | olumlu_yuzde | steam_puani |
|---|---|---|---|---|---|---|---|
| Rainbow Six Siege | 34,266 | 0 | FREE | 0 | – | – | – |
| Watch Dogs 2 | 2,109 | 5.99 | USD | 85 | – | – | – |
| Titanfall 2 | 1,735 | 4.49 | USD | 85 | – | – | – |
| Star Wars Battlefront II | 677 | 7.99 | USD | 80 | – | – | – |
| Watch Dogs | 564 | 3.99 | USD | 75 | – | – | – |

## 7. İndirim etkisi: indirimli günlerde oyuncu sayısı artıyor mu? (JOIN + koşullu AVG)

| oyun | indirimli_gun | normal_gun | max_indirim_yuzde | ort_indirimli | ort_normal | fark_yuzde |
|---|---|---|---|---|---|---|
| Watch Dogs 2 | 13 | 41 | 95 | 3,180 | 1,904 | 67 |
| Titanfall 2 | 12 | 42 | 85 | 1,688 | 1,096 | 54 |
| Watch Dogs | 13 | 41 | 90 | 980 | 735 | 33.4 |
| Star Wars Battlefront II | 12 | 42 | 80 | 1,037 | 1,016 | 2 |
| Rainbow Six Siege | 0 | 54 | 0 | – | 54,082 | – |

## 8. İndirim × oyuncu sayısı korelasyonu (Pearson r, Python)

| oyun | gun_sayisi | pearson_r | yorum |
|---|---|---|---|
| Rainbow Six Siege | 54 | – | hesaplanamadı (indirim hiç değişmedi) |
| Star Wars Battlefront II | 54 | +0.054 | çok zayıf pozitif |
| Titanfall 2 | 54 | +0.682 | güçlü pozitif |
| Watch Dogs | 54 | +0.340 | zayıf pozitif |
| Watch Dogs 2 | 54 | +0.507 | orta pozitif |

> r ≈ +1: indirim arttıkça oyuncu artıyor · r ≈ 0: ilişki yok · r ≈ −1: ters ilişki. Korelasyon nedensellik değildir; birkaç günlük veriyle sonuç güvenilir olmaz.
