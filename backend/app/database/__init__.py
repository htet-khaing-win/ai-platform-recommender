#database/__init__.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# SQLite URL for local files
SQLALCHEMY_DATABASE_URL = "sqlite:///./ai_platforms.db"

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
    Base.metadata.create_all(bind=engine)

# Import and expose commonly used components
from .models import AIPlatform
from . import crud
from . import schemas

if __name__ == "__main__":
    initdb()
    print("Database tables created successfully")