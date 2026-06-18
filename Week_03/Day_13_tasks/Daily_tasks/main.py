from fastapi import FastAPI
from config import engine
from database_models import Base

app = FastAPI()


Base.metadata.create_all(bind=engine)