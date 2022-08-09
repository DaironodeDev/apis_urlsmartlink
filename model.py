from sqlalchemy import Column, Integer, String, Boolean, DateTime
from conexion import Base
import datetime


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
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow)

class Token(Base):
    __tablename__ = 'token'
    id = Column(Integer, primary_key=True, index=True)
    id_apps = Column(Integer)
    id_clientes = Column(Integer)
    token_jwt = Column(String(100))
    estatus = Column(Boolean)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

class Clientes(Base):
    __tablename__ = 'clientes'
    id = Column(Integer, primary_key=True, index=True)
    secret_key = Column(String(50))
    nombre = Column(String(80))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

class Cliente_Apps(Base):
    __tablename__ = 'cliente_apps'
    id = Column(Integer, primary_key=True, index=True)
    id_apps = Column(Integer)
    id_clientes = Column(Integer)

