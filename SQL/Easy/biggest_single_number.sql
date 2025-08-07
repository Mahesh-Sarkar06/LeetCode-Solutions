-- A single number is a number that appeared only once in the MyNumbers table.

-- Find the largest single number. If there is no single number, report null.


-- Write your PostgreSQL query statement below
with max_num as (
    select num, count(num) as cnt
    from MyNumbers
    group by num
)
select max(num) as num
from max_num
where cnt = 1;