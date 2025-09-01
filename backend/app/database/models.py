#database/models.py

from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, CheckConstraint, UniqueConstraint
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.sql import func

Base = declarative_base() #Created Base to use everywhere

class AIPlatform(Base):
    __tablename__ = "ai_platforms"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique =True, index=True, nullable=False)
    description = Column(Text, nullable=False)
    category = Column(String(100), nullable=False)
    website = Column(String(255), nullable=False)

    def __repr__(self):
        return f"<AIPlatform(name={self.name}, website{self.website})>"
    
class Tool(Base):
    __tablename__ = "tools"

    id = Column(Integer, primary_key = True, index = True)
    name = Column(String(255), unique = True, nullable= False)
    description = Column(Text, nullable= False)
    category = Column(String(100), nullable= False)
    pricing = Column(String(100), nullable= True)
    website = Column(String(255), nullable= False)

    workflow_steps = relationship("WorkflowStep", back_populates="tool")

    #Metadata fields

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    #Constraints

    __table_args__ = (
        UniqueConstraint("name", name = "uq_tool_name"),
        CheckConstraint("char_length(name) > 2", name="check_tool_name_length")  #at least 3 char
    )

class Workflow(Base):

    __tablename__ = "workflows"

    id = Column(Integer, primary_key= True, index= True)
    name = Column(String(100), unique= True, nullable= False)
    description = Column(Text, nullable= False)
    trigger_keywords = Column(Text, nullable= False)
    
    steps = relationship("WorkflowStep", back_populates="workflow")

    #Metadata fields

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    #Constraints

    __table_args__ = (
        CheckConstraint("char_length(description) > 10", name="check_workflow_description_length"),
    )

class WorkflowStep(Base):
    __tablename__ = "workflow_steps"

    id = Column(Integer, primary_key= True, index= True)
    workflow_id = Column(Integer, ForeignKey("workflows.id"), nullable= False)
    step_number = Column(Integer, nullable = False)
    tool_id = Column(Integer, ForeignKey("tools.id"), nullable= False)
    action_description = Column(Text, nullable= False)

    workflow = relationship("Workflow", back_populates="steps")
    tool = relationship("Tool", back_populates= "workflow_steps")

    #Metadata fields

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
