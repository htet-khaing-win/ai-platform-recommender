import asyncio
from sqlalchemy import select
from . import AsyncSessionLocal
from .models import Tool

async def test_query():
    async with AsyncSessionLocal() as session:
        result = await session.execute(select(Tool))
        tools = result.scalars().all()
        print(tools)

asyncio.run(test_query())
