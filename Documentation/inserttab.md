# Notes on inserttab

```python
sql_string = """SELECT 
        table_name, CAST(table_name::regclass AS oid) as table_id, column_name, ordinal_position, column_default, is_nullable, data_type, generation_expression, is_updatable, character_maximum_length 
        FROM information_schema.columns 
        WHERE table_schema=\'public\' AND table_name=%s
        ORDER BY ordinal_position ASC
        """
```

source https://cloud.google.com/spanner/docs/information-schema-pg

useless_basic_columns_in_postgresql = 'table_catalog, table_schema, '
useful_basic_columns_in_postgresql = 'table_name, column_name, ordinal_position, column_default, is_nullable, data_type, generation_expression, is_updatable'
used_precision_columns_in_postgresql = 'character_maximum_length'

class_is_uniform_so_duplicate_info = 'numeric_precision, numeric_precision_radix, numeric_scale'
