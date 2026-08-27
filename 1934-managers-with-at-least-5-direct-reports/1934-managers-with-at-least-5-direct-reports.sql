-- Write your PostgreSQL query statement below
select e1.name 
from employee e1 
inner join employee e2
on e1.id = e2.managerid
group by e1.name,e2.managerid
having count(e2.managerid)>=5
-- order by e1.id

/*
Synced seamlessly with LeetHub Pro
Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
*/