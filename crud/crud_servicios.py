import models.model_servicios as model
from sqlalchemy.orm import Session


def get_servicios(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.Servicio)\
        .offset(skip)\
        .limit(limit)\
        .all()


def get_servicio_by_id(db: Session, servicio_id: int):
    return db.query(model.Servicio)\
        .filter(model.Servicio.Id == servicio_id)\
        .first()


def create_servicio(db: Session, data):
    nuevo = model.Servicio(**data.dict())
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