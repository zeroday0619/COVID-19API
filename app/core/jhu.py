from app.Util import CountryCodeUtil
from aiohttp import ClientSession
from app.Exceptions import APIException

class JHU:
    def __init__(self):
        self.url = "https://jhucoronavirus.azureedge.net/api/v1/regions/{}.json"
    
    @staticmethod
    async def refactor(source: dict):
        frame = {
            "country": source["country"],
            "data": {
                "confirmed_cases": source["confirmed_cases"],
                "confirmed_cases_records": source["confirmed_cases_records"],
                "deaths": source["deaths"],
                "deaths_records": source["deaths_records"]
            }
        }
        return frame

    async def fetch_country_status(self, alpha_3: str):
        cn = CountryCodeUtil.get_country_code(alpha_3)
        url = self.url.format(cn)
        async with ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    return await self.refactor(source=await response.json())
                else:
                    raise APIException(
                        status=False,
                        system={
                            "message": "Could not retrievethe JHU data for {}".format(alpha_3),
                            "code": response.status_code
                        },
                        source=None
                    )