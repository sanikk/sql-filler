```mermaid
---
title: connect, account knows table, table knows work
---
sequenceDiagram
    AccountTab->>Data_service: connect(username, dbname) & disconnect()
    Data_service-->>AccountTab: True/False
    AccountTab->> UI: do_connection_chores()
    UI->> InsertTab: update_tables()
    InsertTab->>TableFrame: update_tables()
```

```mermaid
---
title: table switch, account knows table, table knows work
---
sequenceDiagram
    User->>Table: choose another table
    Table->>Work: switch_table(table_number)
```

```mermaid
---
title: connect two
---
sequenceDiagram
    Account->>UI: connect(username, dbname)
    UI->>Data_service: connect(username, dbname)
    Data_service-->>UI: True/False
    UI -->>Account: True/False
    UI ->> Table: update_tables()
```