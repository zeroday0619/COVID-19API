from scrapy.selector import Selector
from app.ext.utils.Performance import Performance
from .utils import cleanText
from .utils.msnCovid import MsnCovid


class CoronaVirusDiseaseStatus:
    def __init__(self):
        self.loop = Performance()
        self.source = MsnCovid()

    async def GlobalCoronaVirusDisease(self):
        """
        {
            "totalConfirmed": source['totalConfirmed'],
            "totalDeaths": source['totalDeaths'],
            "totalRecovered": source['totalRecovered'],
            "lastUpdated": source['lastUpdated']
        }
        """
        source = await self.source.MsnRequest()
        data = {
            "totalConfirmed": source['totalConfirmed'],
            "totalDeaths": source['totalDeaths'],
            "totalRecovered": source['totalRecovered'],
            "lastUpdated": source['lastUpdated']
        }
        return data

    async def SearchGlobalCoronaVirusDisease(self):
        source = await self.source.MsnRequest()
        areas = source['areas']
        return areas