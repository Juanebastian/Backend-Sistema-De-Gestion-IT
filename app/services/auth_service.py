from sqlalchemy.orm import Session
from app.db.models.usuario import Usuario
from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta
from app.schemas.auth import UserCreate

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

SECRET_KEY = "tu_clave_secreta_muy_segura"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def crear_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def authenticate_user(db: Session, correo: str, contrasena: str):
    user = db.query(Usuario).filter(Usuario.correo == correo).first()
    if not user:
        return None
    if not verify_password(contrasena, user.contrasena):
        return None
    return user


def crear_usuario(db: Session, user_create: UserCreate):
    user = db.query(Usuario).filter(Usuario.correo == user_create.correo).first()
    if user:
        raise Exception("Correo ya registrado")

    hashed_password = hash_password(user_create.contrasena)

    new_user = Usuario(
        nombre=user_create.nombre,
        cedula=user_create.cedula,
        correo=user_create.correo,
        contrasena=hashed_password,
        rol_id=user_create.rol_id,
        area_id=user_create.area_id  # si el campo es opcional
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user