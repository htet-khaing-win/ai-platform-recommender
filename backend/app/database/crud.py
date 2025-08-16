from sqlalchemy.orm import Session
from . import models, schemas

def create_platform(db: Session, platform: schemas.PlatformCreate):
    db_platform = models.AIPlatform(**platform.dict())
    db.add(db_platform)
    db.commit()
    db.refresh(db_platform)
    return db_platform

def get_platforms(db: Session):
    return db.query(models.AIPlatform).all()

def get_platform_by_id(db: Session, platform_id: int):
    return db.query(models.AIPlatform).filter(models.AIPlatform.id == platform_id).first()

def update_platform(db: Session, platform_id: int, platform: schemas.PlatformUpdate):
    db_platform = db.query(models.AIPlatform).filter(models.AIPlatform.id == platform_id).first()
    if db_platform:
        # Update all fields in the loop
        for key, value in platform.dict(exclude_unset=True).items():
            setattr(db_platform, key, value)
        
        # OUTSIDE the loop: commit, refresh, and return
        db.commit()
        db.refresh(db_platform)
        return db_platform
    
    return None

def delete_platform(db: Session, platform_id: int):
    db_platform = db.query(models.AIPlatform).filter(models.AIPlatform.id == platform_id).first()
    if db_platform:
        db.delete(db_platform)
        db.commit()
    return db_platform

#------------Tool---------------------

def create_tool(db: Session, tool:schemas.ToolCreate):
    db_tool = models.Tool(models.app.tool.dict())
    db.add(db_tool)
    db.commit()
    db.refresh(db_tool)
    return db_tool

def get_tool(db: Session, skip : int = 0, limit = 10):
    return db.query(models.Tool).offset(skip).limit(limit).all()

def update_tool(db: Session, tool_id: int, tool: schemas.ToolUpdate):
    db_tool = db.query(models.Tool).filter(models.Tool.id == tool_id).first()
    if not db_tool:
        return None
    for key, value in tool.dict(exclude_unset= True).items():
        setattr(db_tool, key,value)
    db.commit()
    db.refresh(db_tool)
    return db_tool

def delete_tool(db: Session, tool_id: int):
    db_tool = db.query(models.Tool).filter(models.Tool.id == tool_id).first()
    if not db_tool:
        return None
    db.delete(db_tool)
    db.commit()
    return db_tool