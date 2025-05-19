from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.marca import MarcaCreate, MarcaOut, MarcaUpdate
from app.services.marca_service import (
    get_marcas,
    get_marca,
    create_marca,
    update_marca,
    delete_marca
)

router = APIRouter(
    prefix="/marcas",
    tags=["marcas"]
)

@router.get("/", response_model=list[MarcaOut])
def listar_marcas(db: Session = Depends(get_db)):
    return get_marcas(db)

@router.get("/{marca_id}", response_model=MarcaOut)
def obtener_marca(marca_id: int, db: Session = Depends(get_db)):
    marca = get_marca(db, marca_id)
    if not marca:
        raise HTTPException(status_code=404, detail="Marca no encontrada")
    return marca

@router.post("/", response_model=MarcaOut)
def crear_marca(marca: MarcaCreate, db: Session = Depends(get_db)):
    return create_marca(db, marca)

@router.put("/{marca_id}", response_model=MarcaOut)
def actualizar_marca(marca_id: int, marca: MarcaUpdate, db: Session = Depends(get_db)):
    db_marca = update_marca(db, marca_id, marca)
    if not db_marca:
        raise HTTPException(status_code=404, detail="Marca no encontrada")
    return db_marca

@router.delete("/{marca_id}", response_model=MarcaOut)
def eliminar_marca(marca_id: int, db: Session = Depends(get_db)):
    db_marca = delete_marca(db, marca_id)
    if not db_marca:
        raise HTTPException(status_code=404, detail="Marca no encontrada")
    return db_marca
