from pydantic import BaseModel
from typing import Optional

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