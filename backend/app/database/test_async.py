import pytest
from sqlalchemy import select
from backend.app.database import AsyncSessionLocal
from backend.app.database.models import Tool

@pytest.mark.asyncio
async def test_query():
    async with AsyncSessionLocal() as session:
        result = await session.execute(select(Tool))
        tools = result.scalars().all()
        # Simple assert instead of print
        assert isinstance(tools, list)
