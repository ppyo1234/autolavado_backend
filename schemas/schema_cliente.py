from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ClienteBase(BaseModel):
    nombre: str
    telefono: str
    email: Optional[str] = None
    direccion: Optional[str] = None

class ClienteCreate(ClienteBase):
    pass

class ClienteUpdate(BaseModel):
    nombre: Optional[str] = None
    telefono: Optional[str] = None
    email: Optional[str] = None
    direccion: Optional[str] = None

class Cliente(ClienteBase):
    id: int
    fecha_registro: datetime

    class Config:
        orm_mode = True