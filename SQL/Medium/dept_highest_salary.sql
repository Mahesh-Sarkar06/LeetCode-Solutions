-- Write a solution to find employees who have the highest salary in each of the departments.

-- Return the result table in any order.

-- Write your PostgreSQL query statement below
WITH dept_high_sal AS (
    SELECT e.id AS empId, e.name AS Employee, e.salary, d.id AS deptId, d.name AS Department,
    DENSE_RANK() OVER(PARTITION BY d.name ORDER BY e.salary desc) AS rn
    FROM Employee e
    JOIN Department d
    ON e.departmentId = d.id
)
SELECT Department, Employee, Salary
FROM dept_high_sal
WHERE rn = 1;