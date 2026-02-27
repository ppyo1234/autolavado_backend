import os
from datetime import datetime, timedelta
from typing import Any, Union
from jose import jwt, JWTError
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from config.db import SessionLocal
import crud.crud_usuarios as crud_usuarios
import models.user as models

# Configuración de JWT
# En producción, SECRET_KEY debe estar en variables de entorno (.env)
SECRET_KEY = os.getenv("SECRET_KEY", "b3n9x8m2k1p4q7z5w6v8c2y1h4f9d3s7") 
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# OAuth2 esquema espera que el cliente envíe el token en el header "Authorization"
# con el valor "Bearer <token>"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_access_token(subject: Union[str, Any], expires_delta: timedelta = None) -> str:
    """Genera un token JWT."""
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    
    to_encode = {"exp": expire, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def get_current_user(
    db: Session = Depends(get_db), 
    token: str = Depends(oauth2_scheme)
) -> models.Usuario:
    """Extrae el usuario del token y verifica que exista base de datos."""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="No se pudieron validar las credenciales",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        correo_electronico: str = payload.get("sub")
        if correo_electronico is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
        
    user = crud_usuarios.get_usuario_by_correo(db, correo=correo_electronico)
    if user is None:
        raise credentials_exception
        
    return user

def get_current_active_user(
    current_user: models.Usuario = Depends(get_current_user)
) -> models.Usuario:
    """Asegura que el usuario autenticado esté activo."""
    if not current_user.estatus:
        raise HTTPException(status_code=400, detail="Usuario inactivo")
    return current_user
