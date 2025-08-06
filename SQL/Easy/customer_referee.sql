-- Find the names of the customer that are either:

-- referred by any customer with id != 2.
-- not referred by any customer.
-- Return the result table in any order.


-- Write your PostgreSQL query statement below
SELECT name
FROM customer
WHERE referee_id != 2 IS NOT FALSE;