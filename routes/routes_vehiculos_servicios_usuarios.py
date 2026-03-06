from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
import crud.crud_vehiculos_servicios_usuarios as crud
import schemas.schema_vehiculos_servicios_usuarios as schema
import config.db
from utils.security import get_current_active_user

router = APIRouter(
    prefix="/vehiculos-servicios-usuarios", 
    tags=["AutoServicio"],
    dependencies=[Depends(get_current_active_user)]
)


def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=list[schema.AutoServicio])
def listar(db: Session = Depends(get_db)):
    return crud.get_registros(db)


@router.get("/{registro_id}", response_model=schema.AutoServicio)
def obtener(registro_id: int, db: Session = Depends(get_db)):
    registro = crud.get_registro_by_id(db, registro_id)
    if not registro:
        raise HTTPException(status_code=404, detail="Registro no encontrado")
    return registro


@router.post("/", response_model=schema.AutoServicio)
def crear(data: schema.AutoServicioCreate, db: Session = Depends(get_db)):
    return crud.create_registro(db, data)


@router.put("/{registro_id}", response_model=schema.AutoServicio)
def actualizar(registro_id: int, data: schema.AutoServicioUpdate, db: Session = Depends(get_db)):
    registro = crud.update_registro(db, registro_id, data)
    if not registro:
        raise HTTPException(status_code=404, detail="Registro no encontrado")
    return registro


@router.delete("/{registro_id}")
def eliminar(registro_id: int, db: Session = Depends(get_db)):
    registro = crud.delete_registro(db, registro_id)
    if not registro:
        raise HTTPException(status_code=404, detail="Registro no encontrado")
    return {"mensaje": "Registro eliminado correctamente"}