-- Write a solution to report all the duplicate emails.
-- Note that it's guaranteed that the email field is not NULL.

-- Return the result table in any order.

-- Write your PostgreSQL query statement below
SELECT DISTINCT email
FROM Person
GROUP BY email
HAVING COUNT(*) > 1;


-- Alternate method using window function ROW_NUMBER()
WITH redundant AS (
    SELECT email,
    ROW_NUMBER() OVER(PARTITION BY email) AS rn
    FROM Person
)
SELECT DISTINCT email
FROM redundant
WHERE rn > 1;