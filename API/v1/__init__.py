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
from app.crawler.euro import Euro
from app.ext.route.euroStatus import euroStatus
from app.ext.route.euroStatus import euroSelectStatus
import fastapi_plugins
import aioredis
import fastapi
import typing
import ujson


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


@router.get("/euro/status")
async def EuroCovid(cache: aioredis.Redis = fastapi.Depends(fastapi_plugins.depends_redis), ) -> typing.Dict:
    """유럽 COVID-19 현황 조회"""
    loop = Performance()
    da = Euro()
    sb = await euroStatus(loop=loop, cache=cache, db=da)
    return sb


@router.get("/euro/status/region/{select}")
async def EuroCOVID19(select: str, cache: aioredis.Redis = fastapi.Depends(
    fastapi_plugins.depends_redis), ) -> typing.Dict:
    """# 유럽 COVID-19 국가별 선택 현황 조회 [EU 회원국]
    ## 국가 코드\n
    AT	오스트리아\n
    BE	벨기에\n
    BG	불가리아\n
    CY	키프로스\n
    CZ	체코\n
    DE	독일\n
    DK	덴마크\n
    EE	에스토니아\n
    ES	스페인\n
    FI	핀란드\n
    FR	프랑스\n
    GB	영국\n
    GR	그리스\n
    HR	크로아티아\n
    HU	헝가리\n
    IE	아일랜드\n
    IT	이탈리아\n
    LT	리투아니아\n
    LU	룩셈부르크\n
    LV	라트비아\n
    MT	몰타\n
    NL	네덜란드\n
    PL	폴란드\n
    PT	포르투갈\n
    RO	루마니아\n
    SE	스웨덴\n
    SI	슬로베니아\n
    SK	슬로바키아
    """
    loop = Performance()
    da = Euro()
    source = await euroSelectStatus(loop=loop, cache=cache, db=da, select=select)
    return source