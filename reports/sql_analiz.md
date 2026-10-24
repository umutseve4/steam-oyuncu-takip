# 🔎 SQL Analizi

_Otomatik üretildi: 24.10.2026 17:59 UTC · sorgular: [`queries.sql`](../queries.sql)_

## 1. Her oyunun en kalabalık olduğu saat (UTC, ortalamaya göre)

| oyun | zirve_saat_utc | zirve_saat_tr | ort_oyuncu | olcum |
|---|---|---|---|---|
| Rainbow Six Siege | 20:00 | 23:00 | 77,547 | 7 |
| Watch Dogs 2 | 15:00 | 18:00 | 5,577 | 4 |
| Titanfall 2 | 13:00 | 16:00 | 2,013 | 3 |
| Watch Dogs | 15:00 | 18:00 | 1,836 | 4 |
| Star Wars Battlefront II | 17:00 | 20:00 | 1,474 | 4 |

## 2. Günlük ortalama ve günlük değişim (%) — LAG window function

| oyun | gun | gunluk_ort | degisim_yuzde |
|---|---|---|---|
| Rainbow Six Siege | 2026-10-24 | 61,584 | 9 |
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
| Star Wars Battlefront II | 2026-10-24 | 1,312 | 15.4 |
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
| Titanfall 2 | 2026-10-24 | 1,498 | 27.4 |
| Titanfall 2 | 2026-10-23 | 1,176 | 20 |
| Titanfall 2 | 2026-10-22 | 980 | 0.8 |
| Titanfall 2 | 2026-10-21 | 972 | 9.1 |
| Titanfall 2 | 2026-10-20 | 891 | -18.6 |
| Titanfall 2 | 2026-10-19 | 1,094 | -24.4 |

## 3. Her ölçümde oyunların sıralaması (son 5 ölçüm) — DENSE_RANK

| zaman_utc | oyun | oyuncu | sira |
|---|---|---|---|
| 2026-10-24T17:59:07+00:00 | Rainbow Six Siege | 77,157 | 1 |
| 2026-10-24T17:59:07+00:00 | Watch Dogs 2 | 2,379 | 2 |
| 2026-10-24T17:59:07+00:00 | Star Wars Battlefront II | 1,874 | 3 |
| 2026-10-24T17:59:07+00:00 | Titanfall 2 | 1,341 | 4 |
| 2026-10-24T17:59:07+00:00 | Watch Dogs | 1,114 | 5 |
| 2026-10-24T14:22:41+00:00 | Rainbow Six Siege | 66,416 | 1 |
| 2026-10-24T14:22:41+00:00 | Watch Dogs 2 | 4,256 | 2 |
| 2026-10-24T14:22:41+00:00 | Titanfall 2 | 2,179 | 3 |
| 2026-10-24T14:22:41+00:00 | Star Wars Battlefront II | 1,585 | 4 |
| 2026-10-24T14:22:41+00:00 | Watch Dogs | 1,242 | 5 |
| 2026-10-24T10:38:23+00:00 | Rainbow Six Siege | 41,121 | 1 |
| 2026-10-24T10:38:23+00:00 | Watch Dogs 2 | 3,384 | 2 |
| 2026-10-24T10:38:23+00:00 | Titanfall 2 | 1,569 | 3 |
| 2026-10-24T10:38:23+00:00 | Star Wars Battlefront II | 995 | 4 |
| 2026-10-24T10:38:23+00:00 | Watch Dogs | 868 | 5 |
| 2026-10-24T05:34:25+00:00 | Rainbow Six Siege | 57,029 | 1 |
| 2026-10-24T05:34:25+00:00 | Watch Dogs 2 | 2,735 | 2 |
| 2026-10-24T05:34:25+00:00 | Titanfall 2 | 1,509 | 3 |
| 2026-10-24T05:34:25+00:00 | Star Wars Battlefront II | 912 | 4 |
| 2026-10-24T05:34:25+00:00 | Watch Dogs | 711 | 5 |
| 2026-10-24T00:32:36+00:00 | Rainbow Six Siege | 66,198 | 1 |
| 2026-10-24T00:32:36+00:00 | Star Wars Battlefront II | 1,194 | 2 |
| 2026-10-24T00:32:36+00:00 | Watch Dogs 2 | 1,114 | 3 |
| 2026-10-24T00:32:36+00:00 | Titanfall 2 | 893 | 4 |
| 2026-10-24T00:32:36+00:00 | Watch Dogs | 562 | 5 |

