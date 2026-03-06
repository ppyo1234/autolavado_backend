from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class UsuarioBase(BaseModel):
    rol_id: int
    nombre: str
    primer_apellido: str
    segundo_apellido: str | None = None
    direccion: str | None = None
    correo_electronico: EmailStr
    numero_telefono: str | None = None
    estatus: bool = True

class UsuarioCreate(UsuarioBase):
    contrasena: str

class UsuarioUpdate(BaseModel):
    rol_id: int | None = None
    nombre: str | None = None
    primer_apellido: str | None = None
    segundo_apellido: str | None = None
    direccion: str | None = None
    correo_electronico: EmailStr | None = None
    numero_telefono: str | None = None
    estatus: bool | None = None
    contrasena: str | None = None

class Usuario(UsuarioBase):
    id: int
    fecha_registro: Optional[datetime] = None
    fecha_actualizacion: Optional[datetime] = None

    class Config:
        from_attributes = True

class UsuarioLogin(BaseModel):
    correo_electronico: str
    contrasena: str