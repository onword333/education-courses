-- 619. Biggest Single Number
SELECT
  MAX(num) AS num
FROM
  (
    SELECT
      num
    FROM
      MyNumbers mn
    GROUP BY
      num
    HAVING
      COUNT(num) = 1
  )