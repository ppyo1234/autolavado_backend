from sqlalchemy import Column, Integer, String, Boolean, DateTime, Enum, Date, ForeignKey
from sqlalchemy.orm import relationship
from config.db import Base


class Usuario(Base):
    __tablename__ = "tbb_usuarios"
    id = Column(Integer, primary_key=True, index=True)
    rol_id = Column(Integer, ForeignKey("tbc_roles.Id"))
    nombre = Column(String(60))
    primer_apellido = Column(String(60))
    segundo_apellido = Column(String(60))
    direccion = Column(String(100))
    correo_electronico = Column(String(100))
    numero_telefono = Column(String(20))
    contrasena = Column(String(100))
    estatus = Column(Boolean, default=True)
    fecha_registro = Column(DateTime)
    fecha_actualizacion = Column(DateTime)

    servicios_realizados = relationship("AutoServicio", back_populates="usuario")