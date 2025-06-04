from sqlalchemy.orm import Session
from app.db.models.os import SistemaOperativo
from app.schemas.os import SistemaOperativoCreate, SistemaOperativoUpdate


def obtener_sistemas_operativos(db: Session):
    return db.query(SistemaOperativo).all()

def obtener_sistema_operativo_por_id(db: Session, so_id: int):
    return db.query(SistemaOperativo).filter(SistemaOperativo.id == so_id).first()

def crear_sistema_operativo(db: Session, so: SistemaOperativoCreate):
    db_so = SistemaOperativo(nombre=so.nombre)
    db.add(db_so)
    db.commit()
    db.refresh(db_so)
    return db_so

def eliminar_sistema_operativo(db: Session, so_id: int):
    so = db.query(SistemaOperativo).filter(SistemaOperativo.id == so_id).first()
    if so:
        db.delete(so)
        db.commit()
    return so

def actualizar_sistema_operativo(db: Session, so_id: int, so_update: SistemaOperativoUpdate):
    so = db.query(SistemaOperativo).filter(SistemaOperativo.id == so_id).first()
    if not so:
        return None
    so.nombre = so_update.nombre
    db.commit()
    db.refresh(so)
    return so