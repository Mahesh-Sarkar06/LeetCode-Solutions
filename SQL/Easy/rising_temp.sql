-- Write a solution to find all dates' id with higher temperatures compared to its previous dates (yesterday).

-- Return the result table in any order.


-- Write your PostgreSQL query statement below
SELECT id
FROM (
    SELECT id, recordDate, temperature,
        LAG(temperature) OVER(ORDER BY recordDate) AS prev_temp,
        LAG(recordDate) OVER(ORDER BY recordDate) AS prev_date
    FROM Weather
)
WHERE recordDate = prev_date + INTERVAL '1 day'
AND temperature > prev_temp;