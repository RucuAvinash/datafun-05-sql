import sqlite3
from pathlib import Path
from utils_logger import logger


DB_PATH = Path(__file__).parent / "data" / "sample.sqlite"


def execute_sql_update_delete(connection, file_path):
    """Execute SQL operations"""
    try:
        with open(file_path, 'r') as file:
            connection.executescript(file.read())
        logger.info(f"Executed: {file_path.name}")

    except FileNotFoundError:
        logger.error(f"File not found: {file_path.resolve()}")
        raise
    except sqlite3.OperationalError as e:
        logger.error(f"SQL execution error in {file_path.name}: {e}")
        raise
    except Exception as e:
        logger.error(f"Unexpected error in {file_path.name}: {e}")
        raise

def main():
    with sqlite3.connect(DB_PATH) as connection:
        execute_sql_update_delete(connection, Path("sql_features/update_records.sql"))
        execute_sql_update_delete(connection, Path("sql_features/delete_records.sql"))
        connection.commit()


if __name__ == "__main__":
    main()