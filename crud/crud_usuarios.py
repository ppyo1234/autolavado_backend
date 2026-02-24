from sqlalchemy.orm import Session
from passlib.context import CryptContext
from datetime import datetime
import models.user as model
import schemas.schema_usuario as schemas # Asegúrate de importar tus schemas

pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")

def get_usuarios(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.Usuario).offset(skip).limit(limit).all()

def get_usuario_by_correo(db: Session, correo: str):
    return db.query(model.Usuario).filter(model.Usuario.correo_electronico == correo).first()

def create_usuario(db: Session, usuario: schemas.UsuarioCreate):
    hashed_password = pwd_context.hash(usuario.contrasena)
    
    db_usuario = model.Usuario(
        Rol_Id=usuario.rol_id,           # CORREGIDO: Coincide con Rol_Id en models/user.py
        nombre=usuario.nombre,
        primer_apellido=usuario.primer_apellido,
        segundo_apellido=usuario.segundo_apellido,
        direccion=usuario.direccion,
        correo_electronico=usuario.correo_electronico,
        numero_telefono=usuario.numero_telefono,
        estatus=usuario.estatus,
        fecha_registro=datetime.utcnow(),
        fecha_actualizacion=datetime.utcnow(),
        contrasena=hashed_password
    )
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

def update_usuario(db: Session, usuario_id: int, usuario: schemas.UsuarioUpdate):
    # CORREGIDO: Tu modelo usa "Id" con mayúscula
    db_usuario = db.query(model.Usuario).filter(model.Usuario.Id == usuario_id).first()
    if not db_usuario:
        return None

    # Usamos model_dump() si es Pydantic V2
    for key, value in usuario.model_dump(exclude_unset=True).items():
        # Mapeo manual si los nombres del schema y modelo no coinciden
        if key == "rol_id":
            setattr(db_usuario, "Rol_Id", value)
        else:
            setattr(db_usuario, key, value)

    db_usuario.fecha_actualizacion = datetime.utcnow()
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

def delete_usuario(db: Session, usuario_id: int):
    # CORREGIDO: Tu modelo usa "Id" con mayúscula
    db_usuario = db.query(model.Usuario).filter(model.Usuario.Id == usuario_id).first()
    if not db_usuario:
        return None

    db.delete(db_usuario)
    db.commit()
    return db_usuario