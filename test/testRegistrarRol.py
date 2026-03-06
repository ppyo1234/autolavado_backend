import pytest

def test_crear_rol_exitoso(test_client, get_auth_token):
    headers = get_auth_token
    import uuid
    rol_nombre = f"Rol_{uuid.uuid4().hex[:5]}"

    payload = {
        "NombreRol": rol_nombre,
        "estado": True,
        "fecha_registro": "2024-01-01T00:00:00",
        "fecha_actualizacion": "2024-01-01T00:00:00"
    }
    response = test_client.post("/roles/", json=payload, headers=headers)
    assert response.status_code == 200

    data = response.json()
    assert data["NombreRol"] == payload["NombreRol"]
    assert data["estado"] == True

    assert "Id" in data

def test_crear_rol_datos_invalidos(test_client, get_auth_token):
    headers = get_auth_token

    payload_invalido = {"rol_id": "no-es-un-numero", "nombre": "Error"}
    response = test_client.post("/roles/", json=payload_invalido, headers=headers)
    assert response.status_code == 422
    