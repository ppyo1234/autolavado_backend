from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import timedelta

import config.db
import crud.crud_usuarios as crud_usuarios
from utils.security import create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES
import schemas.schema_token as schema_token

router = APIRouter(tags=["Login"])

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/login", response_model=schema_token.Token)
def login_for_access_token(
    db: Session = Depends(get_db), 
    form_data: OAuth2PasswordRequestForm = Depends()
):
    # form_data.username puede recibir el correo o el teléfono en este caso,
    # ya que nuestra función `authenticate_user` acepta cualquiera de los dos
    username_clean = form_data.username.strip()
    password_clean = form_data.password.strip()
    user = crud_usuarios.authenticate_user(db, username_clean, password_clean)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Correo o contraseña incorrectos",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Si las credenciales son válidas, generamos el token JWT.
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        subject=user.correo_electronico, expires_delta=access_token_expires
    )
    
    return {"access_token": access_token, "token_type": "bearer"}
