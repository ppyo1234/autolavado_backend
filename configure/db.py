import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 1. Cargar las variables del archivo .env
load_dotenv()

# 2. Obtener las variables
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
db_name = os.getenv("DB_NAME")

# 3. Construir la URL dinámicamente
# Nota: A veces se requiere el driver, ej: mysql+pymysql://...
SQLALCHEMY_DATABASE_URL = f"mysql://{user}:{password}@{host}:{port}/{db_name}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Corregido: es sessionmaker, no sessionmarker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()