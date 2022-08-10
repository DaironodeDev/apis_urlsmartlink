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

class UpdateApps(BaseModel):
    id_usuario: int
    nombre: str
    updated_at: date

    class Config:
        orm_mode = True

class ResponseDelete(BaseModel):
    message: str

class Apis(BaseModel):
    id:Optional[int]
    id_apps: int
    id_usuario: int
    id_status: int
    ruta: str
    descripcion:Optional[str]
    created_at: date
    updated_at: date

    class Config:
        orm_mode = True

class UpdateApis(BaseModel):
    id_apps: int
    id_usuario: int
    id_status: int
    ruta: str
    descripcion: str
    updated_at: date

    class Config:
        orm_mode = True

class Token(BaseModel):
    id:Optional[int]
    id_apps: int
    id_clientes: int
    token_jwt: str
    estatus: bool
    created_at: date
    updated_at: date

    class Config:
        orm_mode = True

class UpdateToken(BaseModel):
    id_apps: int
    id_clientes: int
    token_jwt: str
    estatus: bool
    updated_at: date
    
class Clientes(BaseModel):
    id:Optional[int]
    secret_key: str
    nombre: str
    created_at: date
    updated_at: date

    class Config:
        orm_mode = True

class Cliente_Apps(BaseModel):
    id:Optional[int]
    id_apps: int
    id_clientes: int
    created_at: date
    updated_at: date

    class Config:
        orm_mode = True

class Update_Cliente_Apps(BaseModel):
    id_apps: int
    id_clientes: int
    update_at: date

    class Config:
        orm_mode = True


