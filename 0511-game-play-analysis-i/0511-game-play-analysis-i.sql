# Write your MySQL query statement below
select activity.player_id,
    min(activity.event_date) 
    as first_login
from activity
group by activity.player_id;