from datetime import datetime
from typing import List
from fastapi import FastAPI
from fastapi.params import Depends
from conexion import SessionLocal, engine
from sqlalchemy.orm import Session
import model
import schema


model.Base.metadata.create_all(bind=engine)

app = FastAPI(title='API UrlSmartLink',
              description='API of urlsmartlink', version='0.1')

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.on_event('startup')
async def startup():
    print('Connecting...')


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/status")
def status():
    return 'Health - Ok'


@app.get('/apps/', response_model=List[schema.Apps])
def show_apps(db: Session = Depends(get_db)):
    apps = db.query(model.Apps).all()
    return apps


@app.post('/apps/', response_model=schema.Apps, summary="Guarda Id_usuario, nombre, fecha  en la tabla Apps")
def create_apps(insert: schema.Apps, db: Session = Depends(get_db)):
    apps = model.Apps(id_usuario=insert.id_usuario, nombre=insert.nombre)
    db.add(apps)
    db.commit()
    db.refresh(apps)
    return apps


@app.get('/apis/', response_model=List[schema.Apis])
def show_apis(db: Session = Depends(get_db)):
    apis = db.query(model.Apis).all()
    return apis


@app.post('/apis/', response_model=schema.Apis, summary="Guarda id_apps, id_usuario, id_estatus, ruta, descripcion, fecha  en la tabla Apps")
async def view(id_apps: int, id_usuario: int, id_status: bool, ruta: str, descripcion: str = None, db: Session = Depends(get_db)):
    """
        Detalles de los campos

        - **id**: Es autoincrement.
        - **id_apps**: Es la relación con la tabla Apps.
    """
    apis = model.Apis(id_apps=id_apps, id_usuario=id_usuario,
                      id_status=id_status, ruta=ruta, descripcion=descripcion)
    db.add(apis)
    db.commit()
    db.refresh(apis)
    return apis
# def create_apis(insert: schema.Apis, db: Session = Depends(get_db)):
#     apis = model.Apis(id_apps=insert.id_apps, id_usuario=insert.id_usuario,
#                       id_status=insert.id_status, ruta=insert.ruta, descripcion=insert.descripcion)
#     db.add(apis)
#     db.commit()
#     db.refresh(apis)
#     return apis
