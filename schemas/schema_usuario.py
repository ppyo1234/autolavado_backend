from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class UsuarioBase(BaseModel):
    Nombre:str
    primer_apellido:str
    segundo_apellido:str
    direccion:str
    correo_electronico:str
    numero_telefono:str
    contrasena:str
    estatus:bool
    fecha_registro:datetime
    fecha_actualizacion:datetime

class UsuarioCreate(UsuarioBase):
    pass

class UsuarioUpdate(UsuarioBase):
    pass

class Usuario(UsuarioBase):
    Id: int

    class Config:
        orm_mode = True

class UsuarioLogin(BaseModel):
    numero_telefono: str
    correo_electronico: str
    contrasena: str


