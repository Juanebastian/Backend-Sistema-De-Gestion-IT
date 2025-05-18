from pydantic import BaseModel
from typing import Optional


class AreaBase(BaseModel):
        nombre: str
        ubicacion: Optional[str]


class AreaCreate(AreaBase):
        pass


class AreaOut(AreaBase):
        id: int

        class Config:
                orm_mode = True

