SELECT
    u.name,
    SUM(t.amount) as balance
FROM Users AS u
LEFT JOIN Transactions AS t
ON u.account = t.account
GROUP BY t.account
having balance >10000