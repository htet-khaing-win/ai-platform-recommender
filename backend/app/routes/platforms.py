# backend/app/routes/platforms.py
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession

from ..database import get_db, models, schemas, crud, AsyncSessionLocal, get_db

router = APIRouter()

@router.post("/platforms", response_model=schemas.PlatformOut)
async def create_platform(platform: schemas.PlatformCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create_platform(db, platform)

@router.get("/platforms", response_model=List[schemas.PlatformOut])
async def read_platforms(db: AsyncSession = Depends(get_db)):
    return await crud.get_platforms(db)

@router.get("/platforms/{platform_id}", response_model=schemas.PlatformOut)
async def read_platform(platform_id: int, db: AsyncSession = Depends(get_db)):
    obj = await crud.get_platform_by_id(db, platform_id)
    if obj is None:
        raise HTTPException(status_code=404, detail="Platform not found")
    return obj

@router.put("/platforms/{platform_id}", response_model=schemas.PlatformOut)
async def update_platform(platform_id: int, platform: schemas.PlatformUpdate, db: AsyncSession = Depends(get_db)):
    updated = await crud.update_platform(db, platform_id, platform)
    if updated is None:
        raise HTTPException(status_code=404, detail="Platform not found")
    return updated

@router.delete("/platforms/{platform_id}", response_model=schemas.PlatformOut)
async def delete_platform(platform_id: int, db: AsyncSession = Depends(get_db)):
    deleted = await crud.delete_platform(db, platform_id)
    if deleted is None:
        raise HTTPException(status_code=404, detail="Platform not found")
    return deleted

@router.post("/v1/workflow/generate", response_model=schemas.WorkflowResponse)
async def generate_workflow(request: schemas.WorkflowRequest, db: AsyncSession = Depends(get_db)):
    # simple LIKE keyword match
    result = await db.execute(
        select(models.Workflow).where(models.Workflow.trigger_keywords.like(f"%{request.goal}%"))
    )
    workflow = result.scalars().first()
    if not workflow:
        raise HTTPException(status_code=404, detail="Couldn't find the matching workflow")

    result_steps = await db.execute(
        select(models.WorkflowStep)
        .options(selectinload(models.WorkflowStep.tool))
        .where(models.WorkflowStep.workflow_id == workflow.id)
        .order_by(models.WorkflowStep.step_number)
    )
    steps = result_steps.scalars().all()

    return schemas.WorkflowResponse(
        workflow_id=workflow.id,
        name=workflow.name,
        description=workflow.description,
        steps=[
            schemas.WorkflowStepResponse(
                step_number=s.step_number,
                action_description=s.action_description,
                tool=schemas.ToolResponse(
                    name=s.tool.name,
                    description=s.tool.description,
                    website=s.tool.website,
                )
            ) for s in steps
        ]
    )
