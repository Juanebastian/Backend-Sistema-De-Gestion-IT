from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.db.models.computador import Computador
from app.schemas.computador import ComputadorCreate
from datetime import datetime

def obtener_todos_los_computadores(db: Session):
    return db.query(Computador).all()

def crear_computador(db: Session, computador: ComputadorCreate):
    nuevo_computador = Computador(
        marca=computador.marca,
        modelo=computador.modelo,
        sistema_operativo=computador.sistema_operativo,
        ram=computador.ram,
        disco_duro=computador.disco_duro,
        tipo=computador.tipo,
        serie=computador.serie,
        codigo_inventario=computador.codigo_inventario,
        fecha_adquisicion=computador.fecha_adquisicion,
        activo=computador.activo,
        id_registrado_por=computador.id_registrado_por,
        area_id=computador.area_id,
        fecha_creacion=datetime.now(),
        fecha_actualizacion=datetime.now()
    )

    db.add(nuevo_computador)
    db.commit()
    db.refresh(nuevo_computador)
    return nuevo_computador

def actualizar_computador(db: Session, computador_id: int, datos: ComputadorCreate):
    computador = db.query(Computador).filter(Computador.id == computador_id).first()
    if not computador:
        raise HTTPException(status_code=404, detail="Computador no encontrado")

    computador.marca = datos.marca
    computador.modelo = datos.modelo
    computador.sistema_operativo = datos.sistema_operativo
    computador.ram = datos.ram
    computador.disco_duro = datos.disco_duro
    computador.tipo = datos.tipo
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
