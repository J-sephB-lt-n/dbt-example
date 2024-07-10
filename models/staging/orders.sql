with orders as (
    select * from {{ source('data_source_1', 'orders') }}
)

select
    cast(order_id as integer) as order_id,
    trim(user_email_address) as user_email_address,
    cast(amount as decimal(18, 2)) as amount,
    cast(order_datetime as timestamp_s) as order_datetime
from orders
