# Write your MySQL query statement below
SELECT v.customer_id, COUNT(*) AS count_no_trans 
FROM Visits v
LEFT JOIN Transactions t ON v.visit_id = t.visit_id
WHERE t.visit_id IS NULL
GROUP BY v.customer_id;