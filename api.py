from fastapi import FastAPI
from controllers import TestController

app = FastAPI()


@app.get("/")
async def welcome() -> dict:
    return {"message": "Welcome to the FastAPI world!"}
