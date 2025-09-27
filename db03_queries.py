import sqlite3
import pandas as pd
from pathlib import Path
from utils_logger import logger

DB_PATH = Path(__file__).parent / "data" / "sample.sqlite"
SQL_DESCRIPTIONS = {
    "query_aggregation.sql": "Highest and Lowest Paid Employee",
    "query_filter.sql": "Filters employee last name that starts with letter 'L'",
    "query_group_by.sql": "Groups max salary by department",
    "query_join.sql": "Joins Departments and Employees to count staff per department",
    "query_sorting.sql": "Sorts employee by last name for Finance department"
}


def sql_queries(connection, file_path, description=""):
    """Execute SQL queries and print results using pandas"""
    try:
        query = file_path.read_text(encoding='utf-8').strip()

        # Heading before execution
        print("\n" + "=" * 70)
        print(f"Executing SQL File: {file_path.name}")
        print("=" * 70)
        if description:
            print(f"Description: {description}")
        print("=" * 70)


        # SELECT queries → show results
        if query.lower().startswith("select"):
            df = pd.read_sql_query(query, connection)

            print(f"\n Results from {file_path.name}:")
            print(df.to_string(index=False))
            print(f"\n Total rows: {len(df)}\n")
        else:
            connection.executescript(query)
            print(f" {file_path.name} executed (non-select).")

        logger.info(f"Executed: {file_path.name}")

    except FileNotFoundError:
        logger.error(f" File not found: {file_path.resolve()}")
        raise
    except sqlite3.OperationalError as e:
        logger.error(f" SQL execution error in {file_path.name}: {e}")
        raise
    except Exception as e:
        logger.error(f" Unexpected error in {file_path.name}: {e}")
        raise

def main():
    sql_files = [
        "query_aggregation.sql",
        "query_filter.sql",
        "query_group_by.sql",
        "query_join.sql",
        "query_sorting.sql"
    ]

    with sqlite3.connect(DB_PATH) as connection:
        for filename in sql_files:
            file_path = Path("sql_queries") / filename
            description = SQL_DESCRIPTIONS.get(filename, "No description available")
            sql_queries(connection, file_path, description)


        connection.commit()
        print("\n All SQL queries executed and committed.")

if __name__ == "__main__":
    main()