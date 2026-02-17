
import models.model_rol as model
from sqlalchemy.orm import Session


def get_roles(db: Session, skip: int = 0, limit: int = 100):
    return import models.model_rol as model
from sqlalchemy.orm import Session


def get_roles(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.Rol)\
        .offset(skip)\
        .limit(limit)\
        .all()


def get_rol_by_id(db: Session, rol_id: int):
    return db.query(model.Rol)\
        .filter(model.Rol.Id == rol_id)\
        .first()


def create_rol(db: Session, data):
    nuevo = model.Rol(**data.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo


def update_rol(db: Session, rol_id: int, data):
    rol = get_rol_by_id(db, rol_id)
    if not rol:
        return None

    for key, value in data.dict(exclude_unset=True).items():
        setattr(rol, key, value)

    db.commit()
    db.refresh(rol)
    return rol


def delete_rol(db: Session, rol_id: int):
    rol = get_rol_by_id(db, rol_id)
    if not rol:
        return None

    db.delete(rol)
    db.commit()
    return rol
db.query(model.Rol)\
        .offset(skip)\
        .limit(limit)\
        .all()


def get_rol_by_id(db: Session, rol_id: int):
    return db.query(model.Rol)\
        .filter(model.Rol.Id == rol_id)\
        .first()


def create_rol(db: Session, data):
    nuevo = model.Rol(**data.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo


def update_rol(db: Session, rol_id: int, data):
    rol = get_rol_by_id(db, rol_id)
    if not rol:
        return None

    for key, value in data.dict(exclude_unset=True).items():
        setattr(rol, key, value)

    db.commit()
    db.refresh(rol)
    return rol


def delete_rol(db: Session, rol_id: int):
    rol = get_rol_by_id(db, rol_id)
    if not rol:
        return None

    db.delete(rol)
    db.commit()
    return rol