from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
import crud.crud_usuarios as crud
import schemas.schema_usuario as schema
import config.db

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])


def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=list[schema.Usuario])
def listar_usuarios(db: Session = Depends(get_db)):
    return crud.get_usuarios(db)


@router.get("/{usuario_id}", response_model=schema.Usuario)
def obtener_usuario(usuario_id: int, db: Session = Depends(get_db)):
    usuario = crud.get_usuario_by_id(db, usuario_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario


@router.post("/", response_model=schema.Usuario)
def crear_usuario(data: schema.UsuarioCreate, db: Session = Depends(get_db)):
    if crud.get_usuario_by_correo(db, data.correo_electronico):
        raise HTTPException(status_code=400, detail="Correo ya registrado")
    return crud.create_usuario(db, data)


@router.put("/{usuario_id}", response_model=schema.Usuario)
def actualizar_usuario(usuario_id: int, data: schema.UsuarioUpdate, db: Session = Depends(get_db)):
    usuario = crud.update_usuario(db, usuario_id, data)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario


@router.delete("/{usuario_id}")
def eliminar_usuario(usuario_id: int, db: Session = Depends(get_db)):
    usuario = crud.delete_usuario(db, usuario_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return {"mensaje": "Usuario eliminado correctamente"}