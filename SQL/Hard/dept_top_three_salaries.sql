-- A company's executives are interested in seeing who earns the most money in each of the company's departments.
-- A high earner in a department is an employee who has a salary in the top three unique salaries for that department.

-- Write a solution to find the employees who are high earners in each of the departments.

-- Return the result table in any order.


-- Write your PostgreSQL query statement below
WITH top_three AS (
    SELECT e.id AS empId, e.name AS Employee, e.salary, d.id AS deptId, d.name AS Department,
    DENSE_RANK() OVER(PARTITION BY d.name ORDER BY e.salary DESC) AS rn
    FROM Employee e
    JOIN Department d
    ON e.departmentId = d.id
)
SELECT Department, Employee, Salary
FROM top_three
WHERE rn IN (1,2,3);