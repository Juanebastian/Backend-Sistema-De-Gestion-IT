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
    nombre_marca: str
    modelo_id: int
    nombre_modelo: str
    sistema_operativo_id: int
    nombre_sistema_operativo: str
    tipo_id: int
    nombre_tipo: str
    area_id: int
    nombre_area: str
    id_registrado_por: int
    nombre_usuario: str

    ram: str
    disco_duro: str
    serie: str
    codigo_inventario: str
    fecha_adquisicion: date
    activo: bool

    fecha_creacion: datetime
    fecha_actualizacion: datetime

    class Config:
        orm_mode = True


class ComputadorOut(ComputadorBase):
    id: int
    fecha_creacion: datetime  # aquí mantenemos datetime para info completa
    fecha_actualizacion: datetime

    class Config:
        orm_mode = True
