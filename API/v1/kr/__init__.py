from app.ext.route.kr.KrCumulative import KrCumulativeInspection
from app.crawler.kr.mohw import GetInfectiousDiseasesRegion
from app.ext.route.kr.krstatus import InspectionDetail
from app.ext.route.kr.KrStatusRegion import KrStatusRegion
from app.ext.route.kr.location import loc
from app.ext.route.kr.krstatus import krstatus
from app.ext.route.kr.KrNews import KrNews
from fastapi import APIRouter, HTTPException
from app.ext.utils.Performance import Performance
import fastapi_plugins
import aioredis
import fastapi
import typing

loop = Performance()


class KrRouter(APIRouter()):
    def __init__(self):
        super().__init__()


#@KrRouter.get("/status")
#async def COVID19Status(cache: aioredis.Redis = fastapi.Depends(fastapi_plugins.depends_redis), ) -> typing.Dict:
#    """# 국내 COVID-19 현황
#    ## 대한민국 질병관리본부
#    -http://ncov.mohw.go.kr/
#
#    """
#    Result = await krstatus(cache=cache, loop=loop)
#    return Result


@KrRouter.get("/status/region")
async def covidIDR(cache: aioredis.Redis = fastapi.Depends(fastapi_plugins.depends_redis), ) -> typing.Dict:
    """# 지역 별 COVID-19 현황 조회
    ## 대한민국 질병관리본부
    -	http://ncov.mohw.go.kr/
    """
    Result = await KrStatusRegion(cache=cache, loop=loop)
    return Result


#@KrRouter.get("/status/region/{location}")
#async def ClassificationCOVID19(location: str, cache: aioredis.Redis = fastapi.Depends(fastapi_plugins.depends_redis), ) -> typing.Dict:
#    """# 지역별 COVID-19 선택 현황 조회
#    ## location
#        - seoul		- chungbuk
#        - busan		- chungnam
#        - daegu		- jeonbuk
#        - incheon	- jeonnam
#        - gwangju	- gyeongbuk
#        - daejeon	- gyeongnam
#        - ulsan		- jeju
#        - sejong	- gyeonggi
#        - gangwon
#    ## 대한민국 질병관리본부
#    -	http://ncov.mohw.go.kr/
#    """
#    data = GetInfectiousDiseasesRegion()
#    Result = await loc(location=location, data=data, loop=loop, cache=cache)
#    return Result
#

@KrRouter.get("/status/inspection")
async def CumulativeInspection(cache: aioredis.Redis = fastapi.Depends(fastapi_plugins.depends_redis), ) -> typing.Dict:
    """## 국내 검사 현황 | 누적 확진률"""
    Result = await KrCumulativeInspection(loop=loop, cache=cache)
    return Result


#@KrRouter.get("/status/inspection/detail")
#async def _InspectionDetail(cache: aioredis.Redis = fastapi.Depends(fastapi_plugins.depends_redis), ) -> typing.Dict:
#    """## 국내 검사 현황 상세 조회"""
#    Result = await InspectionDetail(cache=cache, loop=loop)
#    return Result


@KrRouter.get("/news")
async def KrCoronaNews(cache: aioredis.Redis = fastapi.Depends(fastapi_plugins.depends_redis), ) -> typing.Dict:
    """## 국내 코로나 관련 뉴스를 제공.
        10분 간격으로 news 정보 업데이트 됩니다.
        ## Naver News
    """
    Result = await KrNews(cache=cache, loop=loop)
    return Result