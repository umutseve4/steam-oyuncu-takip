# 🔎 SQL Analizi

_Otomatik üretildi: 23.10.2026 14:47 UTC · sorgular: [`queries.sql`](../queries.sql)_

## 1. Her oyunun en kalabalık olduğu saat (UTC, ortalamaya göre)

| oyun | zirve_saat_utc | zirve_saat_tr | ort_oyuncu | olcum |
|---|---|---|---|---|
| Rainbow Six Siege | 20:00 | 23:00 | 77,547 | 7 |
| Watch Dogs 2 | 10:00 | 13:00 | 5,796 | 2 |
| Titanfall 2 | 10:00 | 13:00 | 2,086 | 2 |
| Watch Dogs | 15:00 | 18:00 | 1,836 | 4 |
| Star Wars Battlefront II | 19:00 | 22:00 | 1,396 | 3 |

## 2. Günlük ortalama ve günlük değişim (%) — LAG window function

| oyun | gun | gunluk_ort | degisim_yuzde |
|---|---|---|---|
| Rainbow Six Siege | 2026-10-23 | 47,143 | -9 |
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
| Star Wars Battlefront II | 2026-10-23 | 905 | -3 |
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
| Titanfall 2 | 2026-10-23 | 1,299 | 32.6 |
| Titanfall 2 | 2026-10-22 | 980 | 0.8 |
| Titanfall 2 | 2026-10-21 | 972 | 9.1 |
| Titanfall 2 | 2026-10-20 | 891 | -18.6 |
| Titanfall 2 | 2026-10-19 | 1,094 | -24.4 |
| Titanfall 2 | 2026-10-18 | 1,447 | -13.4 |
| Titanfall 2 | 2026-10-17 | 1,671 | 47.9 |
| Titanfall 2 | 2026-10-16 | 1,130 | 7.1 |

## 3. Her ölçümde oyunların sıralaması (son 5 ölçüm) — DENSE_RANK

| zaman_utc | oyun | oyuncu | sira |
|---|---|---|---|
| 2026-10-23T14:47:43+00:00 | Rainbow Six Siege | 58,208 | 1 |
| 2026-10-23T14:47:43+00:00 | Watch Dogs 2 | 4,007 | 2 |
| 2026-10-23T14:47:43+00:00 | Titanfall 2 | 1,893 | 3 |
| 2026-10-23T14:47:43+00:00 | Star Wars Battlefront II | 1,214 | 4 |
| 2026-10-23T14:47:43+00:00 | Watch Dogs | 1,080 | 5 |
| 2026-10-23T09:49:51+00:00 | Rainbow Six Siege | 30,374 | 1 |
| 2026-10-23T09:49:51+00:00 | Watch Dogs 2 | 2,544 | 2 |
| 2026-10-23T09:49:51+00:00 | Titanfall 2 | 1,100 | 3 |
| 2026-10-23T09:49:51+00:00 | Watch Dogs | 676 | 4 |
| 2026-10-23T09:49:51+00:00 | Star Wars Battlefront II | 628 | 5 |
| 2026-10-23T04:08:41+00:00 | Rainbow Six Siege | 52,848 | 1 |
| 2026-10-23T04:08:41+00:00 | Watch Dogs 2 | 1,355 | 2 |
| 2026-10-23T04:08:41+00:00 | Titanfall 2 | 903 | 3 |
| 2026-10-23T04:08:41+00:00 | Star Wars Battlefront II | 873 | 4 |
| 2026-10-23T04:08:41+00:00 | Watch Dogs | 518 | 5 |
| 2026-10-22T23:06:43+00:00 | Rainbow Six Siege | 62,040 | 1 |
| 2026-10-22T23:06:43+00:00 | Star Wars Battlefront II | 943 | 2 |
| 2026-10-22T23:06:43+00:00 | Watch Dogs 2 | 899 | 3 |
| 2026-10-22T23:06:43+00:00 | Titanfall 2 | 732 | 4 |
| 2026-10-22T23:06:43+00:00 | Watch Dogs | 536 | 5 |
| 2026-10-22T19:10:19+00:00 | Rainbow Six Siege | 66,174 | 1 |
| 2026-10-22T19:10:19+00:00 | Watch Dogs 2 | 1,531 | 2 |
| 2026-10-22T19:10:19+00:00 | Star Wars Battlefront II | 1,478 | 3 |
| 2026-10-22T19:10:19+00:00 | Titanfall 2 | 895 | 4 |
| 2026-10-22T19:10:19+00:00 | Watch Dogs | 876 | 5 |

