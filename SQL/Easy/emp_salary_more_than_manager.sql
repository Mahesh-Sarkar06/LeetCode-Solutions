-- Write a solution to find the employees who earn more than their managers.

-- Return the result table in any order.

-- Write your PostgreSQL query statement below
SELECT e.name as Employee
FROM Employee e
LEFT JOIN Employee m
ON e.managerId = m.id
WHERE e.salary > m.salary