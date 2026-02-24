from fastapi import FastAPI
from config.db import engine, Base
from routes import routes_rol, routes_servicios, routes_usuario, routes_vehiculos, routes_vehiculos_servicios_usuarios

# Esto crea las tablas en la BD si no existen
Base.metadata.create_all(bind=engine)

app = FastAPI(title="API Autolavado")

# Registrar los endpoints
app.include_router(routes_rol.router)
app.include_router(routes_servicios.router)
app.include_router(routes_usuario.router)
app.include_router(routes_vehiculos.router)
app.include_router(routes_vehiculos_servicios_usuarios.router)

@app.get("/")
def read_root():
    return {"mensaje": "API de Autolavado funcionando correctamente"}