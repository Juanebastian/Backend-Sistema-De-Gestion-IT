from sqlalchemy import Column, Integer, String, Date, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from app.db.database import Base



class SistemaOperativo(Base):
    __tablename__ = "sistemas_operativos"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), unique=True, nullable=False)

    computadores = relationship("Computador", back_populates="sistema_operativo")

