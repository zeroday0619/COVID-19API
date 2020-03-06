import asyncio
import aiohttp
import lxml
import ujson
import re
from bs4 import BeautifulSoup
from .utils import KcdcApi
from .utils.kcdcAPI import Performance
from .utils import cleanText
from .utils import JsonData
from ..ext import route

class Parser:
    def __init__(self, mode=11):
        self.data = KcdcApi(mode=mode)
        self.loop = Performance()

    async def CssSelect(self, data):
        soup = await self.data.GetInfectiousDiseases()
        td = await self.loop.run_in_threadpool(lambda: soup.select(data))
        cp = await cleanText(text=td[0])
        return cp

class Query:
    def __init__(self):
        self.Parser = Parser()
        self.ConfirmationPatientCSS = "#content > div > div.bv_content > div > div > table > tbody > tr:nth-of-type(1) > td"
        self.ConfirmationPatientIsolationCSS = "#content > div > div.bv_content > div > div > table > tbody > tr:nth-of-type(2) > td"
        self.DeadCSS = "#content > div > div.bv_content > div > div > table > tbody > tr:nth-of-type(3) > td"
        self.InspectionCSS = "#content > div > div.bv_content > div > div > table > tbody > tr:nth-of-type(4) > td"


    async def ConfirmationPatient(self):
        """확진환자"""
        cp = await self.Parser.CssSelect(data=self.ConfirmationPatientCSS)
        return cp

    async def ConfirmationPatientIsolation(self):
        """확진환자 격리해제"""
        cpi = await self.Parser.CssSelect(data=self.ConfirmationPatientIsolationCSS)
        return cpi

    async def Dead(self):
        """사망자"""
        d = await self.Parser.CssSelect(data=self.DeadCSS)
        return d

    async def Inspection(self):
        """검사진행"""
        i = await self.Parser.CssSelect(data=self.InspectionCSS)
        return i



class InfectiousDiseases:
    """Main Class
    - ConfirmationPatient
    - ConfirmationPatientIsolation
    - Dead
    - Inspection
    """
    def __init__(self):
        self.data = Query()
    
    async def Convert(self) -> dict:
        """
        :return: json
        """
        a = await self.data.ConfirmationPatient()
        b = await self.data.ConfirmationPatientIsolation()
        c = await self.data.Dead()
        d = await self.data.Inspection()
        JsonData = {
            "ConfirmationPatient": a,
            "ConfirmationPatientIsolation": b,
            "Dead": c,
            "Inspection": d
        }
        return JsonData

class GetInfectiousDiseasesbyRegion:
    def __init__(self, mode=13):
        self.data = KcdcApi(mode=mode)
        self.loop = Performance()

    async def Crawler(self) -> list:
        soup = await self.data.GetInfectiousDiseases()
        tbody = await self.loop.run_in_threadpool(lambda: soup.find('tbody'))
        td = await self.loop.run_in_threadpool(lambda: tbody.find_all('td'))
        return td

    async def SubCrawler(self):
        parser = GetInfectiousDiseasesbyRegion()
        data = await parser.Crawler()
        info = data
        stat = []
        for x in range(len(info)):
            inf = await cleanText(text=info[x])
            stat.append(inf)
        return stat

    async def AllRegion(self) -> list:
        #TODO: 귀차니즘의 결과물
        data = GetInfectiousDiseasesbyRegion()
        listdata = await data.SubCrawler()
        jsonData = await JsonData(listdata)
        return jsonData
    
    async def Classification(self, regionNumber: int):
        data = GetInfectiousDiseasesbyRegion()
        rt = await data.AllRegion()
        jsondata = await route(data=rt, regionNumber=regionNumber)
        return jsondata


