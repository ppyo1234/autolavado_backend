from sqlalchemy import Column, Integer, String, DECIMAL, Boolean, DateTime, ForeignKey
from config.db import Base

class estatus(Enum):
    Programado = "Programado"
    Proceso = "En proceso"
    Realizado = "Realizado"

class VehiculoServicio(Base):
    __tablename__ = "tbd_vehiculo_servicio_usuarios"
    Id = Column(Integer, primary_key=True, index=True)
    Vehiculo_Id = Column(Integer, ForeignKey("tbb_vehiculos.Id"))
    cajero_id = Column(Integer, ForeignKey("tbb_usuarios.Id"))
    operador_id = Column(Integer, ForeignKey("tbb_usuarios.Id"))
    servicio_id = Column(Integer, ForeignKey("c_servido.id"))
    fecha = Column(DateTime)
    hora = Column(DateTime)
    estatus = Column(Enum(estatus), default=estatus.Programado)

    estado = Column(String(20))
    fecha_registro = Column(DateTime)
    fecha_actualizacion = Column(DateTime)
