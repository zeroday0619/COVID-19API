from fastapi import APIRouter
from app.v2.crawler import KDCA


kr_router = APIRouter()
source = KDCA()


@kr_router.get("/kdca/region/all")
async def kdca_region_data():
    return await source.covid_data()


@kr_router.get("/kdca/region/select")
async def kdca_region_data_s(region):
    so = await source.covid_data()
    for ix in so:
        if ix['region'].lower() == region.lower():
            return ix
