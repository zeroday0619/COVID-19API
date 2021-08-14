import asyncio

from typing import Optional, List, Union
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
    
    async def south_korea_stat(self, n: int, i: int = 1) -> Union[VACCINE_STAT_MODEL, List[VACCINE_STAT_MODEL]]:
        """
        기본모드 -> n = 0 
        >>> VACCINE_STAT_MODEL

        선택모드 -> n = 1
        >>> VACCINE_STAT_MODEL
            
        전국모드 -> n = 2
        >>> List[VACCINE_STAT_MODEL]
        """
        resp = await self.fetch_data()
        if n == 0:
            source = resp.data[0]
        elif n == 1:
            source = resp.data[i]
        elif n == 2:
            source = resp.data
        else:
            raise ValueError("Invalid argument")
        return source
    
    async def get_regions(self) -> List[str]:
        regions = await self.south_korea_stat(2)
        data = []
        _data = data.append
        for i in regions:
            _data(i.sido)
        return data
    
    async def fetch_select_region(self, region: str):
        json_data = await self.south_korea_stat(2)
        for i in json_data:
            if region in i.sido:
                data = {
                    "region": i.sido,
                    "data": {
                        "base_date": i.baseDate,
                        "first_cnt": i.firstCnt,
                        "second_cnt": i.secondCnt,
                        "total_first_cnt": i.totalFirstCnt,
                        "total_second_cnt": i.totalSecondCnt,
                        "accumulated_first_cnt": i.accumulatedFirstCnt,
                        "accumulated_second_cnt": i.accumulatedSecondCnt
                    }
                }
                return data
        return None

    async def fetch_regions_stat(self):
        json_data = await self.south_korea_stat(2)
        data = []
        _data = data.append
        for i in json_data:
            _data({
                "region": i.sido,
                "data": {
                    "base_date": i.baseDate,
                    "first_cnt": i.firstCnt,
                    "second_cnt": i.secondCnt,
                    "total_first_cnt": i.totalFirstCnt,
                    "total_second_cnt": i.totalSecondCnt,
                    "accumulated_first_cnt": i.accumulatedFirstCnt,
                    "accumulated_second_cnt": i.accumulatedSecondCnt
                }
            })
        data.pop(0)
        return data

    async def fetch_korea_stat(self):
        json_data = await self.south_korea_stat(0)
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