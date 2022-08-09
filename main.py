from typing import List
from fastapi import FastAPI
from fastapi.params import Depends
from conexion import SessionLocal, engine
from sqlalchemy.orm import Session
import model
import schema


model.Base.metadata.create_all(bind=engine)

app = FastAPI(title='API UrlSmartLink', description='API of urlsmartlink', version='0.1')
print("reiner", app)

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
def show_apps(db:Session=Depends(get_db)):
    apps = db.query(model.Apps).all()
    return apps

@app.post('/apps/', response_model=schema.Apps)
def create_apps(insert:schema.Apps,db:Session=Depends(get_db)):
    apps = model.Apps(id_usuario = insert.id_usuario, nombre=insert.nombre)
    db.add(apps)
    db.commit()
    db.refresh(apps)
    return apps