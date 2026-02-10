from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from .schema_servicio import Servicio # Para anidar respuesta si quieres
from .schema_vehiculo import Vehiculo # Para anidar respuesta si quieres

class AutoservicioBase(BaseModel):
    vehiculo_id: int
    servicio_id: int
    observaciones: Optional[str] = None
    estado: str = "PENDIENTE" # PENDIENTE, EN_PROCESO, TERMINADO, PAGADO

class AutoservicioCreate(AutoservicioBase):
    pass

class AutoservicioUpdate(BaseModel):
    estado: Optional[str] = None
    observaciones: Optional[str] = None

class Autoservicio(AutoservicioBase):
    id: int
    fecha_ingreso: datetime
    fecha_fin: Optional[datetime] = None
    
    # Opcional: Si quieres devolver el objeto completo en lugar de solo el ID
    # servicio: Servicio 
    # vehiculo: Vehiculo

    class Config:
        orm_mode = True