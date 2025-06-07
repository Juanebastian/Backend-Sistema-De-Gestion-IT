from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.database import Base
from zoneinfo import ZoneInfo

class Ticket(Base):
    __tablename__ = "tickets"
    id = Column(Integer, primary_key=True)
    asunto = Column(String(150), nullable=False)
    descripcion = Column(Text)
    estado_id = Column(Integer, ForeignKey("estados_ticket.id"), nullable=False)
    prioridad_id = Column(Integer, ForeignKey("prioridades_ticket.id"))
    id_creador = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    id_tecnico = Column(Integer, ForeignKey("usuarios.id"))
    fecha_creacion = Column(DateTime(timezone=True), default=lambda: datetime.now(ZoneInfo("America/Bogota")))
    fecha_actualizacion = Column(DateTime(timezone=True), default=lambda: datetime.now(ZoneInfo("America/Bogota")))
    fecha_cierre = Column(DateTime, nullable=True)
    area_id = Column(Integer, ForeignKey("areas.id"))
    observaciones = Column(Text)

    estado = relationship("Estado", backref="tickets")
    prioridad = relationship("Prioridad", backref="tickets")
    creador = relationship("Usuario", foreign_keys=[id_creador])
    tecnico = relationship("Usuario", foreign_keys=[id_tecnico])
    area = relationship("Area", backref="tickets")

class Estado(Base):
    __tablename__ = "estados_ticket"
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)

class Prioridad(Base):
    __tablename__ = "prioridades_ticket"
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
