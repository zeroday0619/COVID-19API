from fastapi import APIRouter
from app.Util import convertStruct
from app.core.jhu import JHU

world = APIRouter()


@world.get("/country/{alpha_3}")
async def get_country_status(alpha_3: str):
    jhu = JHU()
    return await convertStruct(
        status=True,
        code=200,
        message="Success",
        source=await jhu.fetch_country_status(alpha_3)
    )