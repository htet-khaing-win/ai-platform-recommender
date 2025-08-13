#database/__init__.py

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Use absolute path - place database in the project root  
# Navigate from database/__init__.py to project root
current_file = os.path.abspath(__file__)
database_dir = os.path.dirname(current_file)  # .../backend/app/database
app_dir = os.path.dirname(database_dir)       # .../backend/app  
backend_dir = os.path.dirname(app_dir)        # .../backend
project_root = os.path.dirname(backend_dir)   # .../ai-platform-recommender

DATABASE_PATH = os.path.join(project_root, "ai_platforms.db")
SQLALCHEMY_DATABASE_URL = f"sqlite:///{DATABASE_PATH}"

print(f"Database location: {DATABASE_PATH}")

# Create engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# SessionLocal class for DB sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# defining Base
Base = declarative_base()

# Create tables in the Database
def initdb():
    from . import models  # Import models so they register with Base
    print(f"Creating tables in: {DATABASE_PATH}")
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully!")

# Import and expose commonly used components
from .models import AIPlatform
from . import crud
from . import schemas

# Automatically create tables if they don't exist
# This ensures tables are always available when the module is imported
initdb()

if __name__ == "__main__":
    print("Database tables created successfully")