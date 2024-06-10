-- 550. Game Play Analysis IV
-- 1-st variant
WITH first_login AS (
  SELECT
    player_id,
    MIN(event_date) AS event_date
  FROM
    Activity
  GROUP BY
    player_id
)
SELECT
  round(
    COUNT(DISTINCT a.player_id) :: NUMERIC / COALESCE(MAX(p.count), 1),
    2
  ) AS fraction
FROM
  first_login a
  INNER JOIN Activity n ON a.player_id = n.player_id
  AND a.event_date + 1 = n.event_date
  CROSS JOIN (
    SELECT
      COUNT(DISTINCT player_id) AS count
    FROM
      Activity
  ) p

-- 2-nd variant
SELECT
  ROUND(
    COUNT(player_id) :: NUMERIC / (
      SELECT
        COUNT(DISTINCT player_id)
      FROM
        Activity
    ) :: NUMERIC,
    2
  ) AS fraction
FROM
  Activity
WHERE
  (player_id, event_date - 1) IN (
    SELECT
      player_id,
      MIN(event_date)
    FROM
      Activity
    GROUP BY
      player_id
  );