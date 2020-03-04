from app.crawler.mohw import InfectiousDiseases
from app.crawler.naver import InfectiousDiseasesbyRegion
from fastapi import FastAPI
import fastapi
import typing
import pydantic
import fastapi_plugins
import aioredis

class OtherSettings(pydantic.BaseSettings):
    other: str = 'other'

class AppSettings(OtherSettings, fastapi_plugins.RedisSettings):
    api_name: str = str(__name__)


app = FastAPI()
config = AppSettings()
@app.get("/")
async def RootGet(cache: aioredis.Redis=fastapi.Depends(fastapi_plugins.depends_redis),) -> typing.Dict:
    return dict(ping=await cache.ping())

@app.on_event('startup')
async def on_startup() -> None:
    await fastapi_plugins.redis_plugin.init_app(app, config=config)
    await fastapi_plugins.redis_plugin.init()

@app.on_event('shutdown')
async def on_shutdown() -> None:
    await fastapi_plugins.redis_plugin.terminate()

@app.get("/info", tags=['info'])
async def covidInfo(cache: aioredis.Redis=fastapi.Depends(fastapi_plugins.depends_redis),) -> typing.Dict:
    data = InfectiousDiseases()
    Result = await data.Convert()
    return Result

@app.get("/idr", tags=['idr'])
async def covidIDR(cache: aioredis.Redis=fastapi.Depends(fastapi_plugins.depends_redis),) -> typing.Dict:
    data = InfectiousDiseasesbyRegion()
    result = await data.IDR()
    jsondata = {
        "info": result
    }
    return jsondata

