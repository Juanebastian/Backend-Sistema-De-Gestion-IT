from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.auth import LoginData, Token, UserCreate, UserOut
from app.services.auth_service import authenticate_user, crear_access_token, hash_password, crear_usuario
from app.db.database import get_db

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/login", response_model=Token)
def login(data: LoginData, db: Session = Depends(get_db)):
    user = authenticate_user(db, data.correo, data.contrasena)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Usuario o contraseña incorrecta")
    access_token = crear_access_token(data={"sub": str(user.id)})
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/register", response_model=UserOut)
def register(user_create: UserCreate, db: Session = Depends(get_db)):
    return crear_usuario(db, user_create)
