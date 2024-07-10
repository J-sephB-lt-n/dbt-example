WITH ORDERS AS (
    SELECT * FROM {{ source('data_source_1', 'orders') }}
)

SELECT CAST(ORDER_ID AS INTEGER)
FROM ORDERS
