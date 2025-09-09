-- id is the column with unique values for this table.
-- name is the name of the user.

-- id is the column with unique values for this table.
-- user_id is the id of the user who traveled the distance "distance".


-- Write a solution to report the distance traveled by each user.

-- Return the result table ordered by travelled_distance in descending order, if two or more users traveled the same distance, order them by their name in ascending order.



SELECT u.name,
    COALESCE(SUM(r.distance)) AS travelled_distance
FROM Users u
LEFT JOIN Rides r
ON u.id = r.user_id
GROUP BY r.user_id
ORDER BY travelled_distance DESC, u.name ASC