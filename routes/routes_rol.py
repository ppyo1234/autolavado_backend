from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud.crud_rol , schemas.schema_rol, config.db, models.model_rol

