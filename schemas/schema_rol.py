from pydantic import BaseModel
from datetime import datetime

class RolBase(BaseModel):
    NombreRol: str
    estado: bool
    fecha_registro: datetime
    fecha_actualizacion: datetime


class RolCreate(RolBase):
    pass

class RolUpdate(RolBase):
    pass

class Rol(RolBase):
    Id: int

    class Config:
        