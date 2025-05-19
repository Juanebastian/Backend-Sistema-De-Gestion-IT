from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TicketBase(BaseModel):
    asunto: str
    descripcion: Optional[str]
    estado_id: int
    prioridad_id: Optional[int]
    id_creador: int
    id_tecnico: Optional[int]
    area_id: Optional[int]

class TicketCreate(TicketBase):
    pass

class TicketUpdate(TicketBase):
    fecha_cierre: Optional[datetime]

class TicketOut(TicketBase):
    id: int
    fecha_creacion: datetime
    fecha_actualizacion: datetime
    fecha_cierre: Optional[datetime]

    class Config:
        orm_mode = True
