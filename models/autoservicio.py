from sqlalchemy import Column, Integer, Boolean, DateTime, Time, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship
from config.db import Base  # Recuerda que ya lo habíamos cambiado a config.db

class AutoServicio(Base):
    __tablename__ = "r_auto_servicio"

    as_id = Column(Integer, primary_key=True, index=True)
    
    # Llaves foráneas CORREGIDAS
    au_id = Column(Integer, ForeignKey("c_auto.au_id"))
    se_id = Column(Integer, ForeignKey("c_servido.id"))       # Cambiado de se_id a id
    us_id = Column(Integer, ForeignKey("tbb_usuarios.Id"))    # Cambiado a tbb_usuarios.Id
    
    # Columnas de datos
    as_fecha = Column(DateTime)
    as_pagado = Column(Boolean, default=False)
    as_monto = Column(DECIMAL(10, 2))
    as_aprobado = Column(Boolean, default=False)
    as_hora = Column(Time)

    # Relaciones
    auto = relationship("Auto", back_populates="historial_servicios")
    servicio = relationship("Servicio", back_populates="registros")
    usuario = relationship("Usuario", back_populates="servicios_realizados")