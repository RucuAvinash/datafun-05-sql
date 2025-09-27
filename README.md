Project Progress
Step 1–3: Project Setup

Repo created (datafun-05-sql) with README.md.
.gitignore and requirements.txt added and pushed.
Virtual environment .venv created and activated.
Dependencies installed from requirements.txt.
Step 4: Schema Design and Database Initialization

Added sql_create/Drop.sql(drops existing tables).
Added sql_create/CreateTable.sql (creates authors and books tables).
Added sql_create/03_InsertRecords.sql (inserts at least 10 authors and 10 books).
Created db01_setup.py to run these scripts in order and initialize project.sqlite3.
Verified tables and data in VS Code using SQLite Viewer (Florian Klampfer).
Step 5: Cleaning and Feature Engineering

Added sql_features/update_records.sql (demonstrates UPDATEs).
Added sql_features/delete_records.sql (demonstrates DELETEs).
Created db02_features.py to apply these scripts.
Verified changes in SQLite Viewer:
Corrected title for Harry Potter and the Philosopher's Stone (b10).
Updated Employee salaries - salary *1.05
Deleted  departmentid 8
Step 6: Queries and Aggregations

Added sql_queries/query_aggregation.sql  - MAX/MIN
Added sql_queries/query_filter.sql (WHERE filter).
Added sql_queries/query_sorting.sql (ORDER BY).
Added sql_queries/query_group_by.sql (GROUP BY).
Added sql_queries/query_join.sql (INNER JOIN).
Created db03_queries.py to run these SQL queries and print results to the terminal.

Execution order:

1. db01_setup.py
2. db02_features.py
3. db03_queries.py
