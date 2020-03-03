import asyncio
import aiohttp
import lxml
import re
from bs4 import BeautifulSoup
from .utils import cleanText

class Requests:
    def __init__(self):
        self.url = "http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=&brdGubun=&ncvContSeq=&contSeq=&board_id=&gubun="

    async def GetInfectiousDiseases(self):
        loop = asyncio.get_event_loop()
        async with aiohttp.ClientSession() as session:
            async with session.get(url=self.url) as resp:
                info = await resp.text()
        soup = await loop.run_in_executor(None, BeautifulSoup, info, 'lxml')
        return soup


async def Result():
    data = Requests()
    soup = await data.GetInfectiousDiseases()
    return soup

async def CssSelect(data):
    soup = await Result()
    td = soup.select(data)
    cp = cleanText(text=td[0])
    return cp

class Query:
    def __init__(self):
        self.ConfirmationPatientCSS = "#content > div > div.bv_content > div > div:nth-child(3) > table > tbody > tr:nth-child(1) > td"
        self.ConfirmationPatientIsolationCSS = "#content > div > div.bv_content > div > div:nth-child(3) > table > tbody > tr:nth-child(2) > td"
        self.DeadCSS = "#content > div > div.bv_content > div > div:nth-child(3) > table > tbody > tr:nth-child(3) > td"
        self.InspectionCSS = "#content > div > div.bv_content > div > div:nth-child(3) > table > tbody > tr:nth-child(4) > td"


    async def ConfirmationPatient(self):
        """확진환자"""
        cp = await CssSelect(data=self.ConfirmationPatientCSS)
        return cp

    async def ConfirmationPatientIsolation(self):
        """확진환자 격리해제"""
        cpi = await CssSelect(data=self.ConfirmationPatientIsolationCSS)
        return cpi

    async def Dead(self):
        """사망자"""
        d = await CssSelect(data=self.DeadCSS)
        return d

    async def Inspection(self):
        """검사진행"""
        i = await CssSelect(data=self.InspectionCSS)
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