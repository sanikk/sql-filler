# table names


```python
# select * from pg_catalog.pg_tables

# schemaname |      tablename       | tableowner | tablespace | hasindexes | hasrules | hastriggers | rowsecurity
# ------------+----------------------+------------+------------+------------+----------+-------------+-------------
#  public     | account              | karpo      |            | t          | f        | t           | f

# sql_string = "SELECT tablename from pg_catalog.pg_tables WHERE tableowner=%s"
```
