from sqlalchemy.orm import declarative_base,relationship
from sqlalchemy import Column, String, Integer, ForeignKey
import uuid

Base = declarative_base()

class User(Base):
    __tablename__ ="users"
    __table_args__ = {"schema": "advance"}
    
    id = Column(String, Primary_key=True,default= lambda: str(uuid.uuid4()))
    user_name = Column(String,nullable=False)
    email_id  = Column(String,unique=True,nullable=False)

    posts = relationship("Post",back_populates="user")

class Post(Base):
    __tablename__ ="posts"
    __table_args__ = {"schema": "advance"}

    id= Column(String, Primary_key=True,default= lambda: str(uuid.uuid4()))
    user_id= Column(String , ForeignKey("advance.users.id"),nullable=False)
    title= Column(String, nullable=False)
    status= Column(String, default='draft')
    view= Column(Integer, default=0)

    user = relationship("User",back_populates="postS")
