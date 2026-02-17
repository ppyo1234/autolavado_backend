from pydantic import BaseModel
from datetime import datetime


class ServicioBase(BaseModel):
    nombre: str
    descripcion: str | None = None
    costo: float
    duracion: int | None = None
    estado: bool = True


class ServicioCreate(BaseModel):
    nombre: str
    descripcion: str | None = None
    costo: float
    duracion: int | None = None


class ServicioUpdate(BaseModel):
    nombre: str | None = None
    descripcion: str | None = None
    costo: float | None = None
    duracion: int | None = None
    estado: bool | None = None


class Servicio(ServicioBase):
    Id: int
    fecha_registro: datetime
    fecha_actualizacion: datetime

    class Config:
        orm_mode = True