import asyncio
import aiohttp
from pyppeteer import launch
from ...ext.Performance import Performance
class CSSEParser:
    def __init__(self):
        self.loop = Performance()
        self.globalMapUrl = "https://www.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36 Edg/80.0.361.66"
        }
        self.Config = {'headless': True}
    async def HeadlessCrawler(self):
        browser = await launch(options=self.Config)
        page = await browser.newPage()
        await page.goto(url=self.globalMapUrl)
        