# 🔎 SQL Analizi

_Otomatik üretildi: 28.10.2026 04:59 UTC · sorgular: [`queries.sql`](../queries.sql)_

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
| Rainbow Six Siege | 2026-10-28 | 41,817 | -25.3 |
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
| Rainbow Six Siege | 2026-10-08 | 52,254 | -0.1 |
| Rainbow Six Siege | 2026-10-07 | 52,319 | -1.9 |
| Rainbow Six Siege | 2026-10-06 | 53,345 | -4.7 |
| Rainbow Six Siege | 2026-10-05 | 55,958 | 3.7 |
| Rainbow Six Siege | 2026-10-03 | 53,977 | -21.5 |
| Rainbow Six Siege | 2026-10-02 | 68,763 | – |
| Star Wars Battlefront II | 2026-10-28 | 740 | -30.6 |
| Star Wars Battlefront II | 2026-10-27 | 1,066 | 6.8 |
| Star Wars Battlefront II | 2026-10-26 | 998 | -34.6 |
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

## 3. Her ölçümde oyunların sıralaması (son 5 ölçüm) — DENSE_RANK

| zaman_utc | oyun | oyuncu | sira |
|---|---|---|---|
| 2026-10-28T04:57:23+00:00 | Rainbow Six Siege | 41,817 | 1 |
| 2026-10-28T04:57:23+00:00 | Watch Dogs 2 | 1,436 | 2 |
| 2026-10-28T04:57:23+00:00 | Titanfall 2 | 858 | 3 |
| 2026-10-28T04:57:23+00:00 | Star Wars Battlefront II | 740 | 4 |
| 2026-10-28T04:57:23+00:00 | Watch Dogs | 434 | 5 |
| 2026-10-27T23:41:37+00:00 | Rainbow Six Siege | 69,236 | 1 |
| 2026-10-27T23:41:37+00:00 | Star Wars Battlefront II | 1,247 | 2 |
| 2026-10-27T23:41:37+00:00 | Watch Dogs 2 | 905 | 3 |
| 2026-10-27T23:41:37+00:00 | Titanfall 2 | 715 | 4 |
| 2026-10-27T23:41:37+00:00 | Watch Dogs | 513 | 5 |
| 2026-10-27T19:57:09+00:00 | Rainbow Six Siege | 67,920 | 1 |
| 2026-10-27T19:57:09+00:00 | Star Wars Battlefront II | 1,514 | 2 |
| 2026-10-27T19:57:09+00:00 | Watch Dogs 2 | 1,247 | 3 |
| 2026-10-27T19:57:09+00:00 | Titanfall 2 | 867 | 4 |
| 2026-10-27T19:57:09+00:00 | Watch Dogs | 675 | 5 |
| 2026-10-27T14:13:52+00:00 | Rainbow Six Siege | 47,212 | 1 |
| 2026-10-27T14:13:52+00:00 | Watch Dogs 2 | 3,088 | 2 |
| 2026-10-27T14:13:52+00:00 | Titanfall 2 | 1,510 | 3 |
| 2026-10-27T14:13:52+00:00 | Star Wars Battlefront II | 890 | 4 |
| 2026-10-27T14:13:52+00:00 | Watch Dogs | 848 | 5 |
| 2026-10-27T07:34:10+00:00 | Rainbow Six Siege | 26,382 | 1 |
| 2026-10-27T07:34:10+00:00 | Watch Dogs 2 | 1,338 | 2 |
| 2026-10-27T07:34:10+00:00 | Titanfall 2 | 662 | 3 |
| 2026-10-27T07:34:10+00:00 | Star Wars Battlefront II | 475 | 4 |
| 2026-10-27T07:34:10+00:00 | Watch Dogs | 428 | 5 |

## 4. Oynaklık: hangi oyunun oyuncu sayısı en çok dalgalanıyor? (max-min / ortalama)

| oyun | min | max | ort | dalga_yuzde |
|---|---|---|---|---|
| Watch Dogs 2 | 899 | 8,619 | 2,834 | 272.4 |
| Star Wars Battlefront II | 398 | 2,156 | 1,008 | 174.5 |
| Watch Dogs | 428 | 2,131 | 1,041 | 163.5 |
| Titanfall 2 | 662 | 2,760 | 1,307 | 160.5 |
| Rainbow Six Siege | 26,086 | 91,821 | 58,838 | 111.7 |

## 5. Hafta içi vs hafta sonu ortalaması

| oyun | hafta_sonu | hafta_ici |
|---|---|---|
| Rainbow Six Siege | 67,927 | 54,470 |
| Star Wars Battlefront II | 1,237 | 897 |
| Titanfall 2 | 1,580 | 1,175 |
| Watch Dogs | 1,196 | 967 |
| Watch Dogs 2 | 3,286 | 2,617 |

## 6. Mağaza verisi: fiyat, indirim, yorum puanı + anlık oyuncu (JOIN)

| oyun | anlik_oyuncu | fiyat | para_birimi | indirim_yuzde | toplam_yorum | olumlu_yuzde | steam_puani |
|---|---|---|---|---|---|---|---|
| Rainbow Six Siege | 41,817 | 0 | FREE | 0 | – | – | – |
| Watch Dogs 2 | 1,436 | 39.99 | USD | 0 | – | – | – |
| Titanfall 2 | 858 | 29.99 | USD | 0 | – | – | – |
| Star Wars Battlefront II | 740 | 39.99 | USD | 0 | – | – | – |
| Watch Dogs | 434 | 15.99 | USD | 0 | – | – | – |

## 7. İndirim etkisi: indirimli günlerde oyuncu sayısı artıyor mu? (JOIN + koşullu AVG)

| oyun | indirimli_gun | normal_gun | max_indirim_yuzde | ort_indirimli | ort_normal | fark_yuzde |
|---|---|---|---|---|---|---|
| Watch Dogs 2 | 4 | 20 | 95 | 5,047 | 2,449 | 106.1 |
| Watch Dogs | 4 | 20 | 90 | 1,603 | 940 | 70.5 |
| Titanfall 2 | 4 | 20 | 85 | 1,741 | 1,209 | 44 |
| Star Wars Battlefront II | 4 | 20 | 75 | 913 | 999 | -8.6 |
| Rainbow Six Siege | 0 | 24 | 0 | – | 57,509 | – |

## 8. İndirim × oyuncu sayısı korelasyonu (Pearson r, Python)

| oyun | gun_sayisi | pearson_r | yorum |
|---|---|---|---|
| Rainbow Six Siege | 24 | – | hesaplanamadı (indirim hiç değişmedi) |
| Star Wars Battlefront II | 24 | -0.160 | çok zayıf negatif |
| Titanfall 2 | 24 | +0.571 | orta pozitif |
| Watch Dogs | 24 | +0.629 | güçlü pozitif |
| Watch Dogs 2 | 24 | +0.734 | güçlü pozitif |

> r ≈ +1: indirim arttıkça oyuncu artıyor · r ≈ 0: ilişki yok · r ≈ −1: ters ilişki. Korelasyon nedensellik değildir; birkaç günlük veriyle sonuç güvenilir olmaz.
