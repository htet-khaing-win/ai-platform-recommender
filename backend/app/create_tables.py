# For running as module: python -m backend.app.create_tables
from .database import initdb

# For running directly: python create_tables.py
# from database import initdb

if __name__ == "__main__":
    initdb()
    print("Tables created successfully!")