import pytest

def test_crud_usuarios(test_client, get_auth_token):
    headers = get_auth_token
    import uuid
    random_str = uuid.uuid4().hex[:6]
    correo_prueba = f"test_{random_str}@example.com"
    
    # Obtener el ID de un rol existente (el TEST_ROLE que crea el conftest sirve)
    roles_response = test_client.get("/roles/", headers=headers)
    assert roles_response.status_code == 200
    roles = roles_response.json()
    assert len(roles) > 0
    rol_id = roles[0]["Id"]
    
    # 1. Crear Usuario
    payload = {
        "rol_id": rol_id,
        "nombre": "Juan",
        "primer_apellido": "Pérez",
        "direccion": "Calle Falsa 123",
        "correo_electronico": correo_prueba,
        "numero_telefono": "5551234567",
        "contrasena": "MiPasswordSegura123"
    }
    response = test_client.post("/usuarios/", json=payload, headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert data["nombre"] == "Juan"
    assert data["correo_electronico"] == correo_prueba
    usuario_id = data["id"]
    
    # 2. Listar Usuarios
    response_list = test_client.get("/usuarios/", headers=headers)
    assert response_list.status_code == 200
    assert any(u["id"] == usuario_id for u in response_list.json())
    
    # 3. Obtener usuario actual (/me)
    # Debería devolver la información del "admin@test.com" del token
    response_me = test_client.get("/usuarios/me", headers=headers)
    assert response_me.status_code == 200
    assert response_me.json()["correo_electronico"] == "admin@test.com"
    
    # 4. Obtener usuario específico
    response_get = test_client.get(f"/usuarios/{usuario_id}", headers=headers)
    assert response_get.status_code == 200
    assert response_get.json()["id"] == usuario_id
    
    # 5. Intentar crear correo duplicado
    response_dup = test_client.post("/usuarios/", json=payload, headers=headers)
    assert response_dup.status_code == 400
    
    # 6. Actualizar usuario
    payload_update = {
        "nombre": "Juan Carlos",
        "numero_telefono": "5559876543",
        "estatus": False
    }
    response_update = test_client.put(f"/usuarios/{usuario_id}", json=payload_update, headers=headers)
    assert response_update.status_code == 200
    data_update = response_update.json()
    assert data_update["nombre"] == "Juan Carlos"
    assert data_update["numero_telefono"] == "5559876543"
    assert data_update["estatus"] == False
    
    # 7. Eliminar usuario
    response_del = test_client.delete(f"/usuarios/{usuario_id}", headers=headers)
    assert response_del.status_code == 200
    
    # 8. Verificar eliminación
    response_get_deleted = test_client.get(f"/usuarios/{usuario_id}", headers=headers)
    assert response_get_deleted.status_code == 404

def test_obtener_usuario_inexistente(test_client, get_auth_token):
    headers = get_auth_token
    response = test_client.get("/usuarios/999999", headers=headers)
    assert response.status_code == 404
