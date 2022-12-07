# Write your MySQL query statement below
select class from (
    select class, count(distinct student) as number_of_students
    from courses group by class)
as full_classes
where number_of_students >= 5;
    