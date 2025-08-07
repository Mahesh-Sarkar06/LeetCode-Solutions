-- Write a solution to report the products that were only sold in the first quarter of 2019.
-- That is, between 2019-01-01 and 2019-03-31 inclusive.

-- Return the result table in any order.


-- Write your PostgreSQL query statement below
SELECT DISTINCT p.product_id, p.product_name
FROM Product p
JOIN Sales s
ON p.product_id = s.product_id
WHERE EXTRACT(YEAR FROM s.sale_date) = 2019
AND EXTRACT(MONTH FROM s.sale_date) BETWEEN 1 AND 3
AND p.product_id NOT IN (
    SELECT product_id
    FROM Sales
    WHERE sale_date < '2019-01-01'
    OR sale_date > '2019-03-31'
);