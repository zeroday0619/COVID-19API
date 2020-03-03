from fastapi import APIRouter
from .crawler.mohw import InfectiousDiseases

covid = APIRouter()

@covid.get("/info", tags=['info'])
async def covidInfo():
    data = InfectiousDiseases()
    Result = await data.Convert()
    return Result