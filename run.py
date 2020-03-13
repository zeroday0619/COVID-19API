"""
:author: zeroday0619
:contact: zeroday0619(at)kakao.com
:copyright: Copyright 2020, zeroday0619
"""
import fastapi
import typing
import ujson
import pydantic
import aioredis
import fastapi_plugins
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from starlette.responses import RedirectResponse, Response
from app.crawler.mohw import GetInfectiousDiseasesbyRegion
from app.ext.KrCumulative import KrCumulativeInspection
from app.ext.KrStatusRegion import KrStatusRegion
from app.ext.Performance import Performance
from datetime import datetime, timedelta
from app.ext.krstatus import InspectionDetail
from app.ext.krstatus import krstatus
from app.ext.KrNews import KrNews
from app.ext.location import loc






__author__ = 'zeroday0619 <zeroday0619(at)kakao.com>'
__copyright__ = 'Copyright 2020, zeroday0619'

class OtherSettings(pydantic.BaseSettings):
    other: str = 'other'
class AppSettings(OtherSettings, fastapi_plugins.RedisSettings):
    api_name: str = str(__name__)

app = FastAPI(
	title="COVID-19 API",
	description="## 코로나 바이러스 감염증 -19 (COVID-19)의 국내 현황/뉴스 제공 API \n\n ### Project Repo: [Github](https://github.com/zeroday0619/COVID-19API)",
	version="2020.03.12 B3",
	debug=False
)
config = AppSettings()


@app.get("/")
async def RootGet(cache: aioredis.Redis=fastapi.Depends(fastapi_plugins.depends_redis),) -> typing.Dict:
	return RedirectResponse('/docs')


@app.get("/kr/status")
async def covidInfo(cache: aioredis.Redis=fastapi.Depends(fastapi_plugins.depends_redis),) -> typing.Dict:
	"""# 국내 COVID-19 현황
	## 대한민국 질병관리본부 
	-http://ncov.mohw.go.kr/

	"""
	loop = Performance()
	Result = await krstatus(cache=cache, loop=loop)
	return Result


@app.get("/kr/status/region")
async def covidIDR(cache: aioredis.Redis=fastapi.Depends(fastapi_plugins.depends_redis),) -> typing.Dict:
	"""# 지역 별 COVID-19 현황 조회
	## 대한민국 질병관리본부 
	-	http://ncov.mohw.go.kr/	
	"""
	loop = Performance()
	Result = await KrStatusRegion(cache=cache, loop=loop)
	return Result


@app.get("/kr/status/region/{location}")
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
	## 대한민국 질병관리본부 
	-	http://ncov.mohw.go.kr/
	"""
	data = GetInfectiousDiseasesbyRegion()
	loop = Performance()
	Result = await loc(location=location, data=data, loop=loop, cache=cache)
	return Result

@app.get("/kr/status/inspection")
async def CumulativeInspection(cache: aioredis.Redis=fastapi.Depends(fastapi_plugins.depends_redis),) -> typing.Dict:
	"""## 국내 검사 현황 | 누적 확진률"""
	loop = Performance()
	Result = await KrCumulativeInspection(loop=loop, cache=cache)
	return Result

@app.get("/kr/status/inspection/detail")
async def _InspectionDetail(cache: aioredis.Redis=fastapi.Depends(fastapi_plugins.depends_redis),) -> typing.Dict:
	"""## 국내 검사 현황 상세 조회"""
	loop = Performance()
	Result = await InspectionDetail(cache=cache, loop=loop)
	return Result

@app.get("/kr/news")
async def KrCoronaNews(cache: aioredis.Redis=fastapi.Depends(fastapi_plugins.depends_redis),) -> typing.Dict:
	"""## 국내 코로나 관련 뉴스를 제공.
		10분 간격으로 news 정보 업데이트 됩니다.
		## Naver News
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