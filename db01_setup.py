import sqlite3
import os
import pandas as pd
from utils_logger import logger


def execute_sql_create(connection, file_path):
    """Execute SQL operations"""
    try:
        with open(file_path, 'r') as file:
            connection.executescript(file.read())
        logger.info(f"Executed: {os.path.basename(file_path)}")
    except FileNotFoundError as e:
        logger.error(f"File not found: {file_path}")
        raise
    except Exception as e:
        logger.error(f"Failed to execute {os.path.basename(file_path)}: {e}")
        raise
     

def setup_database():
    """Database creation"""
    
    ROOT_DIR = os.path.dirname(__file__) #path to python script
    SQL_FOLDER = os.path.join(ROOT_DIR, "sql_create")
    DATA_FOLDER = os.path.join(ROOT_DIR, "data")
    DB_PATH = os.path.join(DATA_FOLDER, "sample.sqlite")
    
    # SQL files to execute in order
    sql_create = [
        "Drop.sql",
        "CreateTable.sql", 
        "InsertRecords.sql"
    ]
    
    # Check for existance of data directory
    os.makedirs(DATA_FOLDER, exist_ok=True)
    
    logger.info("Starting database setup...")
    
    try:
        # Connection to DB
        with sqlite3.connect(DB_PATH) as connection:
            logger.info(f"Connected to: {DB_PATH}")
            
            # Execute each SQL file in loop
            for filename in sql_create:
                print(f"Print SQL Files {filename}")
                file_path = os.path.join(SQL_FOLDER, filename)
                execute_sql_create(connection, file_path)
        
        logger.info("Database setup completed successfully!")
        return True
        
    except Exception as e:
        logger.error(f"Database setup failed: {e}")
        return False

def show_departments_info():
    """Display basic info about the database"""
    
    ROOT_DIR = os.path.dirname(__file__)
    print(f"Root directory is ",ROOT_DIR)
    DB_PATH = os.path.join(ROOT_DIR, "data", "sample.sqlite") #join to the database file name 
    
    if not os.path.exists(DB_PATH):
        print("Database not found. Run setup first.")
        return
    
    try:
       
        df = pd.read_sql_query("SELECT * FROM Departments", sqlite3.connect(DB_PATH))
        
        print("\n" + "="*50)
        print("DEPARTMENTS TABLE")
        print("="*50)
        print(df.to_string(index=False))
        print(f"\nTotal records: {len(df)}")
        
    except Exception as e:
        logger.error(f"Error reading departments table: {e}")
        
def show_employees_info():
    """Display basic info about the database"""
    
    ROOT_DIR = os.path.dirname(__file__)
    DB_PATH = os.path.join(ROOT_DIR, "data", "sample.sqlite") #join to the database file name 
    
    if not os.path.exists(DB_PATH):
        print("Database not found. Run setup first.")
        return
    
    try:
       
        df = pd.read_sql_query("SELECT * FROM employees", sqlite3.connect(DB_PATH))
        
        print("\n" + "="*50)
        print("EMPLOYEES TABLE")
        print("="*50)
        print(df.to_string(index=False))
        print(f"\nTotal records: {len(df)}")
        
    except Exception as e:
        logger.error(f"Error reading authors table: {e}")


def main():
    """Main function"""
    
    # Setup database
    if setup_database():
        # Show records in authors and books table
        show_departments_info()
        show_employees_info()
    else:
        print("Setup failed!")

if __name__ == '__main__':
    main()