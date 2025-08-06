-- Write a solution to report the name and bonus amount of each employee with a bonus less than 1000.

-- Return the result table in any order.



-- Write your PostgreSQL query statement below
SELECT e.name, b.bonus
FROM Employee e
LEFT JOIN Bonus b
ON e.empId = b.empId
WHERE b.bonus < 1000
OR b.bonus IS NULL;