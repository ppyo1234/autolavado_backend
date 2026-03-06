from pydantic import BaseModel
from datetime import datetime, time
from typing import Optional


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


class AutoServicio(BaseModel):
    as_id: int
    au_id: int
    se_id: int
    us_id: int
    as_fecha: datetime
    as_hora: time
    as_pagado: bool = False
    as_monto: float | None = None
    as_aprobado: bool = False

    class Config:
        from_attributes = True