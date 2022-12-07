# Write your MySQL query statement below
select distinct l1.num as ConsecutiveNums
from Logs l1
inner join Logs l2 on l2.id = l1.id+1 and l1.num = l2.num
inner join Logs l3 on l3.id = l1.id+2 and l1.num = l3.num;


