from fastapi import APIRouter
from app.core.data_go_kr import COVID_VACCINE_STAT
from app.Util.converter import convertStruct
from app.Models.kr import KRVacModel, KRVacRgsModel, RegionListModel
from app.Exceptions import APIException
from app.Models.exception import BaseExceptionToJsonModel
kr_vac = APIRouter()


@kr_vac.get(path="/total", response_model=KRVacModel)
async def all_regions():
    vac = COVID_VACCINE_STAT()
    source = await vac.fetch_korea_stat()
    return await convertStruct(
        source=source,
        status=True,
        code=200,
        message="OK"
    )


@kr_vac.get(path="/get_regions", response_model=RegionListModel)
async def region_list():
    vac = COVID_VACCINE_STAT()
    source = await vac.get_regions()
    return await convertStruct(
        source=source,
        status=True,
        code=200,
        message="OK"
    )


@kr_vac.get(path="/regions", response_model=KRVacRgsModel)
async def regions_status():
    vac = COVID_VACCINE_STAT()
    source = await vac.fetch_regions_stat()
    return await convertStruct(
        source=source,
        status=True,
        code=200,
        message="OK"
    )


@kr_vac.get(path="/region/{region}", response_model=KRVacModel, responses={422: {"model": BaseExceptionToJsonModel}})
async def region_status(region: str):
    vac = COVID_VACCINE_STAT()
    source = await vac.fetch_select_region(region)
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