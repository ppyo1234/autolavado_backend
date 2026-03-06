import pytest

def test_crud_vehiculos(test_client, get_auth_token):
    headers = get_auth_token
    import uuid
    placa_prueba = f"XYZ-{uuid.uuid4().hex[:4]}".upper()
    
    # 1. Necesitamos un usuario_id válido para crear el vehículo
    # El usuario actual (del token) es admin@test.com
    me_response = test_client.get("/usuarios/me", headers=headers)
    assert me_response.status_code == 200
    usuario_id = me_response.json()["id"]
    
    # 2. Crear vehículo
    payload = {
        "usuario_id": usuario_id,
        "modelo": "Civic",
        "marca": "Honda",
        "placa": placa_prueba,
        "color": "Rojo",
        "tipo": "Sedán",
        "anio": 2020
    }
    response = test_client.post("/vehiculos/", json=payload, headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert data["placa"] == placa_prueba
    vehiculo_id = data["id"]
    
    # 3. Listar vehículos
    response_list = test_client.get("/vehiculos/", headers=headers)
    assert response_list.status_code == 200
    assert any(v["id"] == vehiculo_id for v in response_list.json())
    
    # 4. Obtener vehículo específico
    response_get = test_client.get(f"/vehiculos/{vehiculo_id}", headers=headers)
    assert response_get.status_code == 200
    assert response_get.json()["id"] == vehiculo_id
    
    # 5. Actualizar vehículo
    payload_update = {
        "color": "Azul",
        "anio": 2022
    }
    response_update = test_client.put(f"/vehiculos/{vehiculo_id}", json=payload_update, headers=headers)
    if response_update.status_code == 422: # Si fallara porque VehiculoUpdate exige algun campo
        pass
    assert response_update.status_code == 200
    data_update = response_update.json()
    assert data_update["color"] == "Azul"
    assert data_update["anio"] == 2022
    
    # 6. Eliminar vehículo
    response_del = test_client.delete(f"/vehiculos/{vehiculo_id}", headers=headers)
    assert response_del.status_code == 200
    
    # 7. Verificar eliminación
    response_get_deleted = test_client.get(f"/vehiculos/{vehiculo_id}", headers=headers)
    assert response_get_deleted.status_code == 404

def test_obtener_vehiculo_inexistente(test_client, get_auth_token):
    headers = get_auth_token
    response = test_client.get("/vehiculos/999999", headers=headers)
    assert response.status_code == 404
