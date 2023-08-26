from sqlalchemy import Column, Integer, String
from declarative_base import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey


class Intérprete(Base):
    __tablename__ = 'intérprete'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    cancion_id = Column(Integer, ForeignKey('cancion.id'))