## 4. Oynaklık: hangi oyunun oyuncu sayısı en çok dalgalanıyor? (max-min / ortalama)

| oyun | min | max | ort | dalga_yuzde |
|---|---|---|---|---|
| Watch Dogs 2 | 899 | 8,619 | 3,036 | 254.3 |
| Star Wars Battlefront II | 398 | 1,874 | 961 | 153.7 |
| Titanfall 2 | 698 | 2,760 | 1,352 | 152.5 |
| Watch Dogs | 518 | 2,131 | 1,103 | 146.2 |
| Rainbow Six Siege | 26,086 | 91,821 | 58,442 | 112.5 |

## 5. Hafta içi vs hafta sonu ortalaması

| oyun | hafta_sonu | hafta_ici |
|---|---|---|
| Rainbow Six Siege | 66,733 | 54,853 |
| Star Wars Battlefront II | 1,145 | 881 |
| Titanfall 2 | 1,660 | 1,219 |
| Watch Dogs | 1,281 | 1,026 |
| Watch Dogs 2 | 3,615 | 2,785 |

## 6. Mağaza verisi: fiyat, indirim, yorum puanı + anlık oyuncu (JOIN)

| oyun | anlik_oyuncu | fiyat | para_birimi | indirim_yuzde | toplam_yorum | olumlu_yuzde | steam_puani |
|---|---|---|---|---|---|---|---|
| Rainbow Six Siege | 77,157 | 0 | FREE | 0 | – | – | – |
| Watch Dogs 2 | 2,379 | 39.99 | USD | 0 | – | – | – |
| Star Wars Battlefront II | 1,874 | 39.99 | USD | 0 | – | – | – |
| Titanfall 2 | 1,341 | 29.99 | USD | 0 | – | – | – |
| Watch Dogs | 1,114 | 15.99 | USD | 0 | – | – | – |

## 7. İndirim etkisi: indirimli günlerde oyuncu sayısı artıyor mu? (JOIN + koşullu AVG)

| oyun | indirimli_gun | normal_gun | max_indirim_yuzde | ort_indirimli | ort_normal | fark_yuzde |
|---|---|---|---|---|---|---|
| Watch Dogs 2 | 4 | 16 | 95 | 5,047 | 2,664 | 89.5 |
| Watch Dogs | 4 | 16 | 90 | 1,603 | 1,019 | 57.2 |
| Titanfall 2 | 4 | 16 | 85 | 1,741 | 1,269 | 37.1 |
| Star Wars Battlefront II | 4 | 16 | 75 | 913 | 971 | -6 |
| Rainbow Six Siege | 0 | 20 | 0 | – | 57,908 | – |

## 8. İndirim × oyuncu sayısı korelasyonu (Pearson r, Python)

| oyun | gun_sayisi | pearson_r | yorum |
|---|---|---|---|
| Rainbow Six Siege | 20 | – | hesaplanamadı (indirim hiç değişmedi) |
| Star Wars Battlefront II | 20 | -0.147 | çok zayıf negatif |
| Titanfall 2 | 20 | +0.556 | orta pozitif |
| Watch Dogs | 20 | +0.634 | güçlü pozitif |
| Watch Dogs 2 | 20 | +0.731 | güçlü pozitif |

> r ≈ +1: indirim arttıkça oyuncu artıyor · r ≈ 0: ilişki yok · r ≈ −1: ters ilişki. Korelasyon nedensellik değildir; birkaç günlük veriyle sonuç güvenilir olmaz.
