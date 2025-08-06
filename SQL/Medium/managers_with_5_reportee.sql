-- Write a solution to find managers with at least five direct reports.

-- Return the result table in any order.


-- Write your PostgreSQL query statement below
SELECT m.name
FROM Employee e
JOIN Employee m
ON e.managerId = m.id
GROUP BY e.managerId, m.name
HAVING COUNT(m.id) >= 5;