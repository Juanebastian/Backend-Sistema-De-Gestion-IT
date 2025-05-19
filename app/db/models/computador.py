from sqlalchemy import Column, Integer, String, Date, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from datetime import datetime
from app.db.models.area import Area
from app.db.models.marca import Marca
from app.db.models.modelo import Modelo
from app.db.models.os import SistemaOperativo
from app.db.database import Base



class TipoComputador(Base):
    __tablename__ = "tipos_computador"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50), unique=True, nullable=False)

    computadores = relationship("Computador", back_populates="tipo")


class Computador(Base):
    __tablename__ = "computadores"

    id = Column(Integer, primary_key=True, index=True)
    marca_id = Column(Integer, ForeignKey("marcas.id"))
    modelo_id = Column(Integer, ForeignKey("modelos.id"))
    sistema_operativo_id = Column(Integer, ForeignKey("sistemas_operativos.id"))
    tipo_id = Column(Integer, ForeignKey("tipos_computador.id"))
    area_id = Column(Integer, ForeignKey("areas.id"))
    id_registrado_por = Column(Integer, ForeignKey("usuarios.id"))

    ram = Column(String)
    disco_duro = Column(String)
    serie = Column(String)
    codigo_inventario = Column(String)
    fecha_adquisicion = Column(Date)
    activo = Column(Boolean, default=True)
    fecha_creacion = Column(DateTime, default=func.now())
    fecha_actualizacion = Column(DateTime, default=func.now(), onupdate=func.now())

    # Relaciones
    marca = relationship("Marca", back_populates="computadores")
    modelo = relationship("Modelo", back_populates="computadores")
    sistema_operativo = relationship("SistemaOperativo", back_populates="computadores")
    tipo = relationship("TipoComputador", back_populates="computadores")
    area = relationship("Area", backref="computadores")
    usuario = relationship("Usuario", backref="computadores", foreign_keys=[id_registrado_por])
