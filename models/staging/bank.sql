with bank as (
    select * from {{ source('source_data', 'bank') }}
)

select
    cast(order_id as integer) as order_id,
    trim(status) as order_pay_status,
    cast(entry_datetime as timestamp_s) as entry_datetime
from bank
