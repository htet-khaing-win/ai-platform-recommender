import sqlite3
import os

# Check if database file exists
if os.path.exists("ai_platforms.db"):
    print("✓ Database file exists")
    
    # Connect and check tables
    conn = sqlite3.connect("ai_platforms.db")
    cursor = conn.cursor()
    
    # List all tables
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    print(f"Tables in database: {tables}")
    
    # Check if ai_platforms table exists and its schema
    cursor.execute("PRAGMA table_info(ai_platforms);")
    schema = cursor.fetchall()
    if schema:
        print("✓ ai_platforms table exists with schema:")
        for column in schema:
            print(f"  Column: {column[1]}, Type: {column[2]}, NotNull: {column[3]}, PrimaryKey: {column[5]}")
    else:
        print("✗ ai_platforms table does not exist")
        print("This means the table creation failed. Let's recreate it...")
        
        # Try to recreate tables
        try:
            from database import initdb
            print("Recreating tables...")
            initdb()
            print("Tables recreated successfully!")
        except Exception as e:
            print(f"Error recreating tables: {e}")
    
    conn.close()
else:
    print("✗ Database file does not exist")