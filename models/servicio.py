from sqlalchemy import Column, Integer, String, DECIMAL
from sqlalchemy.orm import relationship
from configure.db import Base

class Servicio(Base):
    __tablename__ = "c_servido"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50), nullable=False)
    descripcion = Column(String(200), nullable=True)
    costo = Column(DECIMAL(10, 2), nullable=False)
    duracion = Column(Integer, nullable=False)  
    estado = Column(Boolean, default=True)
    fecha_registro = Column(DateTime)
    fecha_actualizacion = Column(DateTime)