from pydantic import BaseModel

class UserCreate(BaseModel):
    user_name: str
    email_id: str

class PostCreate(BaseModel):

    user_id: str
    title: str
    status: str = "draft"
    view: int = 0

class UserUpdate(BaseModel):

    user_name: str
    email_id: str