-- The cancellation rate is computed by dividing the number of canceled (by client or driver) requests
-- with unbanned users by the total number of requests with unbanned users on that day.

-- Write a solution to find the cancellation rate of requests with unbanned users (both client and
-- driver must not be banned) each day between "2013-10-01" and "2013-10-03" with at least one trip.
-- Round Cancellation Rate to two decimal points.


# Write your PostgreSQL query statement below
SELECT request_at AS Day,
    ROUND(
        SUM(CASE WHEN status IN ('cancelled_by_driver', 'cancelled_by_client') THEN 1 ELSE 0 END)::NUMERIC/COUNT(8),
        2
    ) AS CancellationRate
FROM Trips
WHERE client_id IN (SELECT users_id FROM Users WHERE role = 'client' AND banned = 'No')
AND driver_id IN (SELECT users_id FROM Users WHERE role = 'driver' AND banned = 'No')
AND request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY request_at;



 -- Optimized query as there are 2 tables getting created in sub-query which increases the processing
 -- time when large Trips and Users data is present
 SELECT t.request_at AS Day,
    ROUND(
        SUM(CASE WHEN t.status IN ('cancelled_by_driver', 'cancelled_by_client') THEN 1 ELSE 0 END)::NUMERIC/COUNT(8),
        2
    ) AS CancellationRate
FROM Trips t
JOIN Users c ON t.client_id = c.users_id
JOIN Users d ON t.client_id = d.users_id
WHERE c.role = 'client' AND d.role = 'driver'
AND c.banned = 'No' AND d.banned = 'No'
AND request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY request_at;