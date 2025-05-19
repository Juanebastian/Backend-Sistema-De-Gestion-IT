from pydantic import BaseModel
from typing import Optional

class SistemaOperativoBase(BaseModel):
    nombre: str

class SistemaOperativoCreate(SistemaOperativoBase):
    pass

class SistemaOperativoResponse(SistemaOperativoBase):
    id: int

    class Config:
        from_attributes = True  # Equivale a orm_mode en Pydantic v1