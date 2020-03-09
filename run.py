"""
:author: zeroday0619
:contact: zeroday0619(at)kakao.com
:copyright: Copyright 2020, zeroday0619
"""
from app.crawler.mohw import GetInfectiousDiseasesbyRegion
from app.ext.Performance import Performance
from app.ext.location import loc
from app.ext.krstatus import krstatus
from app.ext.KrStatusRegion import KrStatusRegion
from app.ext.KrNews import KrNews
from datetime import datetime, timedelta
from fastapi import FastAPI
from pydantic import BaseModel
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

@app.get("/kr/status", tags=['/kr/status'])
async def covidInfo(cache: aioredis.Redis=fastapi.Depends(fastapi_plugins.depends_redis),) -> typing.Dict:
	"""# 국내 COVID-19 현황"""
	loop = Performance()
	Result = await krstatus(cache=cache, loop=loop)
	return Result


@app.get("/kr/status/region", tags=['/kr/status/region'])
async def covidIDR(cache: aioredis.Redis=fastapi.Depends(fastapi_plugins.depends_redis),) -> typing.Dict:
	"""# 지역 별 COVID-19 현황 조회"""
	loop = Performance()
	Result = await KrStatusRegion(cache=cache, loop=loop)
	return Result


@app.get("/kr/status/region/{location}", tags=['/kr/status/region/{location}'])
async def ClassificationCOVID19(location: str, cache: aioredis.Redis=fastapi.Depends(fastapi_plugins.depends_redis),) -> typing.Dict:
	"""# 시도별 COVID-19 선택 현황 조회
	## location
		- seoul		- chungbuk
		- busan		- chungnam
		- daegu		- jeonbuk
		- incheon	- jeonnam
		- gwangju	- gyeongbuk
		- daejeon	- gyeongnam
		- ulsan		- jeju
		- sejong	- gyeonggi
		- gangwon
	"""
	data = GetInfectiousDiseasesbyRegion()
	loop = Performance()
	Result = await loc(location=location, data=data, loop=loop, cache=cache)
	return Result

@app.get("/kr/news", tags=["/kr/news"])
async def KrCoronaNews(cache: aioredis.Redis=fastapi.Depends(fastapi_plugins.depends_redis),) -> typing.Dict:
	"""국내 코로나 관련 뉴스를 제공합니다.
		10분 간격으로 news 정보 업데이트 됩니다.
	"""
	loop = Performance()
	Result = await KrNews(cache=cache, loop=loop)
	return Result

@app.on_event('startup')
async def on_startup() -> None:
    await fastapi_plugins.redis_plugin.init_app(app, config=config)
    await fastapi_plugins.redis_plugin.init()

@app.on_event('shutdown')
async def on_shutdown() -> None:
    await fastapi_plugins.redis_plugin.terminate()