## 4. Oynaklık: hangi oyunun oyuncu sayısı en çok dalgalanıyor? (max-min / ortalama)

| oyun | min | max | ort | dalga_yuzde |
|---|---|---|---|---|
| Watch Dogs 2 | 899 | 8,619 | 3,085 | 250.3 |
| Titanfall 2 | 698 | 2,760 | 1,352 | 152.5 |
| Watch Dogs | 518 | 2,131 | 1,122 | 143.8 |
| Star Wars Battlefront II | 398 | 1,623 | 929 | 131.9 |
| Rainbow Six Siege | 26,086 | 91,821 | 57,994 | 113.3 |

## 5. Hafta içi vs hafta sonu ortalaması

| oyun | hafta_sonu | hafta_ici |
|---|---|---|
| Rainbow Six Siege | 67,806 | 54,371 |
| Star Wars Battlefront II | 1,110 | 862 |
| Titanfall 2 | 1,694 | 1,226 |
| Watch Dogs | 1,360 | 1,034 |
| Watch Dogs 2 | 3,791 | 2,824 |

## 6. Mağaza verisi: fiyat, indirim, yorum puanı + anlık oyuncu (JOIN)

| oyun | anlik_oyuncu | fiyat | para_birimi | indirim_yuzde | toplam_yorum | olumlu_yuzde | steam_puani |
|---|---|---|---|---|---|---|---|
| Rainbow Six Siege | 58,208 | 0 | FREE | 0 | – | – | – |
| Watch Dogs 2 | 4,007 | 39.99 | USD | 0 | – | – | – |
| Titanfall 2 | 1,893 | 29.99 | USD | 0 | – | – | – |
| Star Wars Battlefront II | 1,214 | 39.99 | USD | 0 | – | – | – |
| Watch Dogs | 1,080 | 15.99 | USD | 0 | – | – | – |

## 7. İndirim etkisi: indirimli günlerde oyuncu sayısı artıyor mu? (JOIN + koşullu AVG)

| oyun | indirimli_gun | normal_gun | max_indirim_yuzde | ort_indirimli | ort_normal | fark_yuzde |
|---|---|---|---|---|---|---|
| Watch Dogs 2 | 4 | 15 | 95 | 5,047 | 2,686 | 87.9 |
| Watch Dogs | 4 | 15 | 90 | 1,603 | 1,027 | 56.1 |
| Titanfall 2 | 4 | 15 | 85 | 1,741 | 1,262 | 37.9 |
| Star Wars Battlefront II | 4 | 15 | 75 | 913 | 933 | -2.1 |
| Rainbow Six Siege | 0 | 19 | 0 | – | 57,222 | – |

## 8. İndirim × oyuncu sayısı korelasyonu (Pearson r, Python)

| oyun | gun_sayisi | pearson_r | yorum |
|---|---|---|---|
| Rainbow Six Siege | 19 | – | hesaplanamadı (indirim hiç değişmedi) |
| Star Wars Battlefront II | 19 | -0.062 | çok zayıf negatif |
| Titanfall 2 | 19 | +0.567 | orta pozitif |
| Watch Dogs | 19 | +0.628 | güçlü pozitif |
| Watch Dogs 2 | 19 | +0.728 | güçlü pozitif |

> r ≈ +1: indirim arttıkça oyuncu artıyor · r ≈ 0: ilişki yok · r ≈ −1: ters ilişki. Korelasyon nedensellik değildir; birkaç günlük veriyle sonuç güvenilir olmaz.
