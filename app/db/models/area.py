from sqlalchemy import Column, Integer, String
from app.db.database import Base

class Area(Base):
        __tablename__ = "areas"
        id = Column(Integer, primary_key=True)
        nombre = Column(String)
        ubicacion = Column(String)