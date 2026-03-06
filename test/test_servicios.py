import pytest

def test_crud_servicios(test_client, get_auth_token):
    headers = get_auth_token
    import uuid
    servicio_nombre = f"Lavado {uuid.uuid4().hex[:5]}"
    
    # 1. Crear servicio
    payload = {
        "nombre": servicio_nombre,
        "descripcion": "Lavado de prueba interactivo",
        "costo": 150.0,
        "duracion": 45
    }
    response = test_client.post("/servicios/", json=payload, headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert data["nombre"] == servicio_nombre
    assert data["costo"] == 150.0
    servicio_id = data["id"]
    
    # 2. Listar servicios
    response_list = test_client.get("/servicios/", headers=headers)
    assert response_list.status_code == 200
    assert any(s["id"] == servicio_id for s in response_list.json())
    
    # 3. Obtener servicio específico
    response_get = test_client.get(f"/servicios/{servicio_id}", headers=headers)
    assert response_get.status_code == 200
    assert response_get.json()["id"] == servicio_id
    
    # 4. Actualizar servicio
    payload_update = {
        "nombre": f"{servicio_nombre} VIP",
        "costo": 200.0,
        "duracion": 60,
        "estado": False
    }
    response_update = test_client.put(f"/servicios/{servicio_id}", json=payload_update, headers=headers)
    assert response_update.status_code == 200
    data_update = response_update.json()
    assert data_update["costo"] == 200.0
    assert data_update["nombre"] == payload_update["nombre"]
    
    # 5. Eliminar servicio
    response_del = test_client.delete(f"/servicios/{servicio_id}", headers=headers)
    assert response_del.status_code == 200
    
    # 6. Verificar eliminación exitosa
    response_get_deleted = test_client.get(f"/servicios/{servicio_id}", headers=headers)
    assert response_get_deleted.status_code == 404

def test_obtener_servicio_inexistente(test_client, get_auth_token):
    headers = get_auth_token
    response = test_client.get("/servicios/999999", headers=headers)
    assert response.status_code == 404
