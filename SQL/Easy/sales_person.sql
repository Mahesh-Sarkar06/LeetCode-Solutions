-- Write a solution to find the names of all the salespersons who did not have any orders related to the company with the name "RED".

-- Return the result table in any order.


-- Write your PostgreSQL query statement below
SELECT sp.name
FROM SalesPerson sp
LEFT JOIN Orders o
ON sp.sales_id = o.sales_id
LEFT JOIN Company c
ON c.com_id = o.com_id
GROUP BY sp.name
HAVING SUM((CASE WHEN c.name = 'RED' THEN 1 ELSE 0 END)::NUMERIC) = 0;