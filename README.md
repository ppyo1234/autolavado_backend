# Autolavado Backend API

Esta es la API del sistema de gestión para el Autolavado, construida con **FastAPI**, **SQLAlchemy** y **MySQL**.

## Requisitos Previos
* Python 3.10 o superior instalado.
* Servidor MySQL ejecutándose de manera local (XAMPP, Workbench, etc.).
* Git instalado.

## Instalación y Configuración Paso a Paso

**1. Clonar el repositorio**
Abre tu terminal y clona este proyecto:
`git clone https://github.com/tu-usuario/autolavado_backend.git`
`cd autolavado_backend`

**2. Crear y activar el entorno virtual (Windows)**
Es indispensable usar un entorno virtual para no mezclar librerías:
`python -m venv venv`
`.\venv\Scripts\activate`

**3. Instalar las dependencias**
Con el entorno activado, instala todas las librerías necesarias:
`pip install -r requirements.txt`

**4. Crear la base de datos**
Abre tu gestor de MySQL y ejecuta el siguiente comando SQL para crear la base de datos vacía:
`CREATE DATABASE autolavado;`

**5. Configurar las variables de entorno**
Crea un archivo llamado `.env` en la raíz del proyecto (al mismo nivel que este README) y agrega tus credenciales de base de datos:
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=
DB_NAME=autolavado

## Ejecutar el Servidor

Una vez completados los pasos anteriores, levanta el servidor de desarrollo con:
`uvicorn main:app --reload`

El servidor construirá las tablas automáticamente la primera vez que arranque.

## Documentación y Pruebas
Para probar los *endpoints* (Crear usuarios, registrar vehículos, agendar servicios), abre tu navegador y visita la interfaz interactiva de Swagger:
👉 **http://127.0.0.1:8000/docs**

## Pruebas Unitarias (API Testing)
El proyecto cuenta con una suite completa de pruebas usando `pytest`. Para ejecutar las pruebas, utiliza los siguientes comandos desde la terminal en la raíz del proyecto (asegúrate de tener tu entorno virtual activado y tu servidor MySQL local corriendo):

**Ejecutar TODAS las pruebas (Recomendado):**
```powershell
.\venv\Scripts\python.exe -m pytest test/
```

**Ejecutar pruebas individualmente por componente:**
* **Autenticación (Login):**
  ```powershell
  .\venv\Scripts\python.exe -m pytest test/test_auth.py
  ```
* **Usuarios:**
  ```powershell
  .\venv\Scripts\python.exe -m pytest test/test_usuarios.py
  ```
* **Servicios:**
  ```powershell
  .\venv\Scripts\python.exe -m pytest test/test_servicios.py
  ```
* **Vehículos:**
  ```powershell
  .\venv\Scripts\python.exe -m pytest test/test_vehiculos.py
  ```
* **AutoServicios (Autos, Servicios, Cajeros y Operadores):**
  ```powershell
  .\venv\Scripts\python.exe -m pytest test/test_vehiculos_servicios.py
  ```

> 💡 **Tip extra:** Si quieres ver mensajes muuuucho más detallados sobre los errores cuando una prueba falla, o si necesitas visualizar los mensajes de `print()` que coloques en tu código, agrega los modificadores `-v -s` al final del comando.
> **Ejemplo:** `.\venv\Scripts\python.exe -m pytest test/ -v -s`