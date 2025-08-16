from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import crud, schemas
from ..database import SessionLocal


router = APIRouter(prefix="/v1/tools", tags=["Tools"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#-------------Routes for Tool------------------
@router.post("/", response_model=schemas.ToolResponse)
def create_tool(tool: schemas.ToolCreate, db: Session = Depends(get_db)):
    return crud.create_tool(db=db, tool=tool)

@router.get("/", response_model=list[schemas.ToolResponse])
def list_tools(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_tools(db, skip=skip, limit=limit)

@router.get("/{tool_id}", response_model=schemas.ToolResponse)
def get_tool(tool_id: int, db: Session = Depends(get_db)):
    db_tool = crud.get_tool(db, tool_id=tool_id)
    if not db_tool:
        raise HTTPException(status_code="404", detail="Tool is not available")
    return db_tool

@router.put("/{tool_id}", response_model=schemas.ToolResponse)
def update_tool(tool_id: int, tool: schemas.ToolUpdate, db: Session = Depends(get_db)):
    db_tool = crud.update_tool(db, tool_id=tool_id, tool=tool)
    if not db_tool:
        raise HTTPException(status_code=404, detail="Tool not found")
    return db_tool

@router.delete("/{tool_id}", response_model=schemas.ToolResponse)
def delete_tool(tool_id: int, db: Session = Depends(get_db)):
    db_tool = crud.delete_tool(db, tool_id=tool_id)
    if not db_tool:
        raise HTTPException(status_code="404", detail= "Tool is not availabe")
    return db_tool