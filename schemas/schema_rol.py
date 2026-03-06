from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class RolBase(BaseModel):
    NombreRol: str
    estado: bool
    fecha_registro: Optional[datetime] = None
    fecha_actualizacion: Optional[datetime] = None


class RolCreate(RolBase):
    pass

class RolUpdate(RolBase):
    pass

class Rol(RolBase):
    Id: int

    class Config:
        orm_mode = True
        