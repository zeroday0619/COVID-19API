from fastapi import APIRouter
from .kr import kr

v3 = APIRouter()

v3.include_router(router=kr, prefix="/kr", tags=["Republic of Korea"])
