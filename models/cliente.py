from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from configure.db import Base

class Cliente(Base):
    __tablename__ = "c_cliente"

    d_id = Column(Integer, primary_key=True, index=True) # ID según diagrama
    d_nombre = Column(String(60))
    d_apellidoMaterno = Column(String(60))
    d_apellidoPaterno = Column(String(60))
    d_direccion = Column(String(255))
    d_email = Column(String(55))
    d_telefono = Column(String(15))
    d_password = Column(String(750))

    # Relación con sus autos
    autos = relationship("Auto", back_populates="cliente")