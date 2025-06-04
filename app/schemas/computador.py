from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional

class ComputadorBase(BaseModel):
    marca_id: int
    modelo_id: int
    sistema_operativo_id: int
    tipo_id: int
    ram: str
    disco_duro: str
    serie: str
    codigo_inventario: str
    fecha_adquisicion: date
    activo: bool
    id_registrado_por: int
    area_id: int

class ComputadorCreate(ComputadorBase):
    pass


class ComputadorResponse(BaseModel):
    id: int
    marca_id: int
    modelo_id: int
    sistema_operativo_id: int
    tipo_id: int
    area_id: int
    id_registrado_por: int
    ram: str
    disco_duro: str
    serie: str
    codigo_inventario: str
    fecha_adquisicion: date
    activo: bool
    fecha_creacion: datetime
    fecha_actualizacion: datetime

    class Config:
        from_attributes = True  # <- Cambio aquí



class ComputadorOut(ComputadorBase):
    id: int
    fecha_creacion: datetime
    fecha_actualizacion: datetime

    class Config:
        from_attributes = True  # <- Cambio aquí
