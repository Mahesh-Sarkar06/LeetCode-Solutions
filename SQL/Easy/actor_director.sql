-- Write a solution to find all the pairs (actor_id, director_id) where
-- the actor has cooperated with the director at least three times.

-- Return the result table in any order.


-- Write your PostgreSQL query statement below
WITH pair AS (
    SELECT actor_id, director_id,
    COUNT(CONCAT(actor_id, director_id)) AS cnt
    FROM ActorDirector
    GROUP BY actor_id, director_id 
)
SELECT actor_id, director_id
FROM pair
WHERE cnt >= 3;




-- Simpler and direct approach
SELECT actor_id, director_id
FROM ActorDirector
GROUP BY actor_id, director_id
HAVING COUNT(*) >= 3;