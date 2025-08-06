-- Write a solution to find all customers who never order anything.

-- Return the result table in any order.

-- Write your PostgreSQL query statement below
SELECT name AS Customers
FROM Customers
WHERE id NOT IN (SELECT customerId FROM orders);