# 3 - Intro to FastAPI
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def say_hello():
  return {"greeting": "Hello World!"}
