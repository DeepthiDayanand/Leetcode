# Write your MySQL query statement below

select Request_at Day,
    ROUND((count(if(status!='completed', TRUE, null))/count(*)), 2) 
    as 'Cancellation Rate'
from Trips 
where
client_id in (select users_id from users where banned = 'No') and
driver_id in (select users_id from users where banned = 'No') and
request_At between '2013-10-01' and '2013-10-03'
group by request_at;