from sqlalchemy import Column, Integer, String, DECIMAL
from sqlalchemy.orm import relationship
from configure.db import Base

class Servicio(Base):
    __tablename__ = "c_servido"

    se_id = Column(Integer, primary_key=True, index=True)
    se_precio = Column(DECIMAL(18, 2))
    se_estatus = Column(String(45))
    se_descripcion = Column(String(850))
    se_nombre = Column(String(80))

    # Relación
    registros = relationship("AutoServicio", back_populates="servicio")