-- 1393. Capital Gain/Loss
-- 1-st variant
SELECT
  stock_name,
  SUM(price) FILTER (
    WHERE
      operation = 'Sell'
  ) - SUM(price) FILTER (
    WHERE
      operation = 'Buy'
  ) AS capital_gain_loss
FROM
  Stocks s
GROUP BY
  stock_name


-- 2-en variant
SELECT
  stock_name,
  SUM(
    CASE
      WHEN operation = 'Buy' THEN - price
      WHEN operation = 'Sell' THEN price
    END
  ) AS capital_gain_loss
FROM
  Stocks
GROUP BY
  stock_name;