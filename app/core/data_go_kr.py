import asyncio

from covid_vaccine_stat import async_request
from covid_vaccine_stat.model import VACCINE_STAT_API
from covid_vaccine_stat.model import VACCINE_STAT_MODEL
from app.config import COVID_VACCINE_STAT_API_KEY
from app.Models.dgk import VAC_ROOT_DATA


class COVID_VACCINE_STAT:
    def __init__(self) -> None:
        """KDCA COVID-19 Vaccine statistics"""
        # self.api_token >> [DATA.GO.KR](https://www.data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15077756)         
        self.api_token: str = COVID_VACCINE_STAT_API_KEY
    
    async def fetch_data(self, page: int = 1, per_page: int = 10):
        try:
            return await async_request.fetch(api_key=self.api_token, page=page, per_page=per_page)
        except TypeError:
            raise TypeError("Please set the COVID_VACCINE_STAT_API_KEY environment variable")
    
    async def south_korea_stat(self):
        resp = await self.fetch_data()
        source = resp.data[0]
        return source
    
    async def fetch_korea_stat(self):
        json_data = await self.south_korea_stat()
        source = {
            "region": json_data.sido,
            "data": {
                "base_date": json_data.baseDate,
                "first_cnt": json_data.firstCnt,
                "second_cnt": json_data.secondCnt,
                "total_first_cnt": json_data.totalFirstCnt,
                "total_second_cnt": json_data.totalSecondCnt,
                "accumulated_first_cnt": json_data.accumulatedFirstCnt,
                "accumulated_second_cnt": json_data.accumulatedSecondCnt
            }
        }
        return source