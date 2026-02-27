from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config.db import engine, Base
from routes import routes_rol, routes_servicios, routes_usuario, routes_vehiculos, routes_vehiculos_servicios_usuarios, routes_auth

# Esto crea las tablas en la BD si no existen
Base.metadata.create_all(bind=engine)

app = FastAPI(title="API Autolavado")

# Configurar CORS para permitir peticiones desde el frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todos los orígenes (para pruebas locales)
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permite todos los headers
)

# Registrar los endpoints
app.include_router(routes_rol.router)
app.include_router(routes_servicios.router)
app.include_router(routes_usuario.router)
app.include_router(routes_vehiculos.router)
app.include_router(routes_vehiculos_servicios_usuarios.router)
app.include_router(routes_auth.router)

@app.get("/")
def read_root():
    return {"mensaje": "API de Autolavado funcionando correctamente"}