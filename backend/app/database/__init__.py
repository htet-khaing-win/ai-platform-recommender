# backend/app/database/__init__.py
import os
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker

load_dotenv()  # this must run before you read os.getenv

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL is not set")

# Clean, simple engine configuration
async_engine = create_async_engine(
    DATABASE_URL, 
    echo=True,  # Keep for development debugging
    future=True
)

AsyncSessionLocal = async_sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autoflush=False,
)

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

async def initdb_async():
    """
    Create tables asynchronously. Call this on startup or from tests.
    """
    # Import models inside function to ensure mappings are registered
    from . import models
    async with async_engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)

__all__ = [
    "DATABASE_URL",
    "async_engine",
    "AsyncSessionLocal", 
    "get_db",
    "initdb_async",
]