from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.db.models.usuario import Usuario
from app.schemas.usuario import UsuarioCreate
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def obtener_todos_los_usuarios(db: Session):
    return db.query(Usuario).all()

def crear_usuario(db: Session, usuario: UsuarioCreate):
    # Verificar si el correo o cédula ya están registrados
    if db.query(Usuario).filter(Usuario.correo == usuario.correo).first():
        raise HTTPException(status_code=400, detail="Correo ya registrado")

    if db.query(Usuario).filter(Usuario.cedula == usuario.cedula).first():
        raise HTTPException(status_code=400, detail="Cédula ya registrada")

    nuevo_usuario = Usuario(
        nombre=usuario.nombre,
        cedula=usuario.cedula,
        correo=usuario.correo,
        contrasena=hash_password(usuario.contrasena),
        area_id=usuario.area_id,
        rol_id=usuario.rol_id,
        activo=usuario.activo
    )
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    return nuevo_usuario

def actualizar_usuario(db: Session, user_id: int, datos: UsuarioCreate):
    usuario = db.query(Usuario).filter(Usuario.id == user_id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    # Validar si el correo o cédula que se quieren actualizar ya existen para otro usuario
    if db.query(Usuario).filter(Usuario.correo == datos.correo, Usuario.id != user_id).first():
        raise HTTPException(status_code=400, detail="Correo ya registrado por otro usuario")

    if db.query(Usuario).filter(Usuario.cedula == datos.cedula, Usuario.id != user_id).first():
        raise HTTPException(status_code=400, detail="Cédula ya registrada por otro usuario")

    usuario.nombre = datos.nombre
    usuario.cedula = datos.cedula
    usuario.correo = datos.correo
    usuario.contrasena = hash_password(datos.contrasena)
    usuario.area_id = datos.area_id
    usuario.rol_id = datos.rol_id
    usuario.activo = datos.activo

    db.commit()
    db.refresh(usuario)
    return usuario
