from fastapi import APIRouter
from .kr import kr
from .kr_vac import kr_vac
from .world import world
from .eu import europe
from .world_vac import world_vac

v3 = APIRouter()

v3.include_router(router=kr, prefix="/kr", tags=["Republic of Korea"])
v3.include_router(router=kr_vac, prefix="/kr/vaccination", tags=["Vaccination Status in Republic of Korea"])
v3.include_router(router=europe, prefix="/europe", tags=["Europe"])
v3.include_router(router=world, prefix="/global", tags=["Global"])
v3.include_router(router=world_vac, prefix="/global/vaccination", tags=["Global vaccination Status"])