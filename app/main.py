from fastapi import APIRouter
from .crawler.mohw import InfectiousDiseases
from .crawler.naver import InfectiousDiseasesbyRegion
covid = APIRouter()

@covid.get("/info", tags=['info'])
async def covidInfo():
    data = InfectiousDiseases()
    Result = await data.Convert()
    return Result

@covid.get("/idr", tags=['idr'])
async def covidIDR():
    data = InfectiousDiseasesbyRegion()
    result = await data.IDR()
    jsondata = {
        "info": result
    }
    return jsondata
