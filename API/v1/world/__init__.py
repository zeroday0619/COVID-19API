from app.ext.route.world.globalStatus import GlobalCoronaStatus
from app.ext.route.world.globalStatus import GlobalCoronaSearch
from app.ext.route.world.globalStatus import globalStatus
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


@GlobalRouter.get("/status")
async def _globalStatus(cache: aioredis.Redis = fastapi.Depends(fastapi_plugins.depends_redis), ) -> typing.Dict:
    """
    ## 국가별 감염, 완치. 사망 정보 조회
    """
    data = await globalStatus(cache=cache, loop=loop)
    return data


@GlobalRouter.get("/status/{country}")
async def _globalCoronaSearch(country: str, cache: aioredis.Redis = fastapi.Depends(fastapi_plugins.depends_redis), ) -> typing.Dict:
    """## COVID-19 Selection Status by Country
    """
    data = await GlobalCoronaSearch(cache=cache, loop=loop, country=country)
    if not data:
        raise HTTPException(status_code=422, detail=f"Validation Error")
    return data


@GlobalRouter.get("/total/status")
async def _GlobalCoronaStatus(cache: aioredis.Redis = fastapi.Depends(fastapi_plugins.depends_redis), ) -> typing.Dict:
    """
    ## 전세계 COVID-19 현황
    """
    data = await GlobalCoronaStatus(cache=cache, loop=loop)
    return data