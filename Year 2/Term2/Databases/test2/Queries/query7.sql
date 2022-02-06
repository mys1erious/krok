use Electronics_store;


-- Highest price product
-- Sold amount of products


select top 1 pt.[name], p.[name], p.price as price
from products p

left join product_types pt on p.[type_id] = pt.[type_id]

order by price desc;


select pt.[name] as [type], p.[name], sum(op.quantity) sold_amount
from orders_products op

left join products p on op.product_id = p.product_id
left join product_types pt on p.[type_id] = pt.[type_id]

group by pt.[name], p.[name]