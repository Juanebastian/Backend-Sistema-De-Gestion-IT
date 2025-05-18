from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.services.usuario_service import obtener_todos_los_usuarios, crear_usuario, actualizar_usuario
from app.schemas.usuario import UsuarioCreate, UsuarioOut, UsuarioResponse
from typing import List

router = APIRouter(prefix="/usuarios", tags=["usuarios"])

# Dependency para obtener la sesión de BD
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=UsuarioOut)
def create_user(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    return crear_usuario(db, usuario)


@router.get("/", response_model=List[UsuarioResponse])
def show_users(db: Session = Depends(get_db)):
    return obtener_todos_los_usuarios(db)


@router.put("/{user_id}", response_model=UsuarioOut)
def update_user(user_id: int, usuario: UsuarioCreate, db: Session = Depends(get_db)):
    return actualizar_usuario(db, user_id, usuario)
