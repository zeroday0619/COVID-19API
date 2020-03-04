import asyncio
import aiohttp
import lxml
import re
import ujson
from bs4 import BeautifulSoup
from .utils import cleanText
from .utils import NaverApi


class InfectiousDiseasesbyRegion:
    def __init__(self):
        self.data = NaverApi()
        self.templit: dict[str, Union[Optional[str], Any]] = {
            "regions": None,
            "info": {
                "ConfirmationPatient": None,
                "ratio": None
            },
        }

    async def Result(self):
        jsonData = await self.data.GetInfectiousDiseasesbyRegion()
        length = len(jsonData)
        for item in jsonData:
            templit = self.templit
            templit['regions'] = item['title']
            templit['info']['ConfirmationPatient'] = item['count']
            templit['info']['ratio'] = item['rate']
            yield templit
    
    async def IDR(self):
        resp = []
        data = InfectiousDiseasesbyRegion()
        async for i in data.Result():
            db = ujson.loads(ujson.encode(i))
            resp.append(db)
        return resp