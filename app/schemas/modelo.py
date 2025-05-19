# app/schemas/modelo.py
from pydantic import BaseModel
from typing import Optional

class ModeloBase(BaseModel):
    nombre: str

class ModeloCreate(ModeloBase):
    pass

class ModeloResponse(ModeloBase):
    id: int

    class Config:
        from_attributes = True  # en Pydantic v2, reemplaza orm_mode
