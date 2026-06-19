from fastapi import FastAPI, Depends
from config import engine,create_schema,SessionLocal
from database_models import Base
from sqlalchemy.orm import Session
import schemas
import crud


app = FastAPI()

#create schemas
create_schema()

#create tables 
Base.metadata.create_all(bind=engine)

def get_db():

    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@app.post("/users")
def create_user(user: schemas.UserCreate , db: Session = Depends(get_db)):
    return crud.create_user(
        db=db,
        user=user
    )

@app.post("/posts")
def create_post(post: schemas.PostCreate , db: Session = Depends(get_db)):
    return crud.create_post(
        db=db,
        post=post
    )

@app.get("/users")
def get_users(db:Session = Depends(get_db)):
    return crud.get_all_users(db)

@app.get("/posts")
def get_posts(db:Session = Depends(get_db)):
    return crud.get_all_posts(db)

@app.put("/users/{user_id}")
def update_user(user_id: str,user:schemas.UserUpdate,db:Session = Depends(get_db)):
    return crud.update_user(
        db=db,
        user_id=user_id,
        update_user=user
    )

@app.delete("/users/{user_id}")
def delete_user(user_id: str,db:Session = Depends(get_db)):
    return crud.delete_user(
        db = db,
        user_id= user_id
    )

@app.get("/users/{user_id}/posts")
def get_user_posts(user_id: str, db:Session = Depends(get_db)):
    return crud.get_user_posts(
        db=db,
        user_id=user_id
    )