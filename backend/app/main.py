

from fastapi import FastAPI
from backend.app.routes import platforms


app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "AI Platform Recommender API is running"}

app.include_router(platforms.router)
