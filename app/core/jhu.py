from app.Util import CountryCodeUtil
from aiohttp import ClientSession
from app.Exceptions import APIException

class JHU:
    def __init__(self):
        self.url = "https://jhucoronavirus.azureedge.net/api/v1/regions/{}.json"
        self.url_vac = "https://jhucoronavirus.azureedge.net/jhucoronavirus/global_vaccines.json"
        self.headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.66"}
    
    @staticmethod
    async def refactor(source: dict):
        frame = {
            "country": source["country"],
            "data": {
                "confirmed_cases": source["confirmed_cases"],
                "deaths": source["deaths"],
                "records": { 
                    "confirmed_cases": source["confirmed_cases_records"],
                    "deaths": source["deaths_records"]
                }
            }
        }
        return frame

    async def fetch_country_vacc(self):
        async with ClientSession(headers=self.headers) as session:
            async with session.get(self.url_vac) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    raise APIException(
                        status=False,
                        system={
                            "message": "Could not retrieve the JHU data for vaccination",
                            "code": 500
                        },
                        source=None
                    )

    async def fetch_country_status(self, alpha_3: str):
        cn = CountryCodeUtil.get_country_code(alpha_3)
        url = self.url.format(cn)
        async with ClientSession(headers=self.headers) as session:
            async with session.get(url) as response:
                if response.status == 200:
                    return await self.refactor(source=await response.json())
                else:
                    raise APIException(
                        status=False,
                        system={
                            "message": "Could not retrievethe JHU data for {}".format(alpha_3),
                            "code": 500
                        },
                        source=None
                    )