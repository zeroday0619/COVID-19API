from fastapi import APIRouter
from API.v2.kr import kr_router

v2_router = APIRouter()

v2_router.include_router(router=kr_router, prefix="/kr")