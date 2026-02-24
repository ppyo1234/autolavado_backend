from sqlalchemy.orm import Session
from passlib.context import CryptContext
from datetime import datetime
from sqlalchemy import or_  # <-- Importamos esto para la búsqueda doble
import models.user as model
import schemas.schema_usuario as schemas 

pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")

def get_usuarios(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.Usuario).offset(skip).limit(limit).all()

def get_usuario_by_correo(db: Session, correo: str):
    return db.query(model.Usuario).filter(model.Usuario.correo_electronico == correo).first()

def create_usuario(db: Session, usuario: schemas.UsuarioCreate):
    hashed_password = pwd_context.hash(usuario.contrasena)
    
    db_usuario = model.Usuario(
        rol_id=usuario.rol_id,           
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
    # CORREGIDO: id en minúscula
    db_usuario = db.query(model.Usuario).filter(model.Usuario.id == usuario_id).first()
    if not db_usuario:
        return None

    for key, value in usuario.model_dump(exclude_unset=True).items():
        setattr(db_usuario, key, value)

    db_usuario.fecha_actualizacion = datetime.utcnow()
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

def delete_usuario(db: Session, usuario_id: int):
    # CORREGIDO: id en minúscula
    db_usuario = db.query(model.Usuario).filter(model.Usuario.id == usuario_id).first()
    if not db_usuario:
        return None

    db.delete(db_usuario)
    db.commit()
    return db_usuario

# FUNCIÓN COMPLETADA
def authenticate_user(db: Session, email_o_tel: str, contrasena: str):
    # Busca un usuario donde el correo O el teléfono coincidan
    db_usuario = db.query(model.Usuario).filter(
        or_(
            model.Usuario.correo_electronico == email_o_tel,
            model.Usuario.numero_telefono == email_o_tel
        )
    ).first()
    
    # Si no existe el usuario, o la contraseña no hace match, regresamos None
    if not db_usuario:
        return None
    if not pwd_context.verify(contrasena, db_usuario.contrasena):
        return None
        
    return db_usuario