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


class Parser2:
    def __init__(self, mode=13):
        self.data = KcdcApi(mode=mode)

    async def Crawler(self) -> list:
        parser = Parser2()
        soup = await parser.Request()
        tbody = soup.find('tbody')
        tr = tbody.find_all('td')
        th = tbody.find_all('th')
        return [tr, th]

    async def SubCrawler(self):
        go = Parser2()
        data = await go.Crawler()
        info = data[0]
        stat = []
        for x in range(len(info)):
            inf = re.sub('<.+?>', '', str(info[x]), 0, re.I|re.S).strip()
            stat.append(inf)
        listdata = stat
        #TODO: 귀차니즘의 결과물
        jsonData = {
            'Region':[{
                'SEOUL':{
                    'increase': listdata[5],
                    'patient': listdata[6],
                    'death': listdata[7],
                    'ratio': listdata[8],
                    'inspection': listdata[9]
                },
                'BUSAN': {
                    'increase': listdata[10],
                    'patient': listdata[11],
                    'death': listdata[12],
                    'ratio': listdata[13],
                    'inspection': listdata[14]
                },
                'DAEGU': {
                    'increase': listdata[15],
                    'patient': listdata[16],
                    'death': listdata[17],
                    'ratio': listdata[18],
                    'inspection': listdata[19]
                },
                'INCHEON': {
                    'increase': listdata[20],
                    'patient': listdata[21],
                    'death': listdata[22],
                    'ratio': listdata[23],
                    'inspection': listdata[24]
                },
                'GWANGJU': {
                    'increase': listdata[25],
                    'patient': listdata[26],
                    'death': listdata[27],
                    'ratio': listdata[28],
                    'inspection': listdata[29]
                },
                'DAEJEON': {
                    'increase': listdata[30],
                    'patient': listdata[31],
                    'death': listdata[32],
                    'ratio': listdata[33],
                    'inspection': listdata[34]
                },
                'ULSAN': {
                    'increase': listdata[35],
                    'patient': listdata[36],
                    'death': listdata[37],
                    'ratio': listdata[38],
                    'inspection': listdata[39]
                },
                'SEJONG': {
                    'increase': listdata[40],
                    'patient': listdata[41],
                    'death': listdata[42],
                    'ratio': listdata[43],
                    'inspection': listdata[44]
                },
                'GYEONGGI': {
                    'increase': listdata[45],
                    'patient': listdata[46],
                    'death': listdata[47],
                    'ratio': listdata[48],
                    'inspection': listdata[49]
                },
                'GANGWON': {
                    'increase': listdata[50],
                    'patient': listdata[51],
                    'death': listdata[52],
                    'ratio': listdata[53],
                    'inspection': listdata[54]
                },
                'CHUNGBUK': {
                    'increase': listdata[55],
                    'patient': listdata[56],
                    'death': listdata[57],
                    'ratio': listdata[58],
                    'inspection': listdata[59]
                },
                'CHUNGNAM': {
                    'increase': listdata[60],
                    'patient': listdata[61],
                    'death': listdata[62],
                    'ratio': listdata[63],
                    'inspection': listdata[64]
                },
                'JEONBUK': {
                    'increase': listdata[65],
                    'patient': listdata[66],
                    'death': listdata[67],
                    'ratio': listdata[68],
                    'inspection': listdata[69]
                },
                'JEONNAM': {
                    'increase': listdata[70],
                    'patient': listdata[71],
                    'death': listdata[72],
                    'ratio': listdata[73],
                    'inspection': listdata[74]
                },
                'GYEONGBUK': {
                    'increase': listdata[75],
                    'patient': listdata[76],
                    'death': listdata[77],
                    'ratio': listdata[78],
                    'inspection': listdata[79]
                },
                'GYEONGNAM': {
                    'increase': listdata[80],
                    'patient': listdata[81],
                    'death': listdata[82],
                    'ratio': listdata[83],
                    'inspection': listdata[84]
                },
                'JEJU': {
                    'increase': listdata[85],
                    'patient': listdata[86],
                    'death': listdata[87],
                    'ratio': listdata[88],
                    'inspection': listdata[89]
                },
            },]
        }
        return jsonData