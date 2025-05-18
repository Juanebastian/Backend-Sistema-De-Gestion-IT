from sqlalchemy import Column, Integer, String
from app.db.database import Base


class Role(Base):
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True)
    nombre = Column(String)

