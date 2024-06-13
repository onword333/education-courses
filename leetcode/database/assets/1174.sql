-- 1174. Immediate Food Delivery II
WITH first_delivery AS (
  SELECT
    DISTINCT FIRST_VALUE(delivery_id) OVER(
      PARTITION BY customer_id
      ORDER BY
        order_date
    ) AS delivery_id
  FROM
    Delivery
)
SELECT
  ROUND(
    SUM(
      CASE
        WHEN d.order_date = d.customer_pref_delivery_date THEN 1
        ELSE 0
      END
    ) :: NUMERIC / COUNT(DISTINCT fs.delivery_id) * 100,
    2
  ) AS immediate_percentage
FROM
  first_delivery fs
  LEFT JOIN Delivery d ON fs.delivery_id = d.delivery_id