-- 601. Human Traffic of Stadium
WITH t AS(
  SELECT
    *,
    id - row_number() over(
      ORDER BY
        id asc
    ) as rnk
  FROM
    stadium
  WHERE
    people >= 100
)
SELECT
  id,
  visit_date,
  people
FROM
  t
WHERE
  rnk in(
    SELECT
      rnk
    FROM
      t
    GROUP BY
      rnk
    HAVING
      COUNT(*) >= 3
  )