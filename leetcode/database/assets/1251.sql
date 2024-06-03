-- 1251. Average Selling Price
SELECT
  p.product_id,
  CASE
    WHEN MAX(u.units) IS NULL THEN 0
    ELSE ROUND(
      SUM(p.price * u.units) :: DECIMAL / SUM(u.units),
      2
    )
  END AS average_price
FROM
  Prices p
  LEFT JOIN UnitsSold u ON u.purchase_date >= p.start_date
  AND u.purchase_date <= p.end_date
  AND p.product_id = u.product_id
GROUP BY
  p.product_id