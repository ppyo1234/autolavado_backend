import pytest
import uuid

def test_crud_vehiculos_servicios(test_client, get_auth_token):
    headers = get_auth_token
    
    # 1. Preparar dependencias: Usuario (Cajero/Operador), Servicio, Vehiculo
    me_response = test_client.get("/usuarios/me", headers=headers)
    assert me_response.status_code == 200
    usuario_id = me_response.json()["id"]
    
    servicio_payload = {"nombre": "Test Service", "costo": 100.0, "duracion": 30}
    serv_res = test_client.post("/servicios/", json=servicio_payload, headers=headers)
    servicio_id = serv_res.json()["id"]
    
    placa = f"ABC-{uuid.uuid4().hex[:4]}".upper()
    vehiculo_payload = {"usuario_id": usuario_id, "modelo": "X", "marca": "Y", "placa": placa}
    veh_res = test_client.post("/vehiculos/", json=vehiculo_payload, headers=headers)
    vehiculo_id = veh_res.json()["id"]
    
    try:
        # 2. Crear AutoServicio (Relación)
        payload = {
            "vehiculo_id": vehiculo_id,
            "cajero_id": usuario_id,
            "operador_id": usuario_id,
            "servicio_id": servicio_id,
            "fecha": "2024-12-31T00:00:00",
            "hora": "14:30:00"
        }
    
        response = test_client.post("/vehiculos-servicios-usuarios/", json=payload, headers=headers)
        assert response.status_code == 200
        data = response.json()
        assert data["se_id"] == servicio_id  # <--- Cambiado a se_id
        registro_id = data["as_id"]          # <--- Cambiado a as_id
    
        # 3. Listar AutoServicios
        response_list = test_client.get("/vehiculos-servicios-usuarios/", headers=headers)
        assert response_list.status_code == 200
        assert any(r["as_id"] == registro_id for r in response_list.json())  # <--- Cambiado a as_id
        
        # 4. Obtener uno
        response_get = test_client.get(f"/vehiculos-servicios-usuarios/{registro_id}", headers=headers)
        assert response_get.status_code == 200
        assert response_get.json()["as_id"] == registro_id  # <--- Cambiado a as_id
    
        # 5. Actualizar AutoServicio
        payload_update = {
            "hora": "15:00:00"
        }
        response_update = test_client.put(f"/vehiculos-servicios-usuarios/{registro_id}", json=payload_update, headers=headers)
        assert response_update.status_code == 200
        
        # 6. Eliminar AutoServicio
        response_del = test_client.delete(f"/vehiculos-servicios-usuarios/{registro_id}", headers=headers)
        assert response_del.status_code == 200
    
    # 7. Verificar eliminación de AutoServicio
        response_get_deleted = test_client.get(f"/vehiculos-servicios-usuarios/{registro_id}", headers=headers)
        assert response_get_deleted.status_code == 404
        
    finally:
        # Limpiar dependencias SIEMPRE
        test_client.delete(f"/vehiculos/{vehiculo_id}", headers=headers)
        test_client.delete(f"/servicios/{servicio_id}", headers=headers)

def test_obtener_autoservicio_inexistente(test_client, get_auth_token):
    headers = get_auth_token
    response = test_client.get("/vehiculos-servicios-usuarios/999999", headers=headers)
    assert response.status_code == 404
