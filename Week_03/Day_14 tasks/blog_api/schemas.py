from pydantic import BaseModel

# ---------- INPUT SCHEMAS ----------
## Create user 
class UserCreate(BaseModel):
    user_name: str
    email_id: str
    age: int
## Create Post
class PostCreate(BaseModel):

    user_id: str
    title: str
    status: str = "draft"
    view: int = 0

##Update User 
class UserUpdate(BaseModel):

    user_name: str
    email_id: str
    age: int



#-------Response Schemas-------#
class UserResponse(BaseModel):

    id: str
    user_name: str
    email_id: str
    age: int

    class Config:
        from_attributes = True

class PostResponse(BaseModel):

    id: str
    user_id: str
    title: str
    status: str
    view: int

    class Config:
        from_attributes= True

class UserWithPosts(BaseModel):
    id: str
    user_name: str
    email_id: str
    age: int
    posts: list[PostResponse]

    class Config:
        from_attributes = True