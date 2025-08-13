from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from typing import List
from sqlalchemy.orm import Session
from ..database import crud, schemas  
from ..database import SessionLocal 

router = APIRouter()

class AIPlatform(BaseModel):
    id: int
    name: str
    category: str
    description: str
    pricing: str
    website: str

# platforms_db = [
#     AIPlatform(
#         id=1,
#         name="ChatGPT",
#         category="LLM",
#         description="Large language model by OpenAI",
#         pricing="Free / Plus subscription",
#         website="https://chat.openai.com/"
#     ),
#     AIPlatform(
#         id=2,
#         name="Claude",
#         category="LLM",
#         description="Conversational AI by Anthropic",
#         pricing="Free / Pro subscription",
#         website="https://claude.ai/"
#     )
# ]

# Dependency to get DB session

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