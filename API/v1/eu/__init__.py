from app.crawler.eu.euro import Euro
from app.ext.route.eu.euroStatus import euroStatus
from app.ext.route.eu.euroStatus import euroSelectStatus
from fastapi import APIRouter, HTTPException
from app.ext.utils.Performance import Performance
import fastapi_plugins
import aioredis
import fastapi
import typing


class EuropeRouter(APIRouter()):
    def __init__(self):
        super().__init__()


loop = Performance()
euro = Euro()


@EuropeRouter.get("/euro/status")
async def EuroCovid(cache: aioredis.Redis = fastapi.Depends(fastapi_plugins.depends_redis), ) -> typing.Dict:
    """유럽 COVID-19 현황 조회"""
    sb = await euroStatus(loop=loop, cache=cache, db=euro)
    return sb


@EuropeRouter.get("/euro/status/region/{select}")
async def EuroCOVID19(select: str, cache: aioredis.Redis = fastapi.Depends(fastapi_plugins.depends_redis), ) -> typing.Dict:
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
    source = await euroSelectStatus(loop=loop, cache=cache, db=euro, select=select)
    return source