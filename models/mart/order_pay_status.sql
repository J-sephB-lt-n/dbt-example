select
    orders.order_id,
    coalesce(bank.order_pay_status, 'pending_approval') as order_pay_status,
    coalesce(bank.entry_datetime, orders.order_datetime)
        as pay_status_updated_at
from {{ ref('orders') }} orders
left join {{ ref('bank') }} bank
    on orders.order_id = bank.order_id
