from fastapi import APIRouter
from app.Util import convertStruct
from app.Exceptions import APIException
from app.core.ECDC import ECDC
from app.Models.europe_m import EuropaResponseModel
europe = APIRouter()


@europe.get("/ecdc/regions", response_model=EuropaResponseModel)
async def get_country_status_by_ecdc():
    ecdc = ECDC()
    source = await ecdc.last_records()
    if source is None:
        raise APIException(
            status=False,
            system={
                "message": f"The country does not exist in database",
                "code": 422
            }

        )
    return await convertStruct(
        status=True,
        code=200,
        message="Success",
        source=source
    )