from sqlalchemy import column, Integer , String, Boolean, DateTime, Enum, Date
from sqlalchemy.orm import relationship
from configure.db import Base

class User(Base):
    __tablename__ = "tbb_usuarios"
    Id = column(Integer, primary_key=True, index=True)
    Rol_Id = column(Integer,foreignkey="tbc_roles.Id")
    nombre = column(String(60))
    primer_apellido = column(String(60))
    segundo_apellido = column(String(60))
    direccion = column(String(100))
    correo_electronico = column(String(100))
    numero_telefono = column(String(20))
    contrasena = column(String(100))
    estatus = column(Boolean, default=True)
    fecha_registro = column(DateTime)
    fecha_actualizacion = column(DateTime)