import asyncio
import aiohttp
import ujson
import lxml
import re

from bs4 import BeautifulSoup
from scrapy.selector import Selector
from .utils import KcdcApi
from ..ext.Performance import Performance
from .utils import cleanText
from .utils import JsonData
from ..ext import route


class InfectiousDiseases:
    """Main Class
    - ConfirmationPatient
    - ConfirmationPatientIsolation
    - Dead
    - Inspection
    """
    def __init__(self, mode=11):
        self.data = KcdcApi(mode=mode)
        self.loop = Performance()
    
    async def Convert(self) -> dict:
        """
        :return: json
        """
        data = await self.data.GetInfectiousDiseases2()
        soup = await self.loop.run_in_threadpool(lambda: Selector(text=data))

        patient = await self.loop.run_in_threadpool(lambda: soup.xpath("/html/body/div/div[5]/div/div/div/div[1]/div[1]/ul/li[1]/span[1]"))
        patientrate = await self.loop.run_in_threadpool(lambda: soup.xpath("/html/body/div/div[5]/div/div/div/div[1]/div[1]/ul/li[1]/span[2]"))
        
        isolation = await self.loop.run_in_threadpool(lambda: soup.xpath("/html/body/div/div[5]/div/div/div/div[1]/div[1]/ul/li[2]/span[1]"))
        isolationrate = await self.loop.run_in_threadpool(lambda: soup.xpath("/html/body/div/div[5]/div/div/div/div[1]/div[1]/ul/li[2]/span[2]"))

        inisolation = await self.loop.run_in_threadpool(lambda: soup.xpath("/html/body/div/div[5]/div/div/div/div[1]/div[1]/ul/li[3]/span[1]"))
        inisolationrate = await self.loop.run_in_threadpool(lambda: soup.xpath("/html/body/div/div[5]/div/div/div/div[1]/div[1]/ul/li[3]/span[2]"))

        death = await self.loop.run_in_threadpool(lambda: soup.xpath("/html/body/div/div[5]/div/div/div/div[1]/div[1]/ul/li[4]/span[1]"))
        deathrate = await self.loop.run_in_threadpool(lambda: soup.xpath("/html/body/div/div[5]/div/div/div/div[1]/div[1]/ul/li[4]/span[2]"))

        _patient = await self.loop.run_in_threadpool(lambda: patient.getall())
        _patientrate = await self.loop.run_in_threadpool(lambda: patientrate.getall())

        _isolation = await self.loop.run_in_threadpool(lambda: isolation.getall())
        _isolationrate = await self.loop.run_in_threadpool(lambda: isolationrate.getall())

        _inisolation = await self.loop.run_in_threadpool(lambda: inisolation.getall())
        _inisolationrate = await self.loop.run_in_threadpool(lambda: inisolationrate.getall())

        _death = await self.loop.run_in_threadpool(lambda: death.getall())
        _deathrate = await self.loop.run_in_threadpool(lambda: deathrate.getall())        

        a = await cleanText(_patient[0])
        b = await cleanText(_patientrate[0])

        c = await cleanText(_isolation[0])
        d = await cleanText(_isolationrate[0])
        
        _a = await cleanText(_inisolation[0])
        _b = await cleanText(_inisolationrate[0])
        
        _c = await cleanText(_death[0])
        _d = await cleanText(_deathrate[0])

        JsonData = [
            {
                "patient": int(a.replace("(누적)", "").strip().replace(",", '')),
                "compared": int(b.replace("전일대비", "").replace("(", "").replace(")", "").replace(" ","").strip().replace(",", ''))
            },
            {
                "isolation": int(c.replace(",", '')),
                "compared": int(d.replace("전일대비", "").replace("(", "").replace(")", "").replace(" ","").strip().replace(",", ''))
            },
            {
                "in_isolation": int(_a.replace(",", '')),
                "compared": int(_b.replace("전일대비", "").replace("(", "").replace(")", "").replace(" ","").strip().replace(",", ''))
            },
            {
                "death": int(_c.replace(",", '')),
                "compared": int(_d.replace("전일대비", "").replace("(", "").replace(")", "").replace(" ","").strip().replace(",", ''))
            }
        ]
        return JsonData
    async def InspectionStatusDetail(self):
        """대한민국 COVID-19 검사 - Detail
        - InIsolation: 격리중
        - Quarantine: 격리 해제
        - Death: 사망
        - SubTotal: 소계
        - NegativeResult: 결과 음성
        - InspectionCompleted: 검사 결과 소계
        - UnderInspection: 검사 중...
        - Total: 합계

        """
        data = await self.data.GetInfectiousDiseases3()
        soup = await self.loop.run_in_threadpool(lambda: Selector(text=data))
        
        """Inspection completed"""
        InIsolation = await self.loop.run_in_threadpool(lambda: soup.xpath("//*[@id='content']/div/div[4]/table/tbody/tr/td[1]")) # 격리중
        Quarantine = await self.loop.run_in_threadpool(lambda: soup.xpath("//*[@id='content']/div/div[4]/table/tbody/tr/td[2]")) # 격리 해제
        Death = await self.loop.run_in_threadpool(lambda: soup.xpath("//*[@id='content']/div/div[4]/table/tbody/tr/td[3]")) # 사망
        SubTotal = await self.loop.run_in_threadpool(lambda: soup.xpath("//*[@id='content']/div/div[4]/table/tbody/tr/td[4]")) # 소계
        NegativeResult = await self.loop.run_in_threadpool(lambda: soup.xpath("//*[@id='content']/div/div[4]/table/tbody/tr/td[5]")) # 결과 음성
        InspectionCompleted = await self.loop.run_in_threadpool(lambda: soup.xpath("//*[@id='content']/div/div[4]/table/tbody/tr/td[6]")) # 검사 결과 소계

        """Inspection....."""
        UnderInspection = await self.loop.run_in_threadpool(lambda: soup.xpath("//*[@id='content']/div/div[4]/table/tbody/tr/td[7]")) # 검사 중......
        Total = await self.loop.run_in_threadpool(lambda: soup.xpath("//*[@id='content']/div/div[4]/table/tbody/tr/td[8]")) # 합계

        a = await cleanText(await self.loop.run_in_threadpool(lambda: InIsolation.getall()[0]))
        b = await cleanText(await self.loop.run_in_threadpool(lambda: Quarantine.getall()[0]))
        c = await cleanText(await self.loop.run_in_threadpool(lambda: Death.getall()[0]))
        d = await cleanText(await self.loop.run_in_threadpool(lambda: SubTotal.getall()[0]))
        e = await cleanText(await self.loop.run_in_threadpool(lambda: NegativeResult.getall()[0]))
        f = await cleanText(await self.loop.run_in_threadpool(lambda: InspectionCompleted.getall()[0]))
        g = await cleanText(await self.loop.run_in_threadpool(lambda: UnderInspection.getall()[0]))
        h = await cleanText(await self.loop.run_in_threadpool(lambda: Total.getall()[0]))
        jsondata = {
            "ConfirmationPatient":{
                "InIsolation": int(a.replace(",", '')),
                "Quarantine": int(b.replace(",", '')),
                "Death": int(c.replace(",", '')),
                "SubTotal": int(d.replace(",", '')),
            },
            "NegativeResult": int(e.replace(",", '')),
            "InspectionCompleted": int(f.replace(",", '')),
            "UnderInspection": int(g.replace(",", '')),
            "Total": int(h.replace(",", ''))
        }
        return jsondata

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


