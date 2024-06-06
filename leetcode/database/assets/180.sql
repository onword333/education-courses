-- 180. Consecutive Numbers
SELECT
  DISTINCT num AS ConsecutiveNums
FROM
  (
    SELECT
      id,
      num,
      LAG(num, 1) OVER (
        ORDER BY
          id
      ) AS prev_num,
      LEAD(num, 1) OVER (
        ORDER BY
          id
      ) AS next_num,
      LAG(id, 1) OVER (
        ORDER BY
          id
      ) AS prev_id,
      LEAD(id, 1) OVER (
        ORDER BY
          id
      ) AS next_id
    FROM
      Logs
  ) t1
WHERE
  num = prev_num
  AND num = next_num
  AND id = prev_id + 1
  AND id = next_id - 1

-- 2-end variant
SELECT
  DISTINCT l1.num AS ConsecutiveNums
FROM
  Logs l1,
  Logs l2,
  Logs l3
WHERE
  l1.num = l2.num
  AND l2.num = l3.num
  AND l1.id = l2.id - 1
  AND l2.id = l3.id - 1;