"""
코드 참조
https://github.com/KKodiac/Covid19_Stats/blob/master/Covid-19/covid19_wd.py
"""
import aiohttp
import ujson
from async_lru import alru_cache
from app.ext.utils.Performance import Performance


class CSSEParser:
    def __init__(self):
        self.loop = Performance()
        self.serviceLinks = "https://services1.arcgis.com/0MSEUqKaxRlEPj5g/arcgis/rest/services/ncov_cases/FeatureServer/2/query"
        self.query_syn = {
            "f": "json",
            "where": "Confirmed>0",
            "outFields": "*",
            "orderByFields": "OBJECTID"
        }
        self.headers = {
            "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:74.0) Gecko/20100101 Firefox/74.0"
        }

    @alru_cache(maxsize=32)
    async def Processing(self):

        async with aiohttp.ClientSession() as session:
            async with session.get(url=self.serviceLinks, params=self.query_syn) as resp:
                j_text = await resp.text()
        return j_text
    
    async def _return_wd_dat(self):
        data = await self.Processing()
        dumped = await self.loop.run_in_threadpool(lambda: ujson.loads(data))
        da = dumped["features"]
        for row in da:
            result = {
                "country": row['attributes']['Country_Region'],
                "state": {
                    "cases": row['attributes']['Confirmed'],
                    "recovered": row['attributes']['Recovered'],
                    "death": row['attributes']['Deaths']
                }
            }
            yield result
    
    async def return_wd_dat(self):
        sa = []
        async for i in self._return_wd_dat():
            sa.append(i)
        return sa