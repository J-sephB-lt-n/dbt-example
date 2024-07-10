{% test is_valid_id(model, column_name) %}

with validation as (

    select
        {{ column_name }} as id_field

    from {{ model }}

),

validation_errors as (

    select
        id_field

    from validation
    -- if this is true, then even_field is actually odd!
    where len(cast(id_field as varchar)) <> 8

)

select *
from validation_errors

{% endtest %}
