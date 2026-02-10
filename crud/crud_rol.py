import models.model_rol 
from sqlalchemy.orm import Session

def get_rol(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.model_rol.Rol).offset(skip).limit(limit).all()
    