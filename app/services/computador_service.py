from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.db.models.computador import Computador
from app.schemas.computador import ComputadorCreate, ComputadorResponse, ComputadorOut
from datetime import datetime
from typing import List

def obtener_todos_los_computadores(db: Session) -> List[ComputadorResponse]:
    computadores = db.query(Computador).all()
    return [ComputadorResponse.from_orm(c) for c in computadores]


def crear_computador(db: Session, computador: ComputadorCreate) -> ComputadorOut:
    existente = db.query(Computador).filter(
        (Computador.serie == computador.serie) |
        (Computador.codigo_inventario == computador.codigo_inventario)
    ).first()
    if existente:
        raise HTTPException(status_code=400, detail="Computador con serie o código de inventario ya existe")

    nuevo_computador = Computador(
        marca_id=computador.marca_id,
        modelo_id=computador.modelo_id,
        sistema_operativo_id=computador.sistema_operativo_id,
        tipo_id=computador.tipo_id,
        ram=computador.ram,
        disco_duro=computador.disco_duro,
        serie=computador.serie,
        codigo_inventario=computador.codigo_inventario,
        fecha_adquisicion=computador.fecha_adquisicion,
        activo=computador.activo,
        id_registrado_por=computador.id_registrado_por,
        area_id=computador.area_id,
    )
    db.add(nuevo_computador)
    db.commit()
    db.refresh(nuevo_computador)
    return nuevo_computador  # Pydantic con orm_mode lo transformará


def actualizar_computador(db: Session, computador_id: int, datos: ComputadorCreate) -> ComputadorOut:
    computador = db.query(Computador).filter(Computador.id == computador_id).first()
    if not computador:
        raise HTTPException(status_code=404, detail="Computador no encontrado")

    computador.marca_id = datos.marca_id
    computador.modelo_id = datos.modelo_id
    computador.sistema_operativo_id = datos.sistema_operativo_id
    computador.tipo_id = datos.tipo_id
    computador.ram = datos.ram
    computador.disco_duro = datos.disco_duro
    computador.serie = datos.serie
    computador.codigo_inventario = datos.codigo_inventario
    computador.fecha_adquisicion = datos.fecha_adquisicion
    computador.activo = datos.activo
    computador.id_registrado_por = datos.id_registrado_por
    computador.area_id = datos.area_id
    computador.fecha_actualizacion = datetime.now()

    db.commit()
    db.refresh(computador)
    return computador
