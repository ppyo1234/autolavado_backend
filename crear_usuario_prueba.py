from config.db import SessionLocal
from crud.crud_usuarios import create_usuario
from schemas.schema_usuario import UsuarioCreate
from models.rol import Rol
from datetime import datetime
import models.user as model

def crear_usuario_prueba():
    db = SessionLocal()
    try:
        # 1. Crear un rol de prueba si no existe
        rol = db.query(Rol).filter(Rol.NombreRol == "Admin").first()
        if not rol:
            rol = Rol(NombreRol="Admin", estado=True, fecha_registro=datetime.utcnow(), fecha_actualizacion=datetime.utcnow())
            db.add(rol)
            db.commit()
            db.refresh(rol)

        # 2. Verificar si el usuario ya existe
        usuario_existente = db.query(model.Usuario).filter(model.Usuario.correo_electronico == "admin@autolavado.com").first()
        if usuario_existente:
            print("=========================================")
            print("El usuario ya existe, usa estas credenciales:")
            print("Correo: admin@autolavado.com")
            print("Contrasena: admin123")
            print("=========================================")
            return

        # 3. Crear el usuario
        nuevo_usuario = UsuarioCreate(
            rol_id=rol.Id,
            nombre="Administrador",
            primer_apellido="Prueba",
            segundo_apellido="Sistema",
            direccion="Calle Falsa 123",
            correo_electronico="admin@autolavado.com",
            numero_telefono="5551234567",
            estatus=True,
            contrasena="admin123" # Contraseña fácil para pruebas
        )

        create_usuario(db, nuevo_usuario)
        print("=========================================")
        print("Usuario de prueba creado exitosamente.")
        print("Correo (o Teléfono): admin@autolavado.com / 5551234567")
        print("Contraseña: admin123")
        print("=========================================")

    except Exception as e:
        print(f"Error al crear usuario: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    crear_usuario_prueba()
