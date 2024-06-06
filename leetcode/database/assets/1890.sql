-- 1890. The Latest Login in 2020
SELECT
  user_id,
  MAX(time_stamp) AS last_stamp
FROM
  Logins
WHERE
  EXTRACT(
    YEAR
    FROM
      time_stamp
  ) = 2020
GROUP BY
  user_id;