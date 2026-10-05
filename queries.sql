-- queries.sql — SQL analizleri (SQLite). analyze.py her sorguyu "-- name:" etiketine göre çalıştırır.
-- Elle denemek için:  sqlite3 data/steam.db  ->  sorguyu yapıştır.

-- name: 1. Her oyunun en kalabalık olduğu saat (UTC, ortalamaya göre)
WITH hourly AS (
    SELECT game_name,
           CAST(strftime('%H', collected_at) AS INTEGER) AS hour_utc,
           ROUND(AVG(player_count)) AS avg_players,
           COUNT(*) AS samples
    FROM player_counts
    GROUP BY game_name, hour_utc
),
ranked AS (
    SELECT *, RANK() OVER (PARTITION BY game_name ORDER BY avg_players DESC) AS rnk
    FROM hourly
)
SELECT game_name   AS oyun,
       printf('%02d:00', hour_utc)          AS zirve_saat_utc,
       printf('%02d:00', (hour_utc + 3) % 24) AS zirve_saat_tr,
       CAST(avg_players AS INTEGER)          AS ort_oyuncu,
       samples                               AS olcum
FROM ranked
WHERE rnk = 1
ORDER BY ort_oyuncu DESC;

-- name: 2. Günlük ortalama ve günlük değişim (%) — LAG window function
WITH daily AS (
    SELECT game_name, date(collected_at) AS gun, ROUND(AVG(player_count)) AS ort
    FROM player_counts
    GROUP BY game_name, gun
)
SELECT game_name AS oyun,
       gun,
       CAST(ort AS INTEGER) AS gunluk_ort,
       ROUND(100.0 * (ort - LAG(ort) OVER w) / LAG(ort) OVER w, 1) AS degisim_yuzde
FROM daily
WINDOW w AS (PARTITION BY game_name ORDER BY gun)
ORDER BY oyun, gun DESC;

-- name: 3. Her ölçümde oyunların sıralaması (son 5 ölçüm) — DENSE_RANK
WITH last_ts AS (
    SELECT DISTINCT collected_at FROM player_counts ORDER BY collected_at DESC LIMIT 5
)
SELECT p.collected_at AS zaman_utc,
       p.game_name    AS oyun,
       p.player_count AS oyuncu,
       DENSE_RANK() OVER (PARTITION BY p.collected_at ORDER BY p.player_count DESC) AS sira
FROM player_counts p
JOIN last_ts USING (collected_at)
ORDER BY zaman_utc DESC, sira;

-- name: 4. Oynaklık: hangi oyunun oyuncu sayısı en çok dalgalanıyor? (max-min / ortalama)
SELECT game_name AS oyun,
       MIN(player_count) AS min,
       MAX(player_count) AS max,
       CAST(ROUND(AVG(player_count)) AS INTEGER) AS ort,
       ROUND(100.0 * (MAX(player_count) - MIN(player_count)) / AVG(player_count), 1) AS dalga_yuzde
FROM player_counts
GROUP BY game_name
ORDER BY dalga_yuzde DESC;

-- name: 5. Hafta içi vs hafta sonu ortalaması
SELECT game_name AS oyun,
       CAST(ROUND(AVG(CASE WHEN strftime('%w', collected_at) IN ('0','6') THEN player_count END)) AS INTEGER) AS hafta_sonu,
       CAST(ROUND(AVG(CASE WHEN strftime('%w', collected_at) NOT IN ('0','6') THEN player_count END)) AS INTEGER) AS hafta_ici
FROM player_counts
GROUP BY game_name
ORDER BY oyun;

-- name: 6. Mağaza verisi: fiyat, indirim, yorum puanı + anlık oyuncu (JOIN)
WITH latest_count AS (
    SELECT app_id, player_count
    FROM player_counts
    WHERE collected_at = (SELECT MAX(collected_at) FROM player_counts)
),
latest_store AS (
    SELECT * FROM game_details
    WHERE snapshot_date = (SELECT MAX(snapshot_date) FROM game_details)
)
SELECT s.game_name AS oyun,
       c.player_count AS anlik_oyuncu,
       s.final_price_cents / 100.0 AS fiyat,
       s.currency AS para_birimi,
       s.discount_percent AS indirim_yuzde,
       s.total_reviews AS toplam_yorum,
       ROUND(100.0 * s.positive_reviews / NULLIF(s.total_reviews, 0), 1) AS olumlu_yuzde,
       s.review_desc AS steam_puani
FROM latest_store s
LEFT JOIN latest_count c USING (app_id)
ORDER BY anlik_oyuncu DESC;

-- name: 7. İndirim etkisi: indirimli günlerde oyuncu sayısı artıyor mu? (JOIN + koşullu AVG)
WITH daily AS (
    SELECT app_id, date(collected_at) AS gun, AVG(player_count) AS ort
    FROM player_counts
    GROUP BY app_id, gun
),
joined AS (
    SELECT g.game_name, d.ort, COALESCE(g.discount_percent, 0) AS indirim
    FROM daily d
    JOIN game_details g ON g.app_id = d.app_id AND g.snapshot_date = d.gun
)
SELECT game_name AS oyun,
       SUM(indirim > 0)  AS indirimli_gun,
       SUM(indirim = 0)  AS normal_gun,
       MAX(indirim)      AS max_indirim_yuzde,
       CAST(ROUND(AVG(CASE WHEN indirim > 0 THEN ort END)) AS INTEGER) AS ort_indirimli,
       CAST(ROUND(AVG(CASE WHEN indirim = 0 THEN ort END)) AS INTEGER) AS ort_normal,
       ROUND(100.0 * (AVG(CASE WHEN indirim > 0 THEN ort END) - AVG(CASE WHEN indirim = 0 THEN ort END))
             / AVG(CASE WHEN indirim = 0 THEN ort END), 1) AS fark_yuzde
FROM joined
GROUP BY game_name
ORDER BY fark_yuzde DESC;
