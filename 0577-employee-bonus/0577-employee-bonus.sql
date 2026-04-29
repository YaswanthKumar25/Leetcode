# Write your MySQL query statement below
select 
e.name,
b.bonus
from  Employee as e
left join Bonus as b
on e.empid=b.empid
where b.empid is null or b.bonus < 1000