-- 1934. Confirmation Rate
-- 1-st variant
SELECT
  s.user_id,
  ROUND(
    COUNT(s.user_id) FILTER(
      WHERE
        action = 'confirmed'
    ) :: numeric / COUNT(s.user_id),
    2
  ) AS confirmation_rate
FROM
  Signups s FULL
  JOIN Confirmations c ON s.user_id = c.user_id
GROUP BY
  s.user_id

-- 2-end variant
SELECT
  s.user_id,
  ROUND(
    avg(
      CASE
        WHEN c.action = 'confirmed' THEN 1
        ELSE 0
      END
    ),
    2
  ) AS confirmation_rate
FROM
  signups s
  LEFT JOIN confirmations c ON s.user_id = c.user_id
GROUP BY
  s.user_id