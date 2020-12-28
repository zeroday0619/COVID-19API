import typing
from fastapi import APIRouter, HTTPException
from app.ext import get_now_timestamp
from app.v2.crawler import KDCA
from API.v2.kr.interface import KDCAResponse, KDCAResponseX


kr_router = APIRouter()
source = KDCA()


@kr_router.get("/kdca/regionCases",
               response_model=KDCAResponse,
               name="KDCA All Region")
async def kdca_region_data() -> typing.Dict:
    """COVID-19 19 status in all cities and provinces"""
    soc: list = await source.covid_data()
    res = {
        "response": soc,
        "timestamp": get_now_timestamp()
    }
    return res


@kr_router.get("/kdca/specific/regionCases",
               response_model=KDCAResponse,
               name="KDCA Specific Region")
async def kdca_region_data_s(region: str) -> typing.Dict:
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


@kr_router.get("/kdca/specific/regionList",
               response_model=KDCAResponseX,
               name="KDCA Region List")
async def kdca_region_list() -> typing.Dict:
    so: dict = await source.region_list()
    data = {
        "response": so,
        "timestamp": get_now_timestamp()
    }
    return data
