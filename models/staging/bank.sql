with bank as (
    select * from {{ source('source_data', 'bank') }}
)

select
    cast(order_id as integer) as order_id,
    trim(status) as order_status
from bank
