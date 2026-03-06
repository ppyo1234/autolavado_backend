import models.servicio as model
from sqlalchemy.orm import Session
from datetime import datetime


def get_servicios(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.Servicio)\
        .offset(skip)\
        .limit(limit)\
        .all()


def get_servicio_by_id(db: Session, servicio_id: int):
    return db.query(model.Servicio)\
        .filter(model.Servicio.id == servicio_id)\
        .first()

def create_servicio(db: Session, data):
    # 1. Convertimos los datos del Pydantic a un diccionario
    datos = data.model_dump() # Si usas Pydantic v1 puede ser data.dict()
    
    # 2. Le agregamos las fechas automáticamente
    datos["fecha_registro"] = datetime.utcnow()
    datos["fecha_actualizacion"] = datetime.utcnow()
    
    # 3. Guardamos en la base de datos
    nuevo = model.Servicio(**datos)
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo



def update_servicio(db: Session, servicio_id: int, data):
    servicio = get_servicio_by_id(db, servicio_id)
    if not servicio:
        return None

    for key, value in data.dict(exclude_unset=True).items():
        setattr(servicio, key, value)

    db.commit()
    db.refresh(servicio)
    return servicio


def delete_servicio(db: Session, servicio_id: int):
    servicio = get_servicio_by_id(db, servicio_id)
    if not servicio:
        return None

    db.delete(servicio)
    db.commit()
    return servicio