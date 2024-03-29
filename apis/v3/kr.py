from fastapi import APIRouter
from app.core import KDCA
from app.Util.converter import convertStruct
from app.Models import KRSelectResponseModel
from app.Models import KRResponseModel
from app.Models import RegionListModel
from app.Models import KRTotalModel
from app.Exceptions import APIException
from app.Models.exception import BaseExceptionToJsonModel

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


@kr.get(path="/region/{region}", response_model=KRSelectResponseModel, responses={422: {"model": BaseExceptionToJsonModel}})
async def select_region(region: str):
    kdca = KDCA()
    source = await kdca.selectRegion(region)
    if source is None:
        raise APIException(
            status=False,
            system={
                "message": f"Invalid region: {region}",
                "code": 422
            },
            source=None
        )
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
