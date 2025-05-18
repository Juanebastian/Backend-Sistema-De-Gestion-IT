from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime

class ComputadorBase(BaseModel):
    marca: Optional[str]
    modelo: Optional[str]
    sistema_operativo: Optional[str]
    ram: Optional[str]
    disco_duro: Optional[str]
    tipo: Optional[str]  # Ej. 'Laptop', 'Desktop'
    serie: Optional[str]
    codigo_inventario: Optional[str]
    fecha_adquisicion: Optional[date]
    activo: Optional[bool] = True
    id_registrado_por: int
    area_id: Optional[int]

class ComputadorCreate(ComputadorBase):
    pass

class ComputadorOut(BaseModel):
    id: int
    marca: Optional[str]
    modelo: Optional[str]
    sistema_operativo: Optional[str]
    ram: Optional[str]
    disco_duro: Optional[str]
    tipo: Optional[str]
    serie: Optional[str]
    codigo_inventario: Optional[str]
    fecha_adquisicion: Optional[date]
    activo: bool
    id_registrado_por: int
    area_id: Optional[int]
    fecha_creacion: datetime
    fecha_actualizacion: datetime

    class Config:
        from_attributes = True  # Pydantic v2

class ComputadorResponse(ComputadorOut):
    nombre_usuario: Optional[str] = None
    nombre_area: Optional[str] = None

    class Config:
        from_attributes = True
