#database/__init__.py

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from dotenv import load_dotenv
from .models import Base, Tool
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from fastapi import Depends
from sqlalchemy import select

# Load environment variables first
load_dotenv()

# Get DATABASE_URL from environment
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable is required")

print(f"Database URL: {DATABASE_URL}")

# Create async engine for main operations
async_engine = create_async_engine(DATABASE_URL, echo=True, future=True)

# Create sync engine for table creation (initdb)
sync_engine = create_engine(DATABASE_URL.replace("+asyncpg", ""), echo=True)

# AsyncSession factory using async_sessionmaker
AsyncSessionLocal = async_sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    autocommit=False,
    autoflush=False,
    expire_on_commit=False
)

async def get_db():
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()

async def read_tools(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Tool))
    return result.scalars().all()

# Create tables in the Database (sync operation)
def initdb():
    from . import models  # Import models so they register with Base
    print("Creating tables in database...")
    Base.metadata.create_all(bind=sync_engine)
    print("Tables created successfully!")

# Import and expose commonly used components
from .models import AIPlatform
from . import crud
from . import schemas

# Automatically create tables if they don't exist
initdb()

if __name__ == "__main__":
    print("Database initialization completed")