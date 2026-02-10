from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# Base: Campos compartidos
class ServicioBase(BaseModel):
    nombre: str
    descripcion: Optional[str] = None
    precio: float  

# Create: Lo que recibes al crear
class ServicioCreate(ServicioBase):
    pass

# Update: Todo opcional para permitir actualizaciones parciales
class ServicioUpdate(BaseModel):
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    precio: Optional[float] = None

# Response: Lo que devuelves al cliente (incluye ID y fechas)
class Servicio(ServicioBase):
    id: int
    fecha_registro: datetime
    fecha_actualizacion: Optional[datetime] = None

    class Config:
        orm_mode = True