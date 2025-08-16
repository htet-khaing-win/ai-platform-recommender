from pydantic import BaseModel
from typing import Optional, List

class PlatformBase(BaseModel):
    name: str
    description: str  
    category: str     
    website: str

class PlatformCreate(PlatformBase):
    pass

class PlatformUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    category: Optional[str] = None
    website: Optional[str] = None

class PlatformOut(PlatformBase):
    id: int
    
    class Config:
        from_attributes = True

#----Request Model-------

class WorkflowRequest(BaseModel):
     goal: str


class ToolResponse(BaseModel):
     name: str
     description: Optional[str] = None
     website: Optional[str] = None

     class Config:
         orm_mode = True

class WorkflowStepResponse(BaseModel):
    step_number: int
    action_description: str
    tool: ToolResponse

    class Config:
        orm_mode = True

class WorkflowResponse(BaseModel):
    workflow_id: int
    name: str
    description: Optional[str] = None
    steps: List[WorkflowStepResponse]

    class Config:
        orm_mode = True


#--------Tool-------------

class ToolBase(BaseModel):
    name: str
    description: str


class ToolCreate(ToolBase):
    pass

class ToolUpdate(BaseModel):
    name = Optional[str] = None
    description = Optional[str] = None

class ToolResponse(ToolBase):
    id: int

    class Config:
        orm_mode = True
    

