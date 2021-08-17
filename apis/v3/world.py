from fastapi import APIRouter
from app.Util import convertStruct
from app.Exceptions import APIException
from app.core.jhu import JHU
from app.Models.world_m import GlobalModel
from app.Models.exception import BaseExceptionToJsonModel

world = APIRouter()


@world.get("/jhu/region/{alpha_3}", response_model=GlobalModel, responses={422: {"model": BaseExceptionToJsonModel}})
async def get_country_status(alpha_3: str):
    """There is a difference of 2 days in the data obtained from JHU CSSE COVID-19 Data."""
    jhu = JHU()
    source = await jhu.fetch_country_status(alpha_3)
    if source is None:
        raise APIException(
            status=False,
            system={
                "message": f"The country with alpha_3: {alpha_3} does not exist in database",
                "code": 422
            },
            source=None

        )
    return await convertStruct(
        status=True,
        code=200,
        message="Success",
        source=source
    )
