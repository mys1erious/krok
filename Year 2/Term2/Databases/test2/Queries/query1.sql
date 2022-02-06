use Electronics_store;


-- total sales profit for each product


select pt.[name] as [type], p.[name], op.quantity, p.price, sum(op.quantity * p.price) as total
from orders_products as op

right join products p on op.product_id = p.product_id
left join product_types as pt on p.[type_id] = pt.[type_id]

group by pt.[name], p.[name], op.quantity, p.price

