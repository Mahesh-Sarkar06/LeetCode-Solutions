-- Write a solution to find all the classes that have at least five students.

-- Return the result table in any order.



-- Write your PostgreSQL query statement below
WITH stud AS (
    SELECT class, count(student) AS stud_cnt
    FROM Courses
    GROUP BY class
)
SELECT class
FROM stud
WHERE stud_cnt >= 5;



-- One liner Solution
SELECT class FROM Courses GROUP BY class HAVING COUNT(student) >= 5;