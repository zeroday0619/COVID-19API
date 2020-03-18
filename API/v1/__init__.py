from fastapi import APIRouter, HTTPException
from app.ext.utils.Performance import Performance
from app.ext.route.KrCumulative import KrCumulativeInspection
from app.crawler.mohw import GetInfectiousDiseasesbyRegion
from app.ext.route.krstatus import InspectionDetail
from app.ext.route.KrStatusRegion import KrStatusRegion
from app.ext.route.location import loc
from app.ext.route.krstatus import krstatus
from app.ext.route.KrNews import KrNews
from app.ext.route.globalStatus import globalStatus
import fastapi_plugins
import aioredis
import fastapi
import typing


router = APIRouter()


@router.get("/kr/status")
async def covidInfo(cache: aioredis.Redis = fastapi.Depends(fastapi_plugins.depends_redis), ) -> typing.Dict:
    """# 국내 COVID-19 현황
	## 대한민국 질병관리본부
	-http://ncov.mohw.go.kr/

	"""
    loop = Performance()
    Result = await krstatus(cache=cache, loop=loop)
    return Result


@router.get("/kr/status/region")
async def covidIDR(cache: aioredis.Redis = fastapi.Depends(fastapi_plugins.depends_redis), ) -> typing.Dict:
    """# 지역 별 COVID-19 현황 조회
	## 대한민국 질병관리본부
	-	http://ncov.mohw.go.kr/
	"""
    loop = Performance()
    Result = await KrStatusRegion(cache=cache, loop=loop)
    return Result


@router.get("/kr/status/region/{location}")
async def ClassificationCOVID19(location: str, cache: aioredis.Redis = fastapi.Depends(
    fastapi_plugins.depends_redis), ) -> typing.Dict:
    """# 지역별 COVID-19 선택 현황 조회
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


@router.get("/kr/status/inspection")
async def CumulativeInspection(cache: aioredis.Redis = fastapi.Depends(fastapi_plugins.depends_redis), ) -> typing.Dict:
    """## 국내 검사 현황 | 누적 확진률"""
    loop = Performance()
    Result = await KrCumulativeInspection(loop=loop, cache=cache)
    return Result


@router.get("/kr/status/inspection/detail")
async def _InspectionDetail(cache: aioredis.Redis = fastapi.Depends(fastapi_plugins.depends_redis), ) -> typing.Dict:
    """## 국내 검사 현황 상세 조회"""
    loop = Performance()
    Result = await InspectionDetail(cache=cache, loop=loop)
    return Result


@router.get("/kr/news")
async def KrCoronaNews(cache: aioredis.Redis = fastapi.Depends(fastapi_plugins.depends_redis), ) -> typing.Dict:
    """## 국내 코로나 관련 뉴스를 제공.
		10분 간격으로 news 정보 업데이트 됩니다.
		## Naver News
	"""
    loop = Performance()
    Result = await KrNews(cache=cache, loop=loop)
    return Result

@router.get("/global/status")
async def KrCoronaNews(cache: aioredis.Redis = fastapi.Depends(fastapi_plugins.depends_redis), ) -> typing.Dict:
    """
	## 국가별 감염, 완치. 사망 정보 조회
	"""
    loop = Performance()
    data = await globalStatus(cache=cache, loop=loop)
    return data