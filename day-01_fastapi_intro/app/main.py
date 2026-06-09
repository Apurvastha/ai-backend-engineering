from fastapi import FastAPI
from app.api import router


app = FastAPI(
    title = 'AI Backend Engineering',
    description='Day 1 Core API Service',
    version='0.1.0'
)

app.include_router(router)