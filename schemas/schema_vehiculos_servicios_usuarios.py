from pydantic import BaseModel
from datetime import datetime, time


class AutoServicioBase(BaseModel):
    vehiculo_id: int
    cajero_id: int
    operador_id: int
    servicio_id: int
    fecha: datetime
    hora: time
    estatus: bool = True


class AutoServicioCreate(BaseModel):
    vehiculo_id: int
    cajero_id: int
    operador_id: int
    servicio_id: int
    fecha: datetime
    hora: time


class AutoServicioUpdate(BaseModel):
    vehiculo_id: int | None = None
    cajero_id: int | None = None
    operador_id: int | None = None
    servicio_id: int | None = None
    fecha: datetime | None = None
    hora: time | None = None
    estatus: bool | None = None


class AutoServicio(AutoServicioBase):
    id: int
    fecha_registro: datetime
    fecha_actualizacion: datetime

    class Config:
        orm_mode = True