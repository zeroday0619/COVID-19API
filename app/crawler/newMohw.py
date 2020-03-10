import asyncio
import scrapy
import ujson

from scrapy.crawler import CrawlerRunner
from scrapy.selector import Selector
from ..ext.Performance import Performance
from .utils.kcdcAPI_V2 import KcdcApiV2
from .utils import cleanText

class Paser:
    """대한민국 질병관리본부 COVID-19 국내 현황 데이터 처리\n
    Version: 2020.03.10
    """
    def __init__(self):
        self.loop = Performance()
        self.KcdcApiV2 = KcdcApiV2()
        self.list = []

    async def Select(self):
        """scrapy Selector"""
        html = await self.KcdcApiV2.Request()
        data = await self.loop.run_in_threadpool(lambda: Selector(text=html))
        realtime = await self.loop.run_in_threadpool(lambda: data.xpath("/html/body/div/div[5]/div/div/div/div[1]/div[2]/div[1]/ul"))
        span = await self.loop.run_in_threadpool(lambda: realtime.css("li > span"))
        o = await self.loop.run_in_threadpool(lambda: span.getall())

        InspectionList = self.list
        for i in o:
            res = await cleanText(i)
            InspectionList.append(res)
        return InspectionList

    async def CumulativeInspection(self):
        il = await Paser().Select()
        jsondata = {
            "inspection":{
                "accumulate": il[1],
                "completions": il[3],
                "rate": il[5]
            },
            "description": il[6]
        }
        return jsondata


        
