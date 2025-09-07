import pytest
import uuid
from sqlalchemy import select, text
from sqlalchemy.exc import IntegrityError
from backend.app.database import AsyncSessionLocal
from backend.app.database.models import Tool

def generate_unique_name(prefix="TestTool"):
    """Generate unique names to avoid conflicts"""
    return f"{prefix}_{uuid.uuid4().hex[:8]}"

@pytest.mark.asyncio
async def test_tool_insert():
    """Test basic tool insertion and retrieval"""
    tool_name = generate_unique_name()
    
    async with AsyncSessionLocal() as session:
        tool = Tool(
            name=tool_name,
            description="A comprehensive testing tool",
            category="Testing",
            website="https://test.com"
        )
        session.add(tool)
        await session.commit()

        assert tool.id is not None
        assert tool.name == tool_name
        assert tool.created_at is not None
        
        result = await session.execute(select(Tool).where(Tool.name == tool_name))
        db_tool = result.scalars().first()
        assert db_tool is not None
        assert db_tool.name == tool_name

@pytest.mark.asyncio
async def test_tool_unique_constraint():
    """Test that tool names must be unique"""
    tool_name = generate_unique_name("UniqueTool")
    
    async with AsyncSessionLocal() as session:
        tool1 = Tool(
            name=tool_name,
            description="First tool",
            category="Testing",
            website="https://unique1.com"
        )
        session.add(tool1)
        await session.commit()

    async with AsyncSessionLocal() as session:
        tool2 = Tool(
            name=tool_name,
            description="Second tool",
            category="Testing", 
            website="https://unique2.com"
        )
        session.add(tool2)
        
        with pytest.raises(IntegrityError):
            await session.commit()

@pytest.mark.asyncio
async def test_tool_name_length_constraint():
    """Test the check constraint on tool name length"""
    async with AsyncSessionLocal() as session:
        tool = Tool(
            name="AB",
            description="Tool with short name", 
            category="Testing",
            website="https://short.com"
        )
        session.add(tool)
        
        with pytest.raises(IntegrityError):
            await session.commit()

@pytest.mark.asyncio
async def test_tool_valid_creation():
    """Test creating a tool with all valid fields"""
    tool_name = generate_unique_name("ValidTool")
    
    async with AsyncSessionLocal() as session:
        tool = Tool(
            name=tool_name,
            description="Valid tool description",
            category="Development",
            pricing="Free",
            website="https://valid-tool.com"
        )
        session.add(tool)
        await session.commit()
        
        assert tool.id is not None
        assert tool.name == tool_name

@pytest.mark.asyncio
async def test_tool_query_operations():
    """Test various query operations"""
    base_name = generate_unique_name("QueryTool")
    category_name = f"TestCat_{uuid.uuid4().hex[:6]}"
    
    async with AsyncSessionLocal() as session:
        tools = [
            Tool(name=f"{base_name}_1", description="First tool", category=category_name, website="https://tool1.com"),
            Tool(name=f"{base_name}_2", description="Second tool", category="DifferentCat", website="https://tool2.com"),
        ]
        
        for tool in tools:
            session.add(tool)
        await session.commit()
        
        result = await session.execute(select(Tool).where(Tool.category == category_name))
        category_tools = result.scalars().all()
        assert len(category_tools) == 1