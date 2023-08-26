from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from declarative_base import Base

class Cancion(Base):
    __tablename__ = 'cancion'
    
    id = Column(Integer, primary_key=True)
    titulo = Column(String)
    minutos = Column(Integer)
    segundos = Column(Integer)
    compositor = Column(String)
    
    interpretes = relationship('Intérprete', cascade='all, delete, delete-orphan')
    albumes = relationship('AlbumCancion', cascade='all, delete, delete-orphan')

class AlbumCancion(Base):
    __tablename__ = 'album_cancion'
    
    album_id = Column(Integer, ForeignKey('album.id'), primary_key=True)
    cancion_id = Column(Integer, ForeignKey('cancion.id'), primary_key=True)

