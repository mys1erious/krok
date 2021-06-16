use Electronics_store;


-- 2 clients who have the most visits(orders)


select top 2 c.lastname + c.firstname as [client], count(o.client_id) as [count]
from orders o

left join clients c on o.client_id = c.client_id

group by c.lastname, c.firstname
order by count(o.client_id) desc