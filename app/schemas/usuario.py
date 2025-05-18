from pydantic import BaseModel, EmailStr
from typing import Optional

class UsuarioBase(BaseModel):
    nombre: str
    cedula: str
    correo: EmailStr
    contrasena: str
    area_id: Optional[int]
    rol_id: int
    activo: Optional[bool] = True

class UsuarioCreate(UsuarioBase):
    pass

class UsuarioOut(BaseModel):
    id: int
    nombre: str
    cedula: str
    correo: EmailStr
    area_id: Optional[int]
    rol_id: int
    activo: bool

    class Config:
        orm_mode = True

class UsuarioResponse(BaseModel):
    id: int
    nombre: str
    cedula: str
    correo: EmailStr
    area_id: Optional[int]
    rol_id: int
    activo: bool
    nombre_rol: Optional[str] = None
    nombre_area: Optional[str] = None

    class Config:
        orm_mode = True
