from sqlalchemy.orm import Session
from . import models, schemas

def create_platform(db: Session, platform: schemas.PlatformCreate):
    db_platform = models.AIPlatform(**platform.dict())
    db.add(db_platform)
    db.commit()
    db.refresh(db_platform)
    return db_platform

def get_platforms(db:Session):
    return db.query(models.AIPlatform).all()

def get_platform_by_id(db: Session, platform_id: int):
    return db.query(models.AIPlatform).filter(models.AIPlatform.id == platform_id).first()

def update_platform(db: Session, platform_id: int, platform: schemas.PlatformUpdate):
    db_platform = db.query(models.AIPlatform).filter(models.AIPlatform.id == platform_id).first()
    if db_platform:
        for key, value in platform.dict(exclude_unset=True).items():
            setattr(db_platform, key, value)
            db.commit()
            db.refresh(db_platform)
            return db_platform
        
def delete_platform(db: Session, platform_id: int):
    db_platform = db.query(models.AIPlatform).filter(models.AIPlatform.id == platform_id).first()
    if db_platform:
        db.delete(db_platform)
        db.commit()
    return db_platform