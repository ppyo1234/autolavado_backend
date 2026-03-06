import pytest
from fastapi.testclient import TestClient
from main import app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config.db import SessionLocal
import models.user as model_user
import models.rol as model_rol
from datetime import datetime

client = TestClient(app)

@pytest.fixture(scope="session")
def test_client():
    """Fixture para compartir el TestClient de la app FastAPI."""
    yield client

@pytest.fixture(scope="module")
def get_auth_token():
    """Fixture para crear un usuario de prueba en la BD y obtener su token Bearer.
       Se ejecuta una sola vez por módulo de prueba."""
    db = SessionLocal()
    
    # Crear un rol de prueba si no existe
    rol_test = db.query(model_rol.Rol).filter(model_rol.Rol.NombreRol == "TEST_ROLE").first()
    if not rol_test:
        rol_test = model_rol.Rol(NombreRol="TEST_ROLE", estado=True)
        db.add(rol_test)
        db.commit()
        db.refresh(rol_test)
    
    # Asegurarnos de borrar el usuario test si existia
    db_usuario = db.query(model_user.Usuario).filter(model_user.Usuario.correo_electronico == "admin@test.com").first()
    if db_usuario:
        db.delete(db_usuario)
        db.commit()
        
    # Crear usuario de prueba
    from passlib.context import CryptContext
    pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")
    hashed_password = pwd_context.hash("password_segura")
    
    nuevo_usuario = model_user.Usuario(
        rol_id=rol_test.Id,           
        nombre="Test",
        primer_apellido="User",
        segundo_apellido="Admin",
        direccion="Test Dir",
        correo_electronico="admin@test.com",
        numero_telefono="0000000000",
        estatus=True,
        contrasena=hashed_password,
        fecha_registro=datetime.utcnow(),
        fecha_actualizacion=datetime.utcnow()
    )
    db.add(nuevo_usuario)
    db.commit()
    
    # Iniciar sesion
    response = client.post("/login", data={
        "username": "admin@test.com",
        "password": "password_segura"
    })
    
    token = response.json().get("access_token")
    
    yield {"Authorization": f"Bearer {token}"}
    
    # Limpieza
    db.delete(nuevo_usuario)
    db.commit()
    
    # Solo borrar el rol de prueba si no hay otros usuarios usandolo
    usuarios_con_rol = db.query(model_user.Usuario).filter(model_user.Usuario.rol_id == rol_test.Id).count()
    if usuarios_con_rol == 0:
        db.delete(rol_test)
        db.commit()
        
    db.close()
