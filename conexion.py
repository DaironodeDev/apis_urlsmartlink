from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

user = 'root'
password = 'Hug*Sql7024'
server = 'localhost'
port = '3306'
database = 'api_urlsmartlink'


DATABASE_URL = "mysql+mysqlconnector://"+user+":"+password+"@"+server+":"+port+"/"+database

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
