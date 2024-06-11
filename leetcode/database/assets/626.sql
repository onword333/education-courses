-- 626. Exchange Seats
SELECT
  id,
  CASE
    WHEN MOD(id, 2) != 0
    AND (COUNT(*) OVER()) = (
      COUNT(*) OVER(
        ORDER BY
          id
      )
    ) THEN student
    WHEN MOD(id, 2) = 0 THEN LAG(student, 1) OVER(
      ORDER BY
        id
    )
    WHEN MOD(id, 2) != 0 THEN LEAD(student, 1) OVER(
      ORDER BY
        id
    )
  END AS student
FROM
  Seat