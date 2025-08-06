-- Write a solution to report the sum of all total investment values in 2016 tiv_2016, for all policyholders who:

-- have the same tiv_2015 value as one or more other policyholders, and
-- are not located in the same city as any other policyholder (i.e., the (lat, lon) attribute pairs must be unique).
-- Round tiv_2016 to two decimal places.


-- Write your PostgreSQL query statement below
with lat_long as (
    select pid, tiv_2015, tiv_2016,
    count(concat(lat,lon)) over(partition by concat(lat,lon)) as cnt_loc,
    count(tiv_2015) over(partition by tiv_2015) as cnt_insurance
    from insurance
)
select round(sum(tiv_2016)::numeric, 2) as tiv_2016
from lat_long
where cnt_loc = 1
and cnt_insurance != 1;