from pydantic import BaseModel, validator
from typing import Optional, List, Text, Union

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
         from_attributes = True

class WorkflowStepResponse(BaseModel):
    step_number: int
    action_description: str
    tool: ToolResponse

    class Config:
        from_attributes = True

class WorkflowResponse(BaseModel):
    workflow_id: int
    name: str
    description: Optional[str] = None
    steps: List[WorkflowStepResponse]

    class Config:
        from_attributes = True


#--------Tool-------------

class ToolBase(BaseModel):
    name: str
    description: str
    category: str          
    pricing: str    
    website: str

class ToolCreate(ToolBase):
    pass

class ToolUpdate(BaseModel):
    name: Optional[str] = None
    description: Text = None
    category: Text = None    
    pricing: str = None     
    website: str = None 

class ToolResponse(ToolBase):
    id: int

    class Config:
        from_attributes = True
    

#-------Workflow------------

class WorkflowBase(BaseModel):
    name: str
    description: str                    
    trigger_keywords: Union[List[str], str]  
    
    @validator('trigger_keywords', pre=True)
    def convert_keywords_to_string(cls, v):
        """Convert list input to comma-separated string for database storage"""
        if isinstance(v, list):
            # Convert list to comma-separated string
            return ', '.join(v)
        elif isinstance(v, str):
            # Already a string, return as-is
            return v
        return str(v)  # Fallback

class WorkflowCreate(WorkflowBase):
    pass

class WorkflowUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None   
    trigger_keywords: Optional[Union[List[str], str]] = None  
    
    @validator('trigger_keywords', pre=True)
    def convert_keywords_to_string(cls, v):
        """Convert list input to comma-separated string for database storage"""
        if v is None:
            return None
        if isinstance(v, list):
            return ', '.join(v)
        elif isinstance(v, str):
            return v
        return str(v)

class WorkflowResponse(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    steps: List[WorkflowStepResponse]

    class Config:
        from_attributes = True