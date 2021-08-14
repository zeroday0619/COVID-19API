from fastapi import APIRouter
from app.core.data_go_kr import COVID_VACCINE_STAT
from app.Util.converter import convertStruct
from app.Models.kr import KRVacModel

kr_vac = APIRouter()


@kr_vac.get(path="/status", response_model=KRVacModel)
async def all_regions():
    vac = COVID_VACCINE_STAT()
    source = await vac.fetch_korea_stat()
    return await convertStruct(
        source=source,
        status=True,
        code=200,
        message="OK"
    )