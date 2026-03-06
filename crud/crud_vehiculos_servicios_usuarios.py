from sqlalchemy.orm import Session
import models.autoservicio as model

def get_registros(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.AutoServicio).offset(skip).limit(limit).all()

def get_registro_by_id(db: Session, registro_id: int):
    return db.query(model.AutoServicio).filter(model.AutoServicio.as_id == registro_id).first()

def create_registro(db: Session, data):
    # ¡Traducción perfecta a los nombres de tu modelo!
    nuevo = model.AutoServicio(
        au_id=data.vehiculo_id,  
        se_id=data.servicio_id,  
        us_id=data.operador_id,  
        as_fecha=data.fecha,     # <-- Cambiado a as_fecha
        as_hora=data.hora        # <-- Cambiado a as_hora
    )
    
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

def update_registro(db: Session, registro_id: int, data):
    registro = get_registro_by_id(db, registro_id)
    if not registro:
        return None

    if data.vehiculo_id is not None: registro.au_id = data.vehiculo_id
    if data.servicio_id is not None: registro.se_id = data.servicio_id
    if data.operador_id is not None: registro.us_id = data.operador_id
    if data.fecha is not None: registro.as_fecha = data.fecha
    if data.hora is not None: registro.as_hora = data.hora

    db.commit()
    db.refresh(registro)
    return registro

def delete_registro(db: Session, registro_id: int):
    registro = get_registro_by_id(db, registro_id)
    if not registro:
        return None

    db.delete(registro)
    db.commit()
    return registro