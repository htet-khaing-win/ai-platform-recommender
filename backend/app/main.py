

from fastapi import FastAPI
from .routes import platforms, tools


app = FastAPI(title="AI Platform Recommender")

@app.get("/")
def read_root():
    return {"message": "AI Platform Recommender API is running"}

@app.get("/ping")
def ping():
    return {"message": "You just got pinged"}

app.include_router(platforms.router) #register platform
app.include_router(tools.router) #register tool
