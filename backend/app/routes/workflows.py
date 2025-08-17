from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import crud, schemas, SessionLocal

router = APIRouter(prefix="/v1/workflows", tags=["Workflows"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=schemas.WorkflowResponse)
def create_workflow(workflow: schemas.WorkflowCreate, db: Session = Depends(get_db)):
    return crud.create_workflow(db=db, workflow=workflow)


@router.get("/", response_model=list[schemas.WorkflowResponse])
def list_workflows(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_workflows(db, skip=skip, limit=limit)


@router.get("/{workflow_id}", response_model=schemas.WorkflowResponse)
def get_workflow(workflow_id: int, db: Session = Depends(get_db)):
    db_workflow = crud.get_workflow(db, workflow_id=workflow_id)
    if not db_workflow:
        raise HTTPException(status_code=404, detail="Workflow not found")
    return db_workflow


@router.put("/{workflow_id}", response_model=schemas.WorkflowResponse)
def update_workflow(workflow_id: int, workflow: schemas.WorkflowUpdate, db: Session = Depends(get_db)):
    db_workflow = crud.update_workflow(db, workflow_id=workflow_id, workflow=workflow)
    if not db_workflow:
        raise HTTPException(status_code=404, detail="Workflow not found")
    return db_workflow


@router.delete("/{workflow_id}", response_model=schemas.WorkflowResponse)
def delete_workflow(workflow_id: int, db: Session = Depends(get_db)):
    db_workflow = crud.delete_workflow(db, workflow_id=workflow_id)
    if not db_workflow:
        raise HTTPException(status_code=404, detail="Workflow not found")
    return db_workflow
