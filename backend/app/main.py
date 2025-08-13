

from fastapi import FastAPI
from .routes import platforms


app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "AI Platform Recommender API is running"}

@app.get("/ping")
def ping():
    return {"message": "You just got pinged"}

app.include_router(platforms.router)
