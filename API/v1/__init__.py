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
from app.ext.route.globalStatus import GlobalCoronaStatus
from app.ext.route.globalStatus import GlobalCoronaSearch
from app.ext.route.usaStatus import UsaCovid19
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

@router.get("/global/status")
async def _globalStatus(cache: aioredis.Redis = fastapi.Depends(fastapi_plugins.depends_redis), ) -> typing.Dict:
    """
	## 국가별 감염, 완치. 사망 정보 조회
	"""
    loop = Performance()
    data = await globalStatus(cache=cache, loop=loop)
    return data


@router.get("/global/status/region/{country}")
async def _globalCoronaSearch(country: str, cache: aioredis.Redis = fastapi.Depends(fastapi_plugins.depends_redis), ) -> typing.Dict:
    """## COVID-19 Selection Status by Country
    ```
    china                   southkorea          sweden
    italy                   switzerland         iran
    unitedkingdom           spain               netherlands
    germany                 austria             unitedstates
    belgium                 france              norway
    denmark                 japan               malaysia
    canada                  portugal            diamondprincess
    australia               czechrepublic       israel
    brazil                  ireland             greece
    qatar                   pakistan            finland
    turkey                  poland              singapore
    chile                   luxembourg          iceland
    slovenia                indonesia           bahrain
    romania                 saudiarabia         thailand
    estonia                 ecuador             egypt
    philippines             hongkong            russia
    india                   iraq                lebanon
    southafrica             kuwait              peru
    sanmarino               unitedarabemirates  panama
    slovakia                armenia             mexico
    croatia                 colombia            taiwan
    bulgaria                serbia              cyprus
    argentina               algeria             costarica
    latvia                  vietnam             uruguay
    andorra                 brunei              hungary
    jordan                  albania             bosniaandherzegovina
    morocco                 srilanka            malta
    belarus                 moldova             northmacedonia
    palestinianauthority    azerbaijan          kazakhstan
    venezuela               georgia             oman
    tunisia                 newzealand          cambodia
    lithuania               senegal             dominicanrepublic
    burkinafaso             liechtenstein       uzbekistan
    afghanistan             kosovo              bangladesh
    macau                   ukraine             bolivia
    jamaica                 congodrc            cameroon
    honduras                nigeria             cuba
    ghana                   paraguay            monaco
    rwanda                  guatemala           ctedivoire
    trinidadandtobago       montenegro          ethiopia
    kenya                   mauritius           equatorialguinea
    mongolia                seychelles          tanzania
    barbados                guyana              bahamas
    congo                   gabon               namibia
    kyrgyzstan              benin               haiti
    liberia                 mauritania          saintlucia
    sudan                   zambia              antiguaandbarbuda
    bhutan                  chad                centralafricanrepublic
    djibouti                elsalvador          eswatini
    fiji                    guinea              nepal
    niger                   nicaragua           stvincentandthegrenadines
    somalia                 suriname            togo
    vaticancity             maldives
    ```
    """
    loop = Performance()
    data = await GlobalCoronaSearch(cache=cache, loop=loop,location=country)
    if not data:
        raise HTTPException(status_code=422, detail=f"Validation Error")
    return data


@router.get("/world/status")
async def _GlobalCoronaStatus(cache: aioredis.Redis = fastapi.Depends(fastapi_plugins.depends_redis), ) -> typing.Dict:
    """
	## 전세계 COVID-19 현황
	"""
    loop = Performance()
    data = await GlobalCoronaStatus(cache=cache, loop=loop)
    return data


@router.get("/global/status/usa")
async def _UsaCovid19(cache: aioredis.Redis = fastapi.Depends(fastapi_plugins.depends_redis), ) -> typing.Dict:
    source = UsaCovid19()
    usaL = await source.StatesCovidStatus(cache=cache)
    if not usaL:
        raise HTTPException(status_code=422, detail=f"Validation Error")
    return usaL


@router.get("/global/status/usa/{state}")
async def _UsaCovid19Status(state: str, cache: aioredis.Redis = fastapi.Depends(fastapi_plugins.depends_redis), ) -> typing.Dict:
    source = UsaCovid19()
    usa = await source.StatesCovidSearcher(cache=cache, state=state)
    if not usa:
        raise HTTPException(status_code=422, detail=f"Validation Error")
    return usa


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


@router.get("/kr/news")
async def KrCoronaNews(cache: aioredis.Redis = fastapi.Depends(fastapi_plugins.depends_redis), ) -> typing.Dict:
    """## 국내 코로나 관련 뉴스를 제공.
		10분 간격으로 news 정보 업데이트 됩니다.
		## Naver News
	"""
    loop = Performance()
    Result = await KrNews(cache=cache, loop=loop)
    return Result