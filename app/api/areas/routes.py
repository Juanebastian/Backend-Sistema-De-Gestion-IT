from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.db.database import SessionLocal
from app.schemas.area import AreaCreate, AreaOut
from app.services.area_service import (
    obtener_areas,
    obtener_area_por_id,
    crear_area,
    actualizar_area,
    eliminar_area
)

router = APIRouter(prefix="/areas", tags=["areas"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[AreaOut])
def listar_areas(db: Session = Depends(get_db)):
    return obtener_areas(db)

@router.get("/{area_id}", response_model=AreaOut)
def obtener_area(area_id: int, db: Session = Depends(get_db)):
    return obtener_area_por_id(db, area_id)

@router.post("/", response_model=AreaOut)
def crear_nueva_area(area: AreaCreate, db: Session = Depends(get_db)):
    return crear_area(db, area)

@router.put("/{area_id}", response_model=AreaOut)
def actualizar_area_existente(area_id: int, area: AreaCreate, db: Session = Depends(get_db)):
    return actualizar_area(db, area_id, area)

@router.delete("/{area_id}")
def eliminar_area_por_id(area_id: int, db: Session = Depends(get_db)):
    return eliminar_area(db, area_id)