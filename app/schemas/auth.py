from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class LoginData(BaseModel):
    correo: EmailStr
    contrasena: str


class Token(BaseModel):
    access_token: str
    token_type: str


class UserCreate(BaseModel):
    nombre: str
    cedula: str
    correo: EmailStr
    contrasena: str
    rol_id: int
    area_id: Optional[int] = None  # si el área no es obligatoria


class UserOut(BaseModel):
    id: int
    nombre: str
    cedula: str
    correo: EmailStr
    rol_id: int
    area_id: Optional[int]
    activo: bool
    fecha_creacion: datetime

    class Config:
        orm_mode = True


class LoginResponse(BaseModel):
    success: bool
    message: str
    statusCode: int
    data: Token