import asyncio
import aiohttp
import lxml
import re
from bs4 import BeautifulSoup
from .utils import KcdcApi
from .utils import cleanText

class Parser:
    def __init__(self, mode=11):
        self.data = KcdcApi(mode=mode)

    async def CssSelect(self, data):
        soup = await self.data.GetInfectiousDiseases()
        td = soup.select(data)
        cp = cleanText(text=td[0])
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

class ConfirmationPatientMovementRoute:
    def __init__(self):
        pass
