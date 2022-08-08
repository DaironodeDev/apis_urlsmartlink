from datetime import date
from pydantic import BaseModel

class Apps(BaseModel):
    id = int
    id_usuario = int
    nombre = str
    created_at = date
    updated_at = date

    class Config:
        orm_mode = True
    
class Apis(BaseModel):
    id = int
    id_apps = int
    id_usuario = int
    id_status = int
    ruta = str
    descripcion = str
    created_at = date
    updated_at = date

    class Config:
        orm_mode = True