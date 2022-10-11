# Write your MySQL query statement below

SELECT d.Name as Department, e.Name as Employee, e.Salary
FROM Employee e, Department d
WHERE 
    d.id = e.departmentId AND 
     e.salary = (SELECT MAX(e1.salary) FROM Employee e1 where e1.departmentId = d.id);
     
     