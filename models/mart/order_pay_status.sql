select
    orders.order_id,
    coalesce(bank.order_pay_status, 'pending_approval') as order_pay_status
from {{ ref('orders') }} orders
left join {{ ref('bank') }} bank
    on orders.order_id = bank.order_id
