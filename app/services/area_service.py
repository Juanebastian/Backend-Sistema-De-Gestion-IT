from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.db.models.area import Area
from app.schemas.area import AreaCreate

def obtener_areas(db: Session):
    return db.query(Area).all()

def obtener_area_por_id(db: Session, area_id: int):
    area = db.query(Area).filter(Area.id == area_id).first()
    if not area:
        raise HTTPException(status_code=404, detail="Área no encontrada")
    return area

def crear_area(db: Session, area: AreaCreate):
    nueva_area = Area(nombre=area.nombre, ubicacion=area.ubicacion)
    db.add(nueva_area)
    db.commit()
    db.refresh(nueva_area)
    return nueva_area

def actualizar_area(db: Session, area_id: int, datos: AreaCreate):
    area = db.query(Area).filter(Area.id == area_id).first()
    if not area:
        raise HTTPException(status_code=404, detail="Área no encontrada")

    area.nombre = datos.nombre
    area.ubicacion = datos.ubicacion

    db.commit()
    db.refresh(area)
    return area

def eliminar_area(db: Session, area_id: int):
    area = db.query(Area).filter(Area.id == area_id).first()
    if not area:
        raise HTTPException(status_code=404, detail="Área no encontrada")

    db.delete(area)
    db.commit()
    return {"mensaje": "Área eliminada correctamente"}
