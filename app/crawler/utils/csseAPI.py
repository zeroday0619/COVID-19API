"""
코드 참조
https://github.com/KKodiac/Covid19_Stats/blob/master/Covid-19/covid19_wd.py
"""
import asyncio
import aiohttp
import ujson
from ...ext.Performance import Performance

class CSSEParser:
    def __init__(self):
        self.headers = {
            "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:74.0) Gecko/20100101 Firefox/74.0"
        }
        self.loop = Performance()

    async def Processing(self):
        serviceLinks = "https://services1.arcgis.com/0MSEUqKaxRlEPj5g/arcgis/rest/services/ncov_cases/FeatureServer/2/query"
        query_syn = {
            "f": "json",
            "where": "Confirmed>0",
            "outFields": "*",
            "orderByFields": "OBJECTID"
        }
        async with aiohttp.ClientSession() as session:
            async with session.get(url=serviceLinks, params=query_syn) as resp:
                jtext = await resp.text()
        return jtext
    
    async def _return_wd_dat(self):
        data = await self.Processing()
        dumped = ujson.loads(data)
        da = dumped["features"]
        sa = []
        for row in da:
            result = {
                "country": row['attributes']['Country_Region'],
                "state":{
                    "patient": row['attributes']['Confirmed'],
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


        