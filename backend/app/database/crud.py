# backend/app/database/crud.py
from typing import Optional, List
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from . import models, schemas

# -------- AIPlatform --------

async def create_platform(db: AsyncSession, platform: schemas.PlatformCreate) -> models.AIPlatform:
    obj = models.AIPlatform(**platform.dict())
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj

async def get_platforms(db: AsyncSession) -> List[models.AIPlatform]:
    result = await db.execute(select(models.AIPlatform))
    return result.scalars().all()

async def get_platform_by_id(db: AsyncSession, platform_id: int) -> Optional[models.AIPlatform]:
    return await db.get(models.AIPlatform, platform_id)

async def update_platform(db: AsyncSession, platform_id: int, platform: schemas.PlatformUpdate) -> Optional[models.AIPlatform]:
    obj = await db.get(models.AIPlatform, platform_id)
    if obj is None:
        return None
    for k, v in platform.dict(exclude_unset=True).items():
        setattr(obj, k, v)
    await db.commit()
    await db.refresh(obj)
    return obj

async def delete_platform(db: AsyncSession, platform_id: int) -> Optional[models.AIPlatform]:
    obj = await db.get(models.AIPlatform, platform_id)
    if obj is None:
        return None
    await db.delete(obj)
    await db.commit()
    return obj

# -------- Tools --------

async def create_tool(db: AsyncSession, tool: schemas.ToolCreate) -> models.Tool:
    obj = models.Tool(**tool.dict())
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj

async def get_tool(db: AsyncSession, tool_id: int) -> Optional[models.Tool]:
    return await db.get(models.Tool, tool_id)

async def get_tools(db: AsyncSession, skip: int = 0, limit: int = 100):
    result = await db.execute(select(models.Tool).offset(skip).limit(limit))
    return result.scalars().all()

async def update_tool(db: AsyncSession, tool_id: int, tool: schemas.ToolUpdate):
    obj = await db.get(models.Tool, tool_id)
    if obj is None:
        return None
    for k, v in tool.dict(exclude_unset=True).items():
        setattr(obj, k, v)
    await db.commit()
    await db.refresh(obj)
    return obj

async def delete_tool(db: AsyncSession, tool_id: int):
    obj = await db.get(models.Tool, tool_id)
    if obj is None:
        return None
    await db.delete(obj)
    await db.commit()
    return obj

# -------- Workflows --------

async def create_workflow(db: AsyncSession, workflow: schemas.WorkflowCreate) -> models.Workflow:
    obj = models.Workflow(**workflow.dict())
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj

async def get_workflow(db: AsyncSession, workflow_id: int):
    return await db.get(models.Workflow, workflow_id)

async def get_workflows(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(select(models.Workflow).offset(skip).limit(limit))
    return result.scalars().all()

async def update_workflow(db: AsyncSession, workflow_id: int, workflow: schemas.WorkflowUpdate):
    obj = await db.get(models.Workflow, workflow_id)
    if obj is None:
        return None
    for k, v in workflow.dict(exclude_unset=True).items():
        setattr(obj, k, v)
    await db.commit()
    await db.refresh(obj)
    return obj

async def delete_workflow(db: AsyncSession, workflow_id: int):
    obj = await db.get(models.Workflow, workflow_id)
    if obj is None:
        return None
    await db.delete(obj)
    await db.commit()
    return obj
