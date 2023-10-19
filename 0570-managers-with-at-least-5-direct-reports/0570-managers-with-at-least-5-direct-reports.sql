# Write your MySQL query statement below

SELECT e.name
FROM Employee e
JOIN (SELECT managerId, COUNT(managerId) as item_count
FROM Employee
GROUP BY (managerId)
HAVING item_count >= 5) AS s
ON e.id = s.managerId;
