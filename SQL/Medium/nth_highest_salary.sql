-- Write a solution to find the nth highest distinct salary from the Employee table.
-- If there are less than n distinct salaries, return null.

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
      WITH salary_rank AS (
        SELECT salary,
        DENSE_RANK() OVER(ORDER BY salary DESC) as rn
        FROM Employee
      )
      SELECT DISTINCT salary
      FROM salary_rank
      WHERE rn = N
  );
END