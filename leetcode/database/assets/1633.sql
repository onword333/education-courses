-- 1633. Percentage of Users Attended a Contest
SELECT
  r.contest_id,
  ROUND(
    COUNT(r.user_id) :: NUMERIC / MAX(cu.count_user) * 100,
    2
  ) AS percentage
FROM
  Register r
  CROSS JOIN (
    SELECT
      COUNT(user_id) AS count_user
    FROM
      Users
  ) cu
GROUP BY
  r.contest_id
ORDER BY
  percentage DESC,
  r.contest_id ASC