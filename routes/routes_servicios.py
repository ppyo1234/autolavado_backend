from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
import crud.crud_servicios as crud
import schemas.schema_servicios as schema
import config.db

router = APIRouter(prefix="/servicios", tags=["Servicios"])


def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=list[schema.Servicio])
def listar_servicios(db: Session = Depends(get_db)):
    return crud.get_servicios(db)


@router.get("/{servicio_id}", response_model=schema.Servicio)
def obtener_servicio(servicio_id: int, db: Session = Depends(get_db)):
    servicio = crud.get_servicio_by_id(db, servicio_id)
    if not servicio:
        raise HTTPException(status_code=404, detail="Servicio no encontrado")
    return servicio


@router.post("/", response_model=schema.Servicio)
def crear_servicio(data: schema.ServicioCreate, db: Session = Depends(get_db)):
    return crud.create_servicio(db, data)


@router.put("/{servicio_id}", response_model=schema.Servicio)
def actualizar_servicio(servicio_id: int, data: schema.ServicioUpdate, db: Session = Depends(get_db)):
    servicio = crud.update_servicio(db, servicio_id, data)
    if not servicio:
        raise HTTPException(status_code=404, detail="Servicio no encontrado")
    return servicio


@router.delete("/{servicio_id}")
def eliminar_servicio(servicio_id: int, db: Session = Depends(get_db)):
    servicio = crud.delete_servicio(db, servicio_id)
    if not servicio:
        raise HTTPException(status_code=404, detail="Servicio no encontrado")
    return {"mensaje": "Servicio eliminado correctamente"}