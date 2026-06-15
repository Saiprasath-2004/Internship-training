from fastapi import FastAPI

#creating FastAPI application object
app = FastAPI()

#first endpoint
@app.get("/")
def home():
    return {
        "message": "Welcome to FastAPI"
    }

#Second Endpoint
@app.get("/hello/{name}")
def greet(name:str):
    return{
        "message": f"Hello {name}"
    }