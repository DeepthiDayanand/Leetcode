# Write your MySQL query statement below
#SELECT DISTINCT p1.Email 
#FROM Person p1, Person p2
#WHERE p1.Email = p2.Email and p1.id != p2.id;

select email
from Person
group by email
having count(email) > 1;