from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.services.os_service import (
    obtener_sistemas_operativos,
    obtener_sistema_operativo_por_id,
    crear_sistema_operativo as servicio_crear_sistema_operativo,
    eliminar_sistema_operativo, actualizar_sistema_operativo
)
from app.schemas.os import SistemaOperativoCreate, SistemaOperativoResponse, SistemaOperativoUpdate
from app.db.database import get_db

router = APIRouter(prefix="/sistemas-operativos", tags=["sistemas operativos"])

@router.get("/", response_model=list[SistemaOperativoResponse])
def listar_sistemas_operativos(db: Session = Depends(get_db)):
    return obtener_sistemas_operativos(db)

@router.get("/{so_id}", response_model=SistemaOperativoResponse)
def obtener_sistema_operativo(so_id: int, db: Session = Depends(get_db)):
    so = obtener_sistema_operativo_por_id(db, so_id)
    if not so:
        raise HTTPException(status_code=404, detail="Sistema operativo no encontrado")
    return so

@router.post("/", response_model=SistemaOperativoResponse)
def crear_sistema_operativo(so: SistemaOperativoCreate, db: Session = Depends(get_db)):
    return servicio_crear_sistema_operativo(db, so)

@router.delete("/{so_id}", response_model=SistemaOperativoResponse)
def eliminar_sistema_operativo(so_id: int, db: Session = Depends(get_db)):
    so = eliminar_sistema_operativo(db, so_id)
    if not so:
        raise HTTPException(status_code=404, detail="Sistema operativo no encontrado")
    return so


@router.put("/{so_id}", response_model=SistemaOperativoResponse)
def actualizar_so(so_id: int, so_update: SistemaOperativoUpdate, db: Session = Depends(get_db)):
    so = actualizar_sistema_operativo(db, so_id, so_update)
    if not so:
        raise HTTPException(status_code=404, detail="Sistema operativo no encontrado")
    return so