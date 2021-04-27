from fastapi import APIRouter
from .v3 import v3


root = APIRouter()
root.include_router(router=v3, prefix="/v3")
