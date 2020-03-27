from app.ext.route.us.usaStatus import UsaCovid19
from fastapi import APIRouter, HTTPException
from app.ext.utils.Performance import Performance
import fastapi_plugins
import aioredis
import fastapi
import typing

loop = Performance()


class UsRouter(APIRouter()):
    def __init__(self):
        super().__init__()


@UsRouter.get("/status")
async def _UsaCovid19(cache: aioredis.Redis = fastapi.Depends(fastapi_plugins.depends_redis), ) -> typing.Dict:
    source = UsaCovid19()
    usaL = await source.StatesCovidStatus(cache=cache)
    if not usaL:
        raise HTTPException(status_code=422, detail=f"Validation Error")
    return usaL


@UsRouter.get("/status/{state}")
async def _UsaCovid19Status(state: str, cache: aioredis.Redis = fastapi.Depends(fastapi_plugins.depends_redis), ) -> typing.Dict:
    """
    비활성화
    """
    source = UsaCovid19()
    usa = await source.StatesCovidSearcher(cache=cache, state=state)
    if not usa:
        raise HTTPException(status_code=422, detail=f"Validation Error")
    return usa