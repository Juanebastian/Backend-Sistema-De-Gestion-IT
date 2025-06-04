from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.auth import LoginData, Token, UserCreate, UserOut, LoginResponse
from app.services.auth_service import authenticate_user, crear_access_token, hash_password, crear_usuario
from app.db.database import get_db

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/login", response_model=LoginResponse)
def login(data: LoginData, db: Session = Depends(get_db)):
    user = authenticate_user(db, data.correo, data.contrasena)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Usuario o contraseña incorrecta")

    token = Token(
        access_token=crear_access_token(data={
            "id": user.id,
            "nombre": user.nombre,
            "correo": user.correo,
            "cedula": user.cedula,
            "rol_id": user.rol_id,
            "area_id": user.area_id,
        }),
        token_type="bearer"
    )

    return LoginResponse(
        success=True,
        message="Inicio de sesión exitoso",
        statusCode=200,
        data=token
    )

@router.post("/register", response_model=UserOut)
def register(user_create: UserCreate, db: Session = Depends(get_db)):
    return crear_usuario(db, user_create)
