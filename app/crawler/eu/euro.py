from app.crawler.utils.eu.ecdcApi import Ecdc
from app.crawler.utils.ext import EuroJsonData
from app.ext.utils.Performance import Performance


class Euro:
    """유럽 연합 질병관리본부 ECDC COVID-19 현황 Parser"""
    def __init__(self):
        self.loop = Performance()
        self.source = Ecdc()

    async def EuroCovid(self):
        listdata = await self.source.ConvertList()
        result = await EuroJsonData(listdata)
        return result