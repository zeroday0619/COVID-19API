# //*[@id="yDmH0d"]/c-wiz/div/div[2]/div/div[2]/div[4]/div[1]/div[1]/div/div[2]/div/div[1]/table/tbody
from scrapy import Selector
import aiohttp
import asyncio
import ujson


class WorldCoronaStatus:
    def __init__(self):
        self.url = "https://google.com/covid19-map/?hl=ko"

    async def Request(self):
        """Request"""
        async with aiohttp.ClientSession() as session:
            async with session.get(url=self.url) as resp:
                html = await resp.read()
        return html

    async def Processing(self):
        source = await self.Request()
        soup = Selector(text=source)
        tbody = soup.xpath('//*[@id="yDmH0d"]/c-wiz/div/div[2]/div/div[2]/div[4]/div[1]/div[1]/div/div[2]/div/div[1]/table/tbody')
        data = tbody.css("tr > td > span").getall()
        for index in data:
            print(index)


o = WorldCoronaStatus()

asyncio.run(o.Processing())
