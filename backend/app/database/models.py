#database/models.py

from sqlalchemy import Column, Integer, String, Text
from . import Base #import Base from __init__

class AIPlatform(Base):
    __tablename__ = "ai_platforms"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique =True, index=True, nullable=False)
    description = Column(Text, nullable=False)
    category = Column(String(100), nullable=False)
    website = Column(String(255), nullable=False)

    def __repr__(self):
        return f"<AIPlatform(name={self.name}, website{self.website})>"