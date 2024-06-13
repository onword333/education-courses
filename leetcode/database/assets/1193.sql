-- 1193. Monthly Transactions I
SELECT
    TO_CHAR(trans_date, 'YYYY-MM') AS month,
    country,
    COUNT(id) AS trans_count,
    COUNT(id) FILTER(WHERE state = 'approved') AS approved_count,
    SUM(amount) AS trans_total_amount,
    COALESCE(SUM(amount) FILTER(WHERE state = 'approved'), 0) AS approved_total_amount
FROM Transactions
GROUP BY
    month,
    country