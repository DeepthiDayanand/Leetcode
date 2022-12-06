# Write your MySQL query statement below

select d.name as department, e1.name as employee, e1.salary 
from department d, employee e1, employee e2
where d.id = e1.departmentid and e1.departmentid = e2.departmentid and
e1.salary <= e2.salary

group by d.id, e1.name having count(distinct e2.salary) <= 3
order by d.name, e1.salary desc 