-- 1164. Product Price at a Given Date
SELECT
  distinct p.product_id,
  COALESCE(lp.new_price, 10) AS price
FROM
  Products p
  LEFT JOIN (
    SELECT
      product_id,
      new_price,
      change_date,
      ROW_NUMBER() OVER (
        PARTITION BY product_id
        ORDER BY
          change_date DESC
      ) AS rn
    FROM
      Products
    WHERE
      change_date <= '2019-08-16'
  ) lp ON p.product_id = lp.product_id
  AND lp.rn = 1