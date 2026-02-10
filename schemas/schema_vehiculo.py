from pydantic import BaseModel
from typing import Optional

class VehiculoBase(BaseModel):
    placa: str
    marca: str
    modelo: str
    color: str
    tipo: str # Ej: Sedan, SUV, Camioneta

class VehiculoCreate(VehiculoBase):
    cliente_id: Optional[int] = None # Opcional si registras el auto sin cliente primero

class VehiculoUpdate(BaseModel):
    color: Optional[str] = None
    cliente_id: Optional[int] = None

class Vehiculo(VehiculoBase):
    id: int
    
    class Config:
        orm_mode = True