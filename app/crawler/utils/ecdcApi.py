from app.ext.utils.Performance import Performance
from . import cleanText
from scrapy.selector import Selector
import aiohttp


class Ecdc:
    def __init__(self):
        self.loop = Performance()
        self.url = "https://www.ecdc.europa.eu/en/cases-2019-ncov-eueea"
        self.headers = {"user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:74.0) Gecko/20100101 Firefox/74.0"}
        self.xpath = '/html/body/div/div/div[1]/main/section[2]/div/div/div/div[2]/div/section/div/div[3]/div[2]/div/table/tbody/tr/td'

    async def Request(self):
        async with aiohttp.ClientSession(headers=self.headers) as session:
            async with session.get(url=self.url) as resp:
                HTML = await resp.text()
        return HTML

    async def Crawler(self):
        source = await self.Request()
        soup = await self.loop.run_in_threadpool(lambda: Selector(text=source))
        layer = await self.loop.run_in_threadpool(lambda: soup.xpath(self.xpath))
        result = await self.loop.run_in_threadpool(lambda: layer.getall())
        return result

    async def ConvertList(self):
        source = await self.Crawler()
        ListA = []
        for item in source:
            ListA.append(cleanText(item))
        return ListA
