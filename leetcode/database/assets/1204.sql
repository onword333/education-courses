-- 1204. Last Person to Fit in the Bus
SELECT
  person_name
FROM
  (
    SELECT
      *,
      SUM(weight) OVER(
        ORDER BY
          turn ASC
      ) AS total_weight
    FROM
      Queue
    ORDER BY
      turn DESC
  )
WHERE
  total_weight <= 1000
LIMIT
  1