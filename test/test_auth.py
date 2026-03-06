import pytest
from conftest import get_auth_token
from fastapi.testclient import TestClient

def test_login_exitoso(test_client):
    # Ya sabemos que el fixture get_auth_token crea un usuario de prueba en conftest.py
    # Así que vamos a crear nosotros mismos un usuario manual temporal para esta prueba
    import uuid
    unico = uuid.uuid4().hex[:6]
    correo = f"login_test_{unico}@autolavado.com"
    password = "password123"
    
    # Lo creamos directamente a través del cliente
    payload = {
        "nombre": "Test Login",
        "primer_apellido": "Apellido",
        "correo_electronico": correo,
        "contrasena": password,
        "rol_id": 1,
        "estatus": True
    }
    
    res_crear = test_client.post("/usuarios/", json=payload)
    assert res_crear.status_code == 200, "Falló al crear el usuario de prueba para login"
    user_id = res_crear.json()["id"]
    
    try:
        # Intentar el login con form data
        login_data = {"username": correo, "password": password}
        response = test_client.post("/login", data=login_data)
        
        assert response.status_code == 200
        data = response.json()
        assert "access_token" in data
        assert data["token_type"] == "bearer"
    finally:
        # Aquí no mandamos headers en el delete porque el delete en routes_usuario.py ocupa token
        # Voy a hacer el delete usando un token que acabamos de obtener
        if "access_token" in response.json():
            token = response.json()["access_token"]
            test_client.delete(f"/usuarios/{user_id}", headers={"Authorization": f"Bearer {token}"})


def test_login_credenciales_incorrectas(test_client):
    login_data = {"username": "nadie@invento.com", "password": "badpassword"}
    response = test_client.post("/login", data=login_data)
    
    assert response.status_code == 401
    assert response.json()["detail"] == "Correo o contraseña incorrectos"
