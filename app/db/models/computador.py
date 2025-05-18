from sqlalchemy import Column, Integer, String, Date, ForeignKey, DateTime , Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.database import Base
from app.db.models.area import Area

class Computador(Base):
    __tablename__ = "computadores"

    id = Column(Integer, primary_key=True, index=True)
    marca = Column(String(50))
    modelo = Column(String(50))
    sistema_operativo = Column(String(50))
    ram = Column(String(50))
    disco_duro = Column(String(50))
    tipo = Column(String(50))  # Laptop o Desktop
    serie = Column(String(50))
    codigo_inventario = Column(String(50), unique=True)
    fecha_adquisicion = Column(Date)
    activo = Column(Boolean, default=True, nullable=False)

    id_registrado_por = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    area_id = Column(Integer, ForeignKey("areas.id"))

    fecha_creacion = Column(DateTime, default=datetime.utcnow)
    fecha_actualizacion = Column(DateTime, default=datetime.utcnow)

    # Relaciones
    #usuario = relationship("Usuario", backref="computadores")
    #area = relationship("Area", backref="computadores")
