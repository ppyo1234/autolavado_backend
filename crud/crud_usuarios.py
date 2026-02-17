from sqlalchemy.orm import Session
import models.model_vehiculos as model

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_usuarios(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.Usuario).offset(skip).limit(limit).all()

def get_usuario_by_nombre(db: Session, nombre: str):
    return db.query(model.Usuario).filter(model.Usuario.nombre == nombre).first()

def get_usuario_by_correo(db: Session, correo: str):
    return db.query(model.Usuario).filter(model.Usuario.correo == correo).first()

def create_usuario(db: Session,usuario:schemas.schema_usuario.UsuarioCreate):
    hashed_password = pwd_context.hash(usuario.contrasena)
    db_usuario = model.Usuario(
        rol_id=usuario.rol_id,
        nombre=usuario.nombre,
        primer_apellido=usuario.primer_apellido,
        segundo_apellido=usuario.segundo_apellido,
        correo_electronico=usuario.correo_electronico,
        direccion=usuario.direccion,
        estado=usuario.estatus,
        fecha_registro=datetime.utcnow(),
        fecha_actualizacion=datetime.utcnow(),
        numero_telefono=usuario.numero_telefono,
        correo_electronico=usuario.correo_electronico,
        contrasena=hashed_password
    )
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

def update_usuario(db: Session, usuario_id: int, usuario: schemas.schema_usuario.UsuarioUpdate):
    db_usuario = db.query(model.Usuario).filter(model.Usuario.id == usuario_id).first()
    if not db_usuario:
        return None

    for key, value in usuario.dict(exclude_unset=True).items():
        setattr(db_usuario, key, value)

    db_usuario.fecha_actualizacion = datetime.utcnow()
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

def delete_usuario(db: Session, usuario_id: int):
    db_usuario = db.query(model.Usuario).filter(model.Usuario.id == usuario_id).first()
    if not db_usuario:
        return None

    db.delete(db_usuario)
    db.commit()
    return db_usuario

