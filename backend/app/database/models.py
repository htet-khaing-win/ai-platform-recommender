#database/models.py

from sqlalchemy import Column, Integer, String
from . import Base #import Base from __init__

class AIPlatform(Base):
    __tablename__ = "ai_platforms"

    id = Column(Integer, primary_key=true, index=True)
    name = Column(String, unique =True, index=True, nullable=False)
    description = Column(String, nullable=False)
    website = Column(String, nullable=False)

    def __repr__(self):
        return f"<AIPlatform(name={self.name}, website{self.website})>"