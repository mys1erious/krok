use Electronics_store;


-- Average payment for 1 order


select avg(total) as average_payment
from (
	select op.order_id, sum(p.price * op.quantity) as total
	from products p

	right join orders_products op on p.product_id = op.product_id

	group by op.order_id) as total;