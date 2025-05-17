# 12. Endpoints de Autenticación (app/api/auth/endpoints.py)

from typing import Any
from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.db.deps import get_db
from app.services.usuario_service import UsuarioService
from app.core.config import settings
from app.core.security import create_access_token
from app.schemas.token import Token

router = APIRouter()

@router.post("/login", response_model=Token)
def login_access_token(
    db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()
) -> Any:
    """
    OAuth2 compatible token login, obtiene un token de acceso para credenciales válidas.
    """
    usuario = UsuarioService.authenticate_usuario(
        db, username=form_data.username, password=form_data.password
    )
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario o contraseña incorrectos",
        )
    elif not usuario.es_activo:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Usuario inactivo"
        )
    
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    return {
        "access_token": create_access_token(
            usuario.id, expires_delta=access_token_expires
        ),
        "token_type": "bearer",
    }