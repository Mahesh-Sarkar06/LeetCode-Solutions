-- Write a solution to find the customer_number for the customer who has placed the largest number of orders.

-- The test cases are generated so that exactly one customer will have placed more orders than any other customer.
-- It is guaranteed that atmost one customer will have maximum orders


-- Write your PostgreSQL query statement below
with customer as (
    select customer_number, count(order_number) as cnt
    from Orders
    group by customer_number
    order by cnt desc
)
select customer_number
from customer
limit 1;


-- This was to return only 1 customer who has ordered the most which is known.
-- Below query will return for all the customers who has ordered the most. So, the query will not
-- only check for top 1 instead all the customers.

WITH customer AS (
    SELECT customer_number, COUNT(order_number) AS cnt
    FROM Orders
    GROUP BY customer_number
),
max_order_count AS (
    SELECT MAX(cnt) AS max_cnt FROM customer
)
SELECT customer_number
FROM customer
WHERE cnt = (SELECT max_cnt FROM max_order_count);
