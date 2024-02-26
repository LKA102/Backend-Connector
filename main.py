from typing import Union
from fastapi import FastAPI
from db.session import Base, engine
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from routes.base import apiRouter

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(apiRouter)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)


if __name__ == "__main__":
    uvicorn.run("main:app", host="192.168.56.105", port=8000, reload=True)