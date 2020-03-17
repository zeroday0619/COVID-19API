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
from .utils import StringToInteger
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
    
    async def Convert(self):
        data = await self.data.GetInfectiousDiseases2()
        _data = await self.data.GetInfectiousDiseases4()
        soup = await self.loop.run_in_threadpool(lambda: Selector(text=data))
        _soup = await self.loop.run_in_threadpool(lambda: Selector(text=_data))

        aPatient = await self.loop.run_in_threadpool(lambda: soup.xpath("//*[@id='content']/div/div[3]/table/tbody/tr/td[4]")) # 확진 환자
        aQuarantine = await self.loop.run_in_threadpool(lambda: soup.xpath("//*[@id='content']/div/div[3]/table/tbody/tr/td[1]")) # 격리중
        aInIsolation = await self.loop.run_in_threadpool(lambda: soup.xpath("//*[@id='content']/div/div[3]/table/tbody/tr/td[2]")) # 격리 해제
        aDeath = await self.loop.run_in_threadpool(lambda: soup.xpath("//*[@id='content']/div/div[3]/table/tbody/tr/td[3]")) # 사망

        # The day before
        aBeforePatient = await self.loop.run_in_threadpool(lambda: _soup.css("body > div > div.mainlive_container > div > div > div > div.live_left > div.liveNum > ul > li:nth-child(1) > span.before")) # 확진 환자
        aBeforeQuarantine = await self.loop.run_in_threadpool(lambda: _soup.css("body > div > div.mainlive_container > div > div > div > div.live_left > div.liveNum > ul > li:nth-child(3) > span.before")) # 격리중
        aBeforeInIsolation = await self.loop.run_in_threadpool(lambda: _soup.css("body > div > div.mainlive_container > div > div > div > div.live_left > div.liveNum > ul > li:nth-child(2) > span.before")) # 격리 해제
        aBeforeDeath = await self.loop.run_in_threadpool(lambda: _soup.css("body > div > div.mainlive_container > div > div > div > div.live_left > div.liveNum > ul > li:nth-child(4) > span.before")) # 사망

        _Patient = await self.loop.run_in_threadpool(lambda: aPatient.getall()[0])
        _Quarantine = await self.loop.run_in_threadpool(lambda: aQuarantine.getall()[0])
        _InIsolation = await self.loop.run_in_threadpool(lambda: aInIsolation.getall()[0])
        _death = await self.loop.run_in_threadpool(lambda: aDeath.getall()[0])

        # The day before
        sBeforePatient = await self.loop.run_in_threadpool(lambda: aBeforePatient.getall()[0]) # 확진 환자
        sBeforeQuarantine = await self.loop.run_in_threadpool(lambda: aBeforeQuarantine.getall()[0]) # 격리 중
        sBeforeInIsolation = await self.loop.run_in_threadpool(lambda: aBeforeInIsolation.getall()[0]) #격리 해제
        sBeforeDeath = await self.loop.run_in_threadpool(lambda: aBeforeDeath.getall()[0]) # 사망

        Patient_ = await cleanText(_Patient)
        Quarantine_ = await cleanText(_Quarantine)
        InIsolation_ = await cleanText(_InIsolation)
        death_ = await cleanText(_death)

        # The day before
        dBeforePatient = await cleanText(sBeforePatient) # 확진 환자
        dBeforeQuarantine = await cleanText(sBeforeQuarantine) # 격리 중
        dBeforeInIsolation = await cleanText(sBeforeInIsolation) # 격리 해제
        dBeforeDeath = await cleanText(sBeforeDeath) # 사망


        Patient = await StringToInteger(string=Patient_)
        Quarantine = await StringToInteger(string=Quarantine_)
        InIsolation = await StringToInteger(string=InIsolation_)
        death = await StringToInteger(string=death_)
        # The day before
        BeforePatient = await StringToInteger(string=dBeforePatient) # 전일대비 확진 환자
        BeforeQuarantine = await StringToInteger(string=dBeforeQuarantine) # 전일대비 격리 중
        BefroeInIsolation = await StringToInteger(string=dBeforeInIsolation) # 전일대비 격리 해제
        BefroeDeath = await StringToInteger(string=dBeforeDeath) # 전일대비 사망

        result = {
            "patient": Patient,
            "before_patient": BeforePatient,
            "quarantine": Quarantine,
            "before_quarantine": BeforeQuarantine,
            "inisolation": InIsolation,
            "before_inisolation": BefroeInIsolation,
            "death": death,
            "before_death": BefroeDeath
        }
        return result
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
        InIsolation = await self.loop.run_in_threadpool(lambda: soup.xpath('//*[@id="content"]/div/div[3]/table/tbody/tr/td[1]')) # 격리중
        Quarantine = await self.loop.run_in_threadpool(lambda: soup.xpath('//*[@id="content"]/div/div[3]/table/tbody/tr/td[2]')) # 격리 해제
        Death = await self.loop.run_in_threadpool(lambda: soup.xpath("//*[@id='content']/div/div[3]/table/tbody/tr/td[3]")) # 사망
        SubTotal = await self.loop.run_in_threadpool(lambda: soup.xpath("//*[@id='content']/div/div[3]/table/tbody/tr/td[4]")) # 소계
        NegativeResult = await self.loop.run_in_threadpool(lambda: soup.xpath("//*[@id='content']/div/div[3]/table/tbody/tr/td[5]")) # 결과 음성
        InspectionCompleted = await self.loop.run_in_threadpool(lambda: soup.xpath("//*[@id='content']/div/div[3]/table/tbody/tr/td[6]")) # 검사 결과 소계

        """Inspection....."""
        UnderInspection = await self.loop.run_in_threadpool(lambda: soup.xpath("//*[@id='content']/div/div[3]/table/tbody/tr/td[7]")) # 검사 중......
        Total = await self.loop.run_in_threadpool(lambda: soup.xpath("//*[@id='content']/div/div[3]/table/tbody/tr/td[8]")) # 합계

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


