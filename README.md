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