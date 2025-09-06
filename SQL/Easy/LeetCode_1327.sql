-- product_id is the primary key (column with unique values) for this table.
-- This table contains data about the company's products.

-- This table may have duplicate rows.
-- product_id is a foreign key (reference column) to the Products table.
-- unit is the number of products ordered in order_date.

-- Write a solution to get the names of products that have at least 100 units ordered in February 2020 and their amount.

-- Return the result table in any order.


SELECT p.product_name,
    SUM(o.unit) AS unit
FROM Products p
JOIN Orders o
ON p.product_id = o.product_id
WHERE MONTH(o.order_date) = 2
AND YEAR(o.order_date) = 2020
GROUP BY o.product_id
HAVING SUM(o.unit) >= 100;