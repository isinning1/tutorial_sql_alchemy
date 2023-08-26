from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from sqlalchemy.orm import relationship
from declarative_base import Base
from enums import Medio  # Importamos la clase Medio desde el archivo enums.py

class Album(Base):
    __tablename__ = 'album'
    
    id = Column(Integer, primary_key=True)
    titulo = Column(String)
    año = Column(Integer)
    descripcion = Column(String)
    medio = Column(Enum(Medio))
    canciones = relationship('AlbumCancion', cascade='all, delete, delete-orphan')

class AlbumCancion(Base):
    __tablename__ = 'album_cancion'
    
    album_id = Column(Integer, ForeignKey('album.id'), primary_key=True)
    cancion_id = Column(Integer, ForeignKey('cancion.id'), primary_key=True)

