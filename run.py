"""
:author: zeroday0619
:contact: zeroday0619(at)kakao.com
:copyright: Copyright 2020, zeroday0619
"""
from app.crawler.mohw import InfectiousDiseases
from app.crawler.mohw import GetInfectiousDiseasesbyRegion
from app.crawler.utils.kcdcAPI import Performance
from datetime import datetime, timedelta
from fastapi import FastAPI
import fastapi
import typing
import ujson
import pydantic
import fastapi_plugins
import aioredis

__author__ = 'zeroday0619 <zeroday0619(at)kakao.com>'
__copyright__ = 'Copyright 2020, zeroday0619'

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
    loop = Performance()
    if not await cache.exists('info'):
        data = InfectiousDiseases()
        Result = await data.Convert()
        rs = {
            'info': Result
        }
        pb = await loop.run_in_threadpool(lambda: ujson.dumps(rs).encode('utf-8'))
        await cache.set('info', pb, expire=3600)
        return rs
    else:
        abc = await cache.get('info', encoding='utf-8')
        adad = await loop.run_in_threadpool(lambda: ujson.loads(abc))
        return adad

@app.get("/idr", tags=['idr'])
async def covidIDR(cache: aioredis.Redis=fastapi.Depends(fastapi_plugins.depends_redis),) -> typing.Dict:
    loop = Performance()
    if not await cache.exists('idr'):
        data = GetInfectiousDiseasesbyRegion()
        result = await data.SubCrawler()
        jsondata = {
            "idr": result
        }
        ob = await loop.run_in_threadpool(lambda: ujson.dumps(jsondata).encode('utf-8'))
        await cache.set('idr', ob, expire=3600)
        return jsondata
    else:
        abc = await cache.get('idr', encoding='utf-8')
        adad = await loop.run_in_threadpool(lambda: ujson.loads(abc))
        return adad