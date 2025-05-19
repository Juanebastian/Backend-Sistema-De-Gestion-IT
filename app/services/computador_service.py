from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.db.models.computador import Computador
from app.schemas.computador import ComputadorCreate, ComputadorResponse, ComputadorOut
from datetime import datetime
from typing import List

def obtener_todos_los_computadores(db: Session) -> List[ComputadorResponse]:
    computadores = db.query(Computador).all()
    resultado = []
    for c in computadores:
        resultado.append(
            ComputadorResponse(
                id=c.id,
                marca_id=c.marca_id,
                nombre_marca=c.marca.nombre,
                modelo_id=c.modelo_id,
                nombre_modelo=c.modelo.nombre,
                sistema_operativo_id=c.sistema_operativo_id,
                nombre_sistema_operativo=c.sistema_operativo.nombre,
                tipo_id=c.tipo_id,
                nombre_tipo=c.tipo.nombre,
                area_id=c.area_id,
                nombre_area=c.area.nombre,
                id_registrado_por=c.id_registrado_por,
                nombre_usuario=c.usuario.nombre if c.usuario else "Desconocido",
                ram=c.ram,
                disco_duro=c.disco_duro,
                serie=c.serie,
                codigo_inventario=c.codigo_inventario,
                fecha_adquisicion=c.fecha_adquisicion,
                activo=c.activo,
                fecha_creacion=c.fecha_creacion,
                fecha_actualizacion=c.fecha_actualizacion
            )
        )
    return resultado

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
