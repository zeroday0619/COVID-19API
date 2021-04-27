from fastapi import APIRouter
from app.core import KDCA
from app.Util.converter import convertStruct
from app.Models import KRResponseModel
from app.Models import RegionListModel
from app.Models import KRTotalModel

kr = APIRouter()


@kr.get(path="/total", response_model=KRTotalModel)
async def total():
    kdca = KDCA()
    source = await kdca.get_total()
    return await convertStruct(
        source=source,
        status=True,
        code=200,
        message="OK"
    )


@kr.get(path="/get_regions", response_model=RegionListModel)
async def region_list():
    kdca = KDCA()
    source = await kdca.region_list()
    return await convertStruct(
        source=source,
        status=True,
        code=200,
        message="OK"
    )


@kr.get(path="/regions", response_model=KRResponseModel)
async def all_regions():
    kdca = KDCA()
    source = await kdca.covid_data()
    return await convertStruct(
        source=source,
        status=True,
        code=200,
        message="OK"
    )
