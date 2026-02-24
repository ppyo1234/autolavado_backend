from pydantic import BaseModel, EmailStr
from datetime import datetime

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

class UsuarioUpdate(UsuarioBase):
    contrasena: str | None = None

class Usuario(UsuarioBase):
    Id: int
    fecha_registro: datetime | None = None
    fecha_actualizacion: datetime | None = None

    class Config:
        from_attributes = True

class UsuarioLogin(BaseModel):
    correo_electronico: str
    contrasena: str