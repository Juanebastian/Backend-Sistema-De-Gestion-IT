from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.services.computador_service import (
    obtener_todos_los_computadores,
    crear_computador,
    actualizar_computador
)
from app.schemas.computador import ComputadorCreate, ComputadorOut, ComputadorResponse
from typing import List

router = APIRouter(prefix="/computadores", tags=["computadores"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=ComputadorOut)
def create_computador(computador: ComputadorCreate, db: Session = Depends(get_db)):
    return crear_computador(db, computador)

@router.get("/", response_model=List[ComputadorResponse])
def show_computadores(db: Session = Depends(get_db)):
    return obtener_todos_los_computadores(db)

@router.put("/{computador_id}", response_model=ComputadorOut)
def update_computador(computador_id: int, computador: ComputadorCreate, db: Session = Depends(get_db)):
    return actualizar_computador(db, computador_id, computador)
