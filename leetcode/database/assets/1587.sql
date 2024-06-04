-- 1587. Bank Account Summary II
SELECT 
    u.name AS NAME,
    SUM(t.amount) AS BALANCE
FROM Transactions t
LEFT JOIN Users u ON t.account = u.account
GROUP BY
    u.name
HAVING SUM(t.amount) > 10000