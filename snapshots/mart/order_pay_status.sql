{% snapshot order_pay_status_snapshot %}

{{
    config(
      target_database='dev',
      target_schema='main_mart',
      unique_key='order_id',
      strategy='timestamp',
      updated_at='pay_status_updated_at',
    )
}}

select * from {{ ref('order_pay_status') }}

{% endsnapshot %}
