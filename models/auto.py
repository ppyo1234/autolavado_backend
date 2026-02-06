from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from configure.db import Base

class Auto(Base):
    __tablename__ = "c_auto"

    au_id = Column(Integer, primary_key=True, index=True)
    au_modelo = Column(String(45))
    au_matricula = Column(String(45))
    au_color = Column(String(45))
    au_Tipo = Column(String(45))
    
    # Llave foránea hacia c_cliente (usando d_id según diagrama)
    d_id = Column(Integer, ForeignKey("c_cliente.d_id"))

    # Relaciones
    cliente = relationship("Cliente", back_populates="autos")
    historial_servicios = relationship("AutoServicio", back_populates="auto")