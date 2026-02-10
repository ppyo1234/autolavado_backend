from sqlchemy import Column, Integer, String, Boolean, DateTime,foreignkey
from configure.db import Base

class Vehiculo(Base):
    __tablename__ = "tbb_vehiculos"
    Id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer,foreignkey="tbb_usuarios.Id")
    marca = Column(String(50))
    modelo = Column(String(50))
    placa = Column(String(20))
    serie = Column(String(50))
    color = Column(String(20))
    tipo = Column(String(20))
    anio = Column(Integer)
    fecha_registro = Column(DateTime)
    fecha_actualizacion = Column(DateTime)