with users as (
    select * from {{ source('data_source_1', 'users') }}
)

select
    trim(email_address) as user_email_address,
    cast(signup_datetime as timestamp_s) as signup_datetime
from users
