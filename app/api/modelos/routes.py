# app/api/modelos/routes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services import modelo_service
from app.schemas.modelo import ModeloCreate, ModeloResponse
from app.db.database import get_db  # Asegúrate de que este exista

router = APIRouter(prefix="/modelos", tags=["modelos"])

@router.get("/", response_model=list[ModeloResponse])
def listar_modelos(db: Session = Depends(get_db)):
    return modelo_service.obtener_modelos(db)

@router.get("/{modelo_id}", response_model=ModeloResponse)
def obtener_modelo(modelo_id: int, db: Session = Depends(get_db)):
    modelo = modelo_service.obtener_modelo_por_id(db, modelo_id)
    if not modelo:
        raise HTTPException(status_code=404, detail="Modelo no encontrado")
    return modelo

@router.post("/", response_model=ModeloResponse)
def crear_modelo(modelo: ModeloCreate, db: Session = Depends(get_db)):
    return modelo_service.crear_modelo(db, modelo)

@router.delete("/{modelo_id}", response_model=ModeloResponse)
def eliminar_modelo(modelo_id: int, db: Session = Depends(get_db)):
    modelo = modelo_service.eliminar_modelo(db, modelo_id)
    if not modelo:
        raise HTTPException(status_code=404, detail="Modelo no encontrado")
    return modelo


@router.put("/{modelo_id}", response_model=ModeloResponse)
def actualizar_modelo(modelo_id: int, modelo: ModeloCreate, db: Session = Depends(get_db)):
    modelo_actualizado = modelo_service.actualizar_modelo(db, modelo_id, modelo)
    if not modelo_actualizado:
        raise HTTPException(status_code=404, detail="Modelo no encontrado")
    return modelo_actualizado