'''Esta clase permite el modelo para los tipos de roles'''
from sqlalchemy import Column, Integer , String, Boolean, DateTime, Enum, Date
from sqlalchemy.orm import relationship
from configure.db import Base

class Rol(Base):
    __tablename__ = "tbc_roles"
    Id = Column(Integer, primary_key=True, index=True)
    NombreRol = Column(String(15))
    estado = Column(Boolean, default=True)
    fecha_registro = Column(DateTime)
    fecha_actualizacion = Column(DateTime)
