from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from typing import List
from sqlalchemy.orm import Session
from ..database import crud, schemas, SessionLocal, models
from ..database.schemas import WorkflowStepResponse, WorkflowRequest, WorkflowResponse, ToolResponse

router = APIRouter()

class AIPlatform(BaseModel):
    id: int
    name: str
    category: str
    description: str
    pricing: str
    website: str


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/platforms", response_model=schemas.PlatformOut)
def create_platform(platform: schemas.PlatformCreate, db: Session = Depends(get_db)):
    return crud.create_platform(db, platform)

@router.get("/platforms", response_model=list[schemas.PlatformOut])
def read_platforms(db: Session = Depends(get_db)):
    return crud.get_platforms(db)

@router.get("/platforms/{platform_id}", response_model=schemas.PlatformOut)
def read_platform(platform_id: int, db: Session = Depends(get_db)):
    db_platform = crud.get_platform_by_id(db, platform_id)
    if db_platform is None:
        raise HTTPException(status_code=404, detail="Something went wrong! Platform is not available")
    return db_platform

@router.put("/platforms/{platform_id}", response_model=schemas.PlatformOut)
def update_platform(platform_id: int, platform: schemas.PlatformUpdate, db: Session = Depends(get_db)):
    updated_platform = crud.update_platform(db, platform_id, platform)
    if updated_platform is None:
        raise HTTPException(status_code=404, detail="Something went wrong! Platform is not available")
    return updated_platform

@router.delete("/platforms/{platform_id}", response_model=schemas.PlatformOut)
def delete_platform(platform_id: int, db : Session = Depends(get_db)):
    deleted_platform = crud.delete_platform(db,platform_id)
    if deleted_platform is None:
        raise HTTPException(status_code=404, detail="Something went wrong! Platform is not available")
    return deleted_platform


@router.post("/v1/workflow/generate", response_model=WorkflowResponse)
def generate_workflow(request: WorkflowRequest, db: Session = Depends(get_db)): 

#searching for the workflow
    workflow = (
        db.query(models.Workflow)
        .filter(models.Workflow.trigger_keywords.like(f"%{request.goal}%"))
        .first()
    )

    if not workflow:
        raise HTTPException(status_code=404, detail="Couldn't find the matching workflow")
    
    # Get ordered steps for the workfow

    steps = (
        db.query(models.WorkflowStep)
        .filter(models.WorkflowStep.workflow_id == workflow.id)
        .order_by(models.WorkflowStep.step_number)
        .all()
    )

    # Building the Response

    response = WorkflowResponse(
        workflow_id = workflow.id,
        name = workflow.name,
        description= workflow.description,
        steps = [
            WorkflowStepResponse(
                step_number = step.step_number,
                action_description = step.action_description,
                tool = ToolResponse(
                    name = step.tool.name,
                    description = step.tool.description,
                    website = step.tool.website
                )
            )
            for step in steps
        ]
    )

    return response
