from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class UsuarioBase(BaseModel):
    nombre: str
    email: EmailStr
    activo: bool = True
    rol_id: int # Relación con la tabla Rol

class UsuarioCreate(UsuarioBase):
    password: str # Solo pedimos password al crear

class UsuarioUpdate(BaseModel):
    nombre: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    activo: Optional[bool] = None
    rol_id: Optional[int] = None

class Usuario(UsuarioBase):
    id: int
    fecha_registro: datetime

    class Config:
        orm_mode = True