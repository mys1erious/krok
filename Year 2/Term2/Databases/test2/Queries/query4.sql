use Electronics_store;


-- Employee who sold the most products


select top 1 e.lastname + e.firstname as employee, sum(op.quantity) as products_sold
from orders_products op

left join orders o on op.order_id = o.order_id
left join employees e on o.employee_id = e.employee_id

group by e.lastname, e.firstname
order by products_sold desc