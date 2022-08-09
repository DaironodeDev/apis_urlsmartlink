from datetime import date
from typing import Optional
from pydantic import BaseModel


class Apps(BaseModel):
    id:Optional[int]
    id_usuario: int
    nombre: str
    created_at: date
    updated_at: date

    class Config:
        orm_mode = True


class Apis(BaseModel):
    id: int
    id_apps: int
    id_usuario: int
    id_status: int
    ruta: str
    descripcion: str
    created_at: date
    updated_at: date

    class Config:
        orm_mode = True

class Token(BaseModel):
    id: int
    id_apps: int
    id_clientes: int
    token_jwt: str
    estatus: bool
    created_at: date
    updated_at: date

    class Config:
        orm_mode: True
    
class Clientes(BaseModel):
    id: int
    secret_key: str
    nombre: str
    created_at: date
    updated_at: date

    class Config:
        orm_mode: True

class Cliente_Apps(BaseModel):
    id: int
    id_apps: int
    id_clientes: int


