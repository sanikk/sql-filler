"""
Playground for prepared statements.

https://www.postgresql.org/docs/current/sql-prepare.html

- Prepared statements only last for the duration of the current database session.

- Prepared statements potentially have the largest performance advantage when a single session is being used to execute
a large number of similar statements. The performance difference will be particularly significant if the statements
are complex to plan or rewrite, e.g., if the query involves a join of many tables or requires the application of
several rules. If the statement is relatively simple to plan and rewrite but relatively expensive to execute, the
performance advantage of prepared statements will be less noticeable.

https://www.postgresql.org/docs/current/view-pg-prepared-statements.html

- get info on prepared statements for the session

Educational tool? Show what statements are prepared serverside from queries?

Comparison for prepared statements? custom vs regular (vs raw?)
"""