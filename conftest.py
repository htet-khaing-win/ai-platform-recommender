# backend/app/tests/conftest.py
import asyncio
import sys
import pytest
from backend.app.database import initdb_async, async_engine

# Windows-specific event loop policy fix
if sys.platform.startswith('win'):
    # Use ProactorEventLoop on Windows to avoid the asyncpg connection issues
    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())

@pytest.fixture(scope="session")
def event_loop():
    """Create an instance of the default event loop for the test session."""
    if sys.platform.startswith('win'):
        # On Windows, create a new ProactorEventLoop
        loop = asyncio.ProactorEventLoop()
    else:
        loop = asyncio.new_event_loop()
    
    yield loop
    loop.close()

@pytest.fixture(scope="session", autouse=True)
async def setup_test_database():
    """Initialize database tables once for the entire test session"""
    await initdb_async()
    yield
    await async_engine.dispose()