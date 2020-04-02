from app.ext.route.world.globalStatus import GlobalCoronaSearch
from fastapi import APIRouter, HTTPException
from app.ext.utils.Performance import Performance
import fastapi_plugins
import aioredis
import fastapi
import typing

loop = Performance()


class GlobalRouter(APIRouter()):
    def __init__(self):
        super().__init__()


@GlobalRouter.get("/status/{country}")
async def _globalCoronaSearch(country: str, cache: aioredis.Redis = fastapi.Depends(fastapi_plugins.depends_redis), ) -> typing.Dict:
    """## COVID-19 Selection Status by Country
    """
    data = await GlobalCoronaSearch(cache=cache, loop=loop, country=country)
    if not data:
        raise HTTPException(status_code=422, detail=f"Validation Error")
    return data