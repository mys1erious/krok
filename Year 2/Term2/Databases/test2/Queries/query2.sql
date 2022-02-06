use Electronics_store;


-- Brands whose products werent sold


select b.[name] as brand
from orders_products op

left join products p on op.product_id = p.product_id
right join brands b on p.brand_id = b.brand_id

where p.brand_id is null