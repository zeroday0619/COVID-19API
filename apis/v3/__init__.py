from fastapi import APIRouter
from .kr import kr
from .kr_vac import kr_vac

v3 = APIRouter()

v3.include_router(router=kr, prefix="/kr", tags=["Republic of Korea"])
v3.include_router(router=kr_vac, prefix="/kr/vaccination", tags=["Vaccination Status in Republic of Korea"])