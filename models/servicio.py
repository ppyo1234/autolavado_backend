from sqlalchemy import Column, Integer, String, DECIMAL, Boolean, DateTime
from sqlalchemy.orm import relationship
from config.db import Base

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

    
    registros = relationship("AutoServicio", back_populates="servicio")