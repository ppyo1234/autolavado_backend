from pydantic import BaseModel
from datetime import datetime

class VehiculoBase(BaseModel):
    usuario_id: int
    modelo: str
    marca: str
    placa: str
    serie: str | None = None
    color: str | None = None
    tipo: str | None = None
    anio: int | None = None
    estatus: bool = True


class VehiculoCreate(BaseModel):
    usuario_id: int
    modelo: str
    marca: str
    placa: str
    serie: str | None = None
    color: str | None = None
    tipo: str | None = None
    anio: int | None = None


class VehiculoUpdate(BaseModel):
    usuario_id: int | None = None
    modelo: str | None = None
    marca: str | None = None
    placa: str | None = None
    serie: str | None = None
    color: str | None = None
    tipo: str | None = None
    anio: int | None = None
    estatus: bool | None = None


class Vehiculo(VehiculoBase):
    id: int
    fecha_registro: datetime | None = None
    fecha_actualizacion: datetime | None = None

    class Config:
        orm_mode = True