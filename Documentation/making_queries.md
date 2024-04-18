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

## On placeholders

class psycopg2.sql.Placeholder(name=None)
A Composable representing a placeholder for query parameters.

If the name is specified, generate a named placeholder (e.g. %(name)s), otherwise generate a positional placeholder (e.g. %s).

The object is useful to generate SQL queries with a variable number of arguments.

Examples:
```python
>>> names = ['foo', 'bar', 'baz']

>>> q1 = sql.SQL("insert into table ({}) values ({})").format(
...     sql.SQL(', ').join(map(sql.Identifier, names)),
...     sql.SQL(', ').join(sql.Placeholder() * len(names)))
>>> print(q1.as_string(conn))
insert into table ("foo", "bar", "baz") values (%s, %s, %s)

>>> q2 = sql.SQL("insert into table ({}) values ({})").format(
...     sql.SQL(', ').join(map(sql.Identifier, names)),
...     sql.SQL(', ').join(map(sql.Placeholder, names)))
>>> print(q2.as_string(conn))
insert into table ("foo", "bar", "baz") values (%(foo)s, %(bar)s, %(baz)s)
name¶
The name of the Placeholder.
```
