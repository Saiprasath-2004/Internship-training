from sqlalchemy.orm import Session
from database_models import User,Post
import schemas
from fastapi import HTTPException

def create_user(db:Session, user: schemas.UserCreate):
    existing = db.query(User).filter(User.email_id== user.email_id).first()
    if existing:
        raise HTTPException(
            status_code=409,
            detail="Email already Exists"
        )
    new_user = User(
        user_name =user.user_name,
        email_id = user.email_id,
        age=user.age
    )
    db.add(new_user)
    try:
        db.commit()
    except Exception:
        db.rollback()

        raise HTTPException(
            status_code=500,
            detail="Database Error"
        )
    db.refresh(new_user)
    return new_user

def create_post(db:Session, post:schemas.PostCreate):

    existing_user = db.query(User).filter(User.id== post.user_id).first()
    if not existing_user:
        raise HTTPException(
            status_code = 404,
            detail = "user not found"
        )
    new_post = Post(
        user_id = post.user_id,
        title = post.title,
        status = post.status,
        view = post.view
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

def get_all_users(db:Session):
    users = db.query(User).all()
    return users

def get_all_posts(db:Session):
    posts = db.query(Post).all()
    return posts

def update_user(db:Session,user_id: str,update_user:schemas.UserUpdate):
    existing_user = db.query(User).filter(User.id== user_id).first()
    if not existing_user:
        raise HTTPException(
            status_code = 404,
            detail="User not found"
        )
    
    existing_user.user_name = update_user.user_name
    existing_user.email_id = update_user.email_id

    db.commit()
    db.refresh(existing_user)
    return existing_user

def delete_user(db:Session,user_id: str):
    existing_user =db.query(User).filter(User.id == user_id).first()
    if not existing_user:
        raise HTTPException(
            status_code=404,
            detail = "User Not found"
        )
    db.delete(existing_user)
    db.commit()
    return {
        "message":"User deleted Successfully"
    }

def get_user_posts(db:Session,user_id:str):
    user = db.query(User).filter(User.id==user_id).first()

    if not user:
        raise HTTPException(
            status_code =404,
            detail="User not Found"
        )
    return user