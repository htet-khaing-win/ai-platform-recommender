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
    db_tool = models.Tool(**tool.dict())
    db.add(db_tool)
    db.commit()
    db.refresh(db_tool)
    return db_tool

def get_tool(db: Session, tool_id: int):  #Specific Tools
    return db.query(models.Tool).filter(models.Tool.id == tool_id).first()

def get_tools(db: Session, skip: int = 0, limit: int = 100):  # All tools
    return db.query(models.Tool).offset(skip).limit(limit).all()

def update_tool(db: Session, tool_id: int, tool: schemas.ToolUpdate): # Tool Update
    db_tool = db.query(models.Tool).filter(models.Tool.id == tool_id).first()
    if not db_tool:
        return None
    for key, value in tool.dict(exclude_unset= True).items():
        setattr(db_tool, key,value)
    db.commit()
    db.refresh(db_tool)
    return db_tool

def delete_tool(db: Session, tool_id: int): # Tool Delete
    db_tool = db.query(models.Tool).filter(models.Tool.id == tool_id).first()
    if not db_tool:
        return None
    db.delete(db_tool)
    db.commit()
    return db_tool

#---------WorkFlow--------------------

def create_workflow(db: Session, workflow: schemas.WorkflowCreate):
    db_workflow = models.Workflow(**workflow.dict())
    db.add(db_workflow)
    db.commit()
    db.refresh(db_workflow)
    return db_workflow

def get_workflow(db: Session, workflow_id: int):
    return db.query(models.Workflow).filter(models.Workflow.id == workflow_id).first()

def get_workflows(db: Session, skip: int=0, limit: int= 10):
    return db.query(models.Workflow).offset(skip).limit(limit).all()

def update_workflow(db: Session, workflow_id: int, workflow: schemas.WorkflowUpdate):
    db_workflow = db.query(models.Workflow).filter(models.Workflow.id == workflow_id).first()
    if not db_workflow:
        return None
    
    for key, value in workflow.dict(exclude_unset=True).items():
        setattr(db_workflow, key, value)
    
    db.commit()
    db.refresh(db_workflow)
    return db_workflow

def delete_workflow(db: Session, workflow_id: int):
    
    db_workflow = db.query(models.Workflow).filter(models.Workflow.id == workflow_id).first()
    if not db_workflow:
        return None
    db.delete(db_workflow)
    db.commit()
    return db_workflow