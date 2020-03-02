from fastapi import FastAPI
from app.main import covid

app = FastAPI()
app.include_router(
    covid,
    prefix="/v1"
)