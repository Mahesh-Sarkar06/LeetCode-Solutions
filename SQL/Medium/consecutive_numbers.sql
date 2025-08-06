-- Find all numbers that appear at least three times consecutively.

-- Return the result table in any order.

-- Write your PostgreSQL query statement below
SELECT DISTINCT l1.num AS ConsecutiveNums
FROM Logs l1, Logs l2, Logs l3
WHERE l1.id = l2.id - 1
AND l2.id = l3.id - 1
AND l1.num = l2.num
AND l2.num = l3.num;



-- Alternate method using LAG() function
SELECT DISTINCT num AS ConsecutiveNums
FROM (
    SELECT num,
    LAG(num, 1) OVER(ORDER BY id) AS prev1,
    LAG(num, 2) OVER(ORDER BY id) AS prev2
    FROM Logs
)
WHERE num = prev1
AND num = prev2;