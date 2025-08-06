-- Write a solution to report the fraction of players that logged in again on the day
-- after the day they first logged in, rounded to 2 decimal places.
-- In other words, you need to determine the number of players who logged in on the day immediately
-- following their initial login, and divide it by the number of total players.


-- Write your PostgreSQL query statement below
select
round(
    sum(case when fs.first_login + 1 = nw.event_date then 1 else 0 end)::numeric/
    count(distinct fs.player_id),
    2
) as fraction
from (
    select player_id, min(event_date) as first_login
    from Activity
    group by player_id
) fs
join activity nw
on fs.player_id = nw.player_id;



-- Optimized way by avoiding unnnecessary joins
WITH first_login AS (
    SELECT player_id, MIN(event_date) AS first_login_date
    FROM Activity
    GROUP BY player_id
),
consecutive_login AS (
    SELECT DISTINCT n.player_id
    FROM Activity n
    JOIN first_login fl
    ON n.player_id = fl.player_id
    WHERE n.event_date = fl.first_login_date + INTERVAL '1 day'
)
SELECT
    ROUND(COUNT(cl.player_id)::NUMERIC/COUNT(fl.player_id), 2) AS fraction
FROM consecutive_login cl
RIGHT JOIN first_login fl
ON cl.player_id = fl.player_id;