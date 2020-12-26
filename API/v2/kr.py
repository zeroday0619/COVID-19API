from fastapi import APIRouter, HTTPException
from app.v2.crawler import KDCA
from app.ext import get_now_timestamp
from API.v2.kr_interface import KCDAResponseA


kr_router = APIRouter()
source = KDCA()


@kr_router.get("/kdca/region/all",
               response_model=KCDAResponseA,
               name="KDCA All Region")
async def kdca_region_data():
    """COVID-19 19 status in all cities and provinces"""
    soc: list = await source.covid_data()
    res = {
        "response": soc,
        "timestamp": get_now_timestamp()
    }
    return res


@kr_router.get("/kdca/region/specific",
               response_model=KCDAResponseA,
               name="KDCA Specific Region")
async def kdca_region_data_s(region: str):
    """COVID-19 status in specific cities and provinces."""
    so: list = await source.covid_data()
    for ix in so:
        if ix['region'].lower() == region.lower():
            res = {
                "response": [
                    ix
                ],
                "timestamp": get_now_timestamp()
            }
            return res
    raise HTTPException(status_code=404, detail="Requested region does not exist.")
