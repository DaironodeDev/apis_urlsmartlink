from sqlalchemy import Column, Integer, String, Boolean, DateTime
from conexion import Base


class Apps(Base):
    __tablename__ = "apps"
    id = Column(Integer, primary_key=True, index=True)
    id_usuario = Column(Integer)
    nombre = Column(String(50))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    
class Apis(Base):
    __tablename__ = "apis"
    id = Column(Integer, primary_key=True, index=True)
    id_apps = Column(Integer)
    id_usuario = Column(Integer)
    id_status = Column(Boolean)
    ruta = Column(String(255))
    descripcion = Column(String(255))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

