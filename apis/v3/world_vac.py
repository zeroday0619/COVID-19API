from fastapi import APIRouter
from app.Util import convertStruct
from app.Exceptions import APIException
from app.core.jhu import JHU
from app.Models.world_m import GlobalVaccinesResponseModel

world_vac = APIRouter()


@world_vac.get("/jhu/regions", response_model=GlobalVaccinesResponseModel)
async def get_global_vaccination_status():
    jhu = JHU()
    soucre = await jhu.fetch_country_vacc()
    if soucre is None:
        raise APIException(
            status=False,
            system={
                "message": "ERROR",
                "code": 500
            },
            soucre=None,
        )
    return await convertStruct(
        status=True,
        message="SUCCESS",
        code=200,
        source=soucre
    )