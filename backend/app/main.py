# backend/app/main.py
from contextlib import asynccontextmanager
from fastapi import FastAPI
from .routes import platforms  # add other routers if available
from .database import initdb_async

@asynccontextmanager
async def lifespan(app: FastAPI):
    # create tables
    await initdb_async()
    yield

app = FastAPI(title="AI Platform Recommender", lifespan=lifespan)

@app.get("/")
async def read_root():
    return {"message": "AI Platform Recommender API is running"}

@app.get("/ping")
async def ping():
    return {"message": "You just got pinged"}

app.include_router(platforms.router)
