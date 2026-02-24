from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from config.db import Base 

class Vehiculo(Base):
    __tablename__ = "tbb_vehiculos"
    Id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer,ForeignKey("tbb_usuarios.Id"))
    marca = Column(String(50))
    modelo = Column(String(50))
    placa = Column(String(20))
    serie = Column(String(50))
    color = Column(String(20))
    tipo = Column(String(20))
    anio = Column(Integer)
    fecha_registro = Column(DateTime)
    fecha_actualizacion = Column(DateTime)