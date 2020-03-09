import asyncio
import aiohttp
import ujson
import re

from scrapy.selector import Selector
from scrapy.crawler import CrawlerRunner
from ..ext.Performance import Performance
from .utils.news import CoronaNewsCrawler 
from .utils import NewsNogadaJsonData
from .utils import cleanText

class KrNewsParser:
    def __init__(self):
        self.loop = Performance()
        self.data = CoronaNewsCrawler()
    
    async def query(self):
        soup = await self.data.Request()
        a = await self.loop.run_in_threadpool(lambda: Selector(text=soup))
        description = await self.loop.run_in_threadpool(lambda: a.css("#main_pack > div.news.mynews.section._prs_nws > ul > li > dl"))
        __press = await self.loop.run_in_threadpool(lambda: description.css("dt > a"))
        __title = await self.loop.run_in_threadpool(lambda: description.css("dd > span._sp_each_source"))
        __summary = await self.loop.run_in_threadpool(lambda: description.css("dd:nth-child(3)"))
        __link = await self.loop.run_in_threadpool(lambda: description.css('dt > a'))
        _link = await self.loop.run_in_threadpool(lambda: __link.xpath("@href"))
        _press = await self.loop.run_in_threadpool(lambda: __press.getall())
        _title = await self.loop.run_in_threadpool(lambda: __title.getall())
        _summary = await self.loop.run_in_threadpool(lambda: __summary.getall())
        link = await self.loop.run_in_threadpool(lambda: _link.getall())
        press = []
        for i in _press:
            ___press = await cleanText(i)
            press.append(___press.replace("선정", ""))
        title = []
        for i in _title:
            ___title = await cleanText(i)
            title.append(___title)
        summary = []
        for i in _summary:
            ___summary = await cleanText(i)
            summary.append(___summary)       
        jsondata = await NewsNogadaJsonData(a=press, b=title, c=summary, d=link)
        return jsondata