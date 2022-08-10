from datetime import datetime
from typing import List
from urllib import response
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

# ------- APPS --------
@app.get('/apps/', response_model=List[schema.Apps])
def show_apps(db: Session = Depends(get_db)):
    apps = db.query(model.Apps).all()
    return apps

@app.post('/apps/', response_model=schema.Apps, summary="Guarda Id_usuario, nombre, fecha  en la tabla Apps")
def create_apps(insert: schema.Apps, db:Session = Depends(get_db)):
    apps = model.Apps(id_usuario=insert.id_usuario, nombre=insert.nombre)
    db.add(apps)
    db.commit()
    db.refresh(apps)
    return apps

@app.put('/apps/{id}', response_model=schema.Apps)
def update_apps(id:int, update:schema.UpdateApps, db:Session= Depends(get_db)):
    apps = db.query(model.Apps).filter_by(id=id).first()
    apps.id_usuario=update.id_usuario
    apps.nombre=update.nombre
    db.commit()
    db.refresh(apps)
    return apps

@app.delete('/apps/{id}', response_model=schema.ResponseDelete)
def delete_apps(id:int, delete:schema.Apps, db:Session= Depends(get_db)):
    apps = db.query(model.Apps).filter_by(id=id).first()
    db.delete(apps)
    db.commit()
    response = schema.ResponseDelete(message='Eliminado del sistema')
    return response
# ------- /APPS --------

# ------- APIS ---------
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
@app.put('/apis/{id}', response_model=schema.Apis)
def update_apis(id:int, update:schema.UpdateApis, db:Session= Depends(get_db)):
    apis = db.query(model.Apis).filter_by(id=id).first()
    apis.id_apps=update.id_apps
    apis.id_usuario=update.id_usuario
    apis.id_status=update.id_status
    apis.ruta=update.ruta
    apis.descripcion=update.descripcion
    db.commit()
    db.refresh(apis)
    return apis

@app.delete('/apis/{id}', response_model=schema.ResponseDelete)
def delete_apis(id:int, delete:schema.Apis, db:Session= Depends(get_db)):
    apis = db.query(model.Apis).filter_by(id=id).first()
    db.delete(apis)
    db.commit()
    response = schema.ResponseDelete(message='Eliminado del sistema')
    return response
# ------- /APIS ---------

# ------- TOKEN ----------
@app.get('/token/', response_model=List[schema.Token])
def show_token(db: Session = Depends(get_db)):
    token = db.query(model.Token).all()
    return token

@app.post('/token/', response_model=schema.Token, summary="Guarda id_apps, id_clientes, id_clientes, token_jwt, estatus, fecha de creacion y fecha de actualización  en la tabla Token")
def create_token(insert: schema.Token, db: Session = Depends(get_db)):
    token = model.Token(id_apps=insert.id_apps, id_clientes=insert.id_clientes,
                        token_jwt=insert.token_jwt, estatus=insert.estatus)
    db.add(token)
    db.commit()
    db.refresh(token)
    return token
#@app.post('/token/', response_model=schema.Token, summary="Guarda id_apps, id_clientes, token_jwt, estatus, fecha de creacion y fecha de actualización  en la tabla Token")
# async def view(id_apps: int, id_clientes: int, token_jwt: str, estatus: bool, db: Session = Depends(get_db)):
#     """
#         Detalles de los campos

#         - **id**: Es autoincrement.
#         - **id_apps**: Es la relación con la tabla Apps.
#     """
#     token = model.Token(id_apps=id_apps, id_clientes=id_clientes, token_jwt=token_jwt,
#                         estatus=estatus)
#     db.add(token)
#     db.commit()
#     db.refresh(token)
#     return token

@app.put('/token/{id}', response_model=schema.Token)
def update_token(id:int, update:schema.UpdateToken, db:Session= Depends(get_db)):
    token = db.query(model.Token).filter_by(id=id).first()
    token.id_apps=update.id_apps
    token.id_clientes=update.id_clientes
    token.token_jwt=update.token_jwt
    token.estatus=update.estatus
    db.commit()
    db.refresh(token)
    return token

@app.delete('/token/{id}', response_model=schema.ResponseDelete)
def delete_token(id:int, delete:schema.Token, db:Session= Depends(get_db)):
    token = db.query(model.Token).filter_by(id=id).first()
    db.delete(token)
    db.commit()
    response = schema.ResponseDelete(message='Eliminado del sistema')
    return response
# ------- /TOKEN ----------

# ------- Cliente Apps --------
@app.get('/cliente_apps/', response_model=List[schema.Cliente_Apps])
def show_cliente_apps(db: Session = Depends(get_db)):
    cliente_apps = db.query(model.Cliente_Apps).all()
    return cliente_apps

@app.post('/cliente_apps/', response_model=schema.Cliente_Apps, summary="Guarda id_apps, id_clientes, fecha de creacion y fecha de actualización en la tabla Cliente_Apps")
def create_cliente_apps(insert: schema.Cliente_Apps, db: Session = Depends(get_db)):
    cliente_apps = model.Cliente_Apps(id_apps=insert.id_apps, id_clientes=insert.id_clientes)
    db.add(cliente_apps)
    db.commit()
    db.refresh(cliente_apps)
    return cliente_apps

# @app.post('/cliente_apps/', response_model=schema.Cliente_Apps, summary="Guarda id_apps, id_clientes en la tabla Cliente_Apps")
# async def view(id_apps: int, id_clientes: int, db: Session = Depends(get_db)):
#     """
#         Detalles de los campos

#         - **id**: Es autoincrement.
#         - **id_apps**: Es la relación con la tabla Apps.
#         - **id_clientes**: Es la relación con la tabla Clientes.
#     """
#     cliente_apps = model.Cliente_Apps(id_apps=id_apps, id_clientes=id_clientes)
#     db.add(cliente_apps)
#     db.commit()
#     db.refresh(cliente_apps)
#     return cliente_apps

@app.put('/cliente_apps/{id}', response_model=schema.Cliente_Apps)
def update_cliente_apps(id:int, update:schema.Update_Cliente_Apps, db:Session= Depends(get_db)):
    cliente_apps = db.query(model.Cliente_Apps).filter_by(id=id).first()
    cliente_apps.id_apps=update.id_apps
    cliente_apps.id_clientes=update.id_clientes
    db.commit()
    db.refresh(cliente_apps)
    return cliente_apps

@app.delete('/cliente_apps/{id}', response_model=schema.ResponseDelete)
def delete_cliente_apps(id:int, delete:schema.Cliente_Apps, db:Session= Depends(get_db)):
    cliente_apps = db.query(model.Cliente_Apps).filter_by(id=id).first()
    db.delete(cliente_apps)
    db.commit()
    response = schema.ResponseDelete(message='Eliminado del sistema')
    return response
# ------- /Cliente Apps --------
