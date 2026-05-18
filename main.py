from fastapi import FastAPI
from app.config import APP_NAME, VERSION, DEFAULT_USER
from app.utils import get_welcome_message

app = FastAPI(title=APP_NAME, version=VERSION)

@app.get("/")
async def root():
    return {"message": get_welcome_message(DEFAULT_USER)}

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": get_welcome_message(name)}