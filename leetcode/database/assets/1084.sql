-- 1084 Sales Analysis III
SELECT
  s.product_id,
  p.product_name
FROM
  Sales s
  JOIN Product p ON s.product_id = p.product_id
WHERE
  s.sale_date BETWEEN '2019-01-01'
  AND '2019-03-31'
  AND s.product_id NOT IN (
    SELECT
      product_id
    FROM
      Sales
    WHERE
      sale_date < '2019-01-01'
      OR sale_date > '2019-03-31'
  )
GROUP BY
  s.product_id,
  p.product_name