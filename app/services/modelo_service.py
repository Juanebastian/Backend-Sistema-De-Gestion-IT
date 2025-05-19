# app/services/modelo_service.py
from sqlalchemy.orm import Session
from app.db.models.modelo import Modelo
from app.schemas.modelo import ModeloCreate

def obtener_modelos(db: Session):
    return db.query(Modelo).all()

def obtener_modelo_por_id(db: Session, modelo_id: int):
    return db.query(Modelo).filter(Modelo.id == modelo_id).first()

def crear_modelo(db: Session, modelo: ModeloCreate):
    db_modelo = Modelo(nombre=modelo.nombre)
    db.add(db_modelo)
    db.commit()
    db.refresh(db_modelo)
    return db_modelo

def eliminar_modelo(db: Session, modelo_id: int):
    modelo = db.query(Modelo).filter(Modelo.id == modelo_id).first()
    if modelo:
        db.delete(modelo)
        db.commit()
    return modelo
