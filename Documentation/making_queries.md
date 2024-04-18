# Making queries

### https://www.psycopg.org/docs/sql.html#module-usage
```python
query = sql.SQL("select {field} from {table} where {pkey} = %s").format(
    field=sql.Identifier('my_name'),
    table=sql.Identifier('some_table'),
    pkey=sql.Identifier('id'))
```

```python
query = sql.SQL("select {fields} from {table}").format(
    fields=sql.SQL(',').join([
        sql.Identifier('field1'),
        sql.Identifier('field2'),
        sql.Identifier('field3'),
    ]),
    table=sql.Identifier('some_table'))
```

```python
>>> query = sql.SQL("select {0} from {1}").format(
...    sql.SQL(', ').join([sql.Identifier('foo'), sql.Identifier('bar')]),
...    sql.Identifier('table'))
>>> print(query.as_string(conn))
select "foo", "bar" from "table"
```
so query.as_string should give me the generated sql lines in conn context,
and then i'll just execute them.

Should I make a black box containing all this, or just use 
postgresservice as one?

If this is good enough for sqlalchemy to use under the hood it should
work for this too, I guess.
