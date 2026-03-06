import os
import sys

# Asegurar que el directorio raíz del proyecto esté en sys.path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from config.db import SessionLocal, engine, Base
from models.model_rol import Rol
from models.model_servicios import Servicio
from models.model_usuario import Usuario
from models.model_vehiculos import Vehiculo
from models.model_vehiculos_servicios_usuarios import AutoServicio
from passlib.context import CryptContext
from datetime import datetime

pwd = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")


def main():
    # Asegurar tablas
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()
    try:
        # Crear rol
        admin = Rol(nombre="Admin")
        db.add(admin)
        db.commit()
        db.refresh(admin)
        print("Rol creado:", getattr(admin, 'Id', None))

        # Crear servicio
        s = Servicio(nombre="Lavado Completo", descripcion="Lavado y encerado", costo=25.0, duracion=45)
        db.add(s)
        db.commit()
        db.refresh(s)
        print("Servicio creado:", getattr(s, 'Id', None))

        # Crear usuario
        hashed = pwd.hash("secret")
        u = Usuario(rol_id=admin.Id, nombre="Juan", primer_apellido="Perez", correo_electronico="juan@example.com", contrasena=hashed)
        db.add(u)
        db.commit()
        db.refresh(u)
        print("Usuario creado:", getattr(u, 'id', None))

        # Crear vehiculo
        v = Vehiculo(usuario_id=u.id, modelo="Model S", marca="Tesla", placa="ABC123")
        db.add(v)
        db.commit()
        db.refresh(v)
        print("Vehiculo creado:", getattr(v, 'id', None))

        # Crear autoservicio
        asv = AutoServicio(vehiculo_id=v.id, cajero_id=u.id, operador_id=u.id, servicio_id=s.Id, fecha=datetime.now(), hora=datetime.now().time())
        db.add(asv)
        db.commit()
        db.refresh(asv)
        print("AutoServicio creado:", getattr(asv, 'id', None))

        # Mostrar totales
        roles = db.query(Rol).count()
        usuarios = db.query(Usuario).count()
        servicios = db.query(Servicio).count()
        vehiculos = db.query(Vehiculo).count()
        autos = db.query(AutoServicio).count()
        print("Totales - roles:", roles, "usuarios:", usuarios, "servicios:", servicios, "vehiculos:", vehiculos, "autos:", autos)

    finally:
        db.close()


if __name__ == "__main__":
    main()