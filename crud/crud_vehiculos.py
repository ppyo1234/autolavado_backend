import models.vehiculo as model
from datetime import datetime
from sqlalchemy.orm import Session

def get_vehiculos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.Vehiculo).offset(skip).limit(limit).all()

def get_vehiculo_by_id(db: Session, vehiculo_id: int):
    return db.query(model.Vehiculo).filter(model.Vehiculo.Id == vehiculo_id).first()


def create_vehiculo(db: Session, data):
    # Convertimos los datos del esquema a un diccionario
    datos = data.model_dump() # o data.dict() si tienes versión anterior
    
    # Inyectamos las fechas
    datos["fecha_registro"] = datetime.utcnow()
    datos["fecha_actualizacion"] = datetime.utcnow()
    
    nuevo = model.Vehiculo(**datos)
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo



def update_vehiculo(db: Session, vehiculo_id: int, data):
    vehiculo = get_vehiculo_by_id(db, vehiculo_id)
    if not vehiculo:
        return None

    for key, value in data.dict(exclude_unset=True).items():
        setattr(vehiculo, key, value)

    db.commit()
    db.refresh(vehiculo)
    return vehiculo

def delete_vehiculo(db: Session, vehiculo_id: int):
    vehiculo = get_vehiculo_by_id(db, vehiculo_id)
    if not vehiculo:
        return None

    db.delete(vehiculo)
    db.commit()
    return vehiculo