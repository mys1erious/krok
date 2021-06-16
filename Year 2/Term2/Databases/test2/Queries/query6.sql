use Electronics_store;


-- Amount of sales of each employee


select e.lastname + e.firstname as employee, count(o.employee_id) as [count]
from orders o

left join employees e on o.employee_id = e.employee_id

group by e.lastname, e.firstname
order by count(o.employee_id) desc