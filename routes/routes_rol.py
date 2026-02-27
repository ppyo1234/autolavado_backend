from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
import crud.crud_rol as crud
import schemas.schema_rol as schema
import config.db
from utils.security import get_current_active_user

router = APIRouter(
    prefix="/roles", 
    tags=["Roles"],
    dependencies=[Depends(get_current_active_user)]
)


def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=list[schema.Rol])
def listar_roles(db: Session = Depends(get_db)):
    return crud.get_roles(db)


@router.get("/{rol_id}", response_model=schema.Rol)
def obtener_rol(rol_id: int, db: Session = Depends(get_db)):
    rol = crud.get_rol_by_id(db, rol_id)
    if not rol:
        raise HTTPException(status_code=404, detail="Rol no encontrado")
    return rol


@router.post("/", response_model=schema.Rol)
def crear_rol(data: schema.RolCreate, db: Session = Depends(get_db)):
    return crud.create_rol(db, data)


@router.put("/{rol_id}", response_model=schema.Rol)
def actualizar_rol(rol_id: int, data: schema.RolUpdate, db: Session = Depends(get_db)):
    rol = crud.update_rol(db, rol_id, data)
    if not rol:
        raise HTTPException(status_code=404, detail="Rol no encontrado")
    return rol


@router.delete("/{rol_id}")
def eliminar_rol(rol_id: int, db: Session = Depends(get_db)):
    rol = crud.delete_rol(db, rol_id)
    if not rol:
        raise HTTPException(status_code=404, detail="Rol no encontrado")
    return {"mensaje": "Rol eliminado correctamente"}