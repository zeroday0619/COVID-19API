from typing import List

from scrapy.selector import Selector
from app.crawler.utils.ext import KcdcApi, cleanText, StringToInteger, JsonData
from app.ext.utils.Performance import Performance
from app.ext.utils.route import route


class InfectiousDiseases:
    """Main Class
    - ConfirmationPatient
    - ConfirmationPatientIsolation
    - Dead
    - Inspection
    """
    def __init__(self, mode=11):
        self.loop = Performance()
        self.data = KcdcApi(mode=mode)

    async def Convert(self):
        data = await self.data.GetInfectiousDiseases2()
        _data = await self.data.GetInfectiousDiseases4()
        soup = await self.loop.run_in_threadpool(lambda: Selector(text=data))
        _soup = await self.loop.run_in_threadpool(lambda: Selector(text=_data))

        aPatient = await self.loop.run_in_threadpool(lambda: soup.xpath("//*[@id='content']/div/div[2]/table/tbody/tr/td[1]")) # 확진 환자

        aQuarantine = await self.loop.run_in_threadpool(lambda: soup.xpath("//*[@id='content']/div/div[2]/table/tbody/tr/td[3]")) # 격리중

        aInIsolation = await self.loop.run_in_threadpool(lambda: soup.xpath("//*[@id='content']/div/div[2]/table/tbody/tr/td[2]")) # 격리 해제

        aDeath = await self.loop.run_in_threadpool(lambda: soup.xpath("//*[@id='content']/div/div[2]/table/tbody/tr/td[4]")) # 사망

        # The day before
        aBeforePatient = await self.loop.run_in_threadpool(lambda: _soup.css("body > div > div.mainlive_container > div.container > div > div.liveboard_layout > div.liveNumOuter > div > ul > li:nth-child(1) > span.before")) # 확진 환자
        aBeforeQuarantine = await self.loop.run_in_threadpool(lambda: _soup.css("body > div > div.mainlive_container > div.container > div > div.liveboard_layout > div.liveNumOuter > div > ul > li:nth-child(3) > span.before")) # 격리중
        aBeforeInIsolation = await self.loop.run_in_threadpool(lambda: _soup.css("body > div > div.mainlive_container > div.container > div > div.liveboard_layout > div.liveNumOuter > div > ul > li:nth-child(2) > span.before")) # 격리 해제
        aBeforeDeath = await self.loop.run_in_threadpool(lambda: _soup.css("body > div > div.mainlive_container > div.container > div > div.liveboard_layout > div.liveNumOuter > div > ul > li:nth-child(4) > span.before")) # 사망

        aTodayCases = await self.loop.run_in_threadpool(lambda: _soup.xpath('/html/body/div/div[5]/div[2]/div/div[1]/div[1]/ul/li[1]/span[2]'))
        aTodayRecovered = await self.loop.run_in_threadpool(lambda: _soup.xpath('/html/body/div/div[5]/div[2]/div/div[1]/div[1]/ul/li[2]/span[2]'))

        _Patient = await self.loop.run_in_threadpool(lambda: aPatient.getall()[0])
        _Quarantine = await self.loop.run_in_threadpool(lambda: aQuarantine.getall()[0])
        _InIsolation = await self.loop.run_in_threadpool(lambda: aInIsolation.getall()[0])
        _death = await self.loop.run_in_threadpool(lambda: aDeath.getall()[0])

        # The day before
        sBeforePatient = await self.loop.run_in_threadpool(lambda: aBeforePatient.getall()[0]) # 확진 환자
        sBeforeQuarantine = await self.loop.run_in_threadpool(lambda: aBeforeQuarantine.getall()[0]) # 격리 중
        sBeforeInIsolation = await self.loop.run_in_threadpool(lambda: aBeforeInIsolation.getall()[0]) #격리 해제
        sBeforeDeath = await self.loop.run_in_threadpool(lambda: aBeforeDeath.getall()[0]) # 사망

        __TodayCases = await self.loop.run_in_threadpool(lambda: aTodayCases.getall()[0])
        __TodayRecovered = await self.loop.run_in_threadpool(lambda: aTodayRecovered.getall()[0])


        Patient_ = await cleanText(_Patient)
        Quarantine_ = await cleanText(_Quarantine)
        InIsolation_ = await cleanText(_InIsolation)
        death_ = await cleanText(_death)

        # The day before
        dBeforePatient = await cleanText(sBeforePatient) # 확진 환자
        dBeforeQuarantine = await cleanText(sBeforeQuarantine) # 격리 중
        dBeforeInIsolation = await cleanText(sBeforeInIsolation) # 격리 해제
        dBeforeDeath = await cleanText(sBeforeDeath) # 사망

        _TodayCases = await cleanText(__TodayCases)
        _TodayRecovered = await cleanText(__TodayRecovered)

        Patient = await StringToInteger(string=Patient_)
        Quarantine = await StringToInteger(string=Quarantine_)
        InIsolation = await StringToInteger(string=InIsolation_)
        death = await StringToInteger(string=death_)
        # The day before
        BeforePatient = await StringToInteger(string=dBeforePatient) # 전일대비 확진 환자
        BeforeQuarantine = await StringToInteger(string=dBeforeQuarantine) # 전일대비 격리 중
        BefroeInIsolation = await StringToInteger(string=dBeforeInIsolation) # 전일대비 격리 해제
        BefroeDeath = await StringToInteger(string=dBeforeDeath) # 전일대비 사망

        TodayCases = await StringToInteger(_TodayCases)
        TodayRecovered = await StringToInteger(_TodayRecovered)

        result = {
            "todayCases": TodayCases,
            "todayRecovered": TodayRecovered,
            "cases": Patient,
            "beforeCases": BeforePatient,
            "quarantine": Quarantine,
            "beforeQuarantine": BeforeQuarantine,
            "recovered": InIsolation,
            "beforeRecovered": BefroeInIsolation,
            "death": death,
            "beforeDeath": BefroeDeath
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
            "cases": {
                "recovered": int(a.replace(",", '')),
                "quarantine": int(b.replace(",", '')),
                "death": int(c.replace(",", '')),
                "subTotal": int(d.replace(",", '')),
            },
            "negativeResult": int(e.replace(",", '')),
            "inspectionCompleted": int(f.replace(",", '')),
            "underInspection": int(g.replace(",", '')),
            "total": int(h.replace(",", ''))
        }
        return jsondata


class GetInfectiousDiseasesbyRegion:
    def __init__(self, mode=13):
        self.data = KcdcApi(mode=mode)
        self.loop = Performance()

    async def Crawler(self) -> list:
        soup = await self.data.GetInfectiousDiseases2()
        tbody = await self.loop.run_in_threadpool(lambda: Selector(text=soup))
        _tbody = await self.loop.run_in_threadpool(lambda: tbody.xpath('//*[@id="content"]/div/div[5]/table/tbody'))
        _td = await self.loop.run_in_threadpool(lambda: _tbody.css('tr > td'))
        td = await self.loop.run_in_threadpool(lambda:_td.getall())
        return td

    async def SubCrawler(self):
        parser = GetInfectiousDiseasesbyRegion()
        data = await parser.Crawler()
        info = data
        stat = [float(await cleanText(items.strip())) for items in info]
        return stat

    @staticmethod
    async def AllRegion() -> list:
        """
        X = 8, Y = 19

        152 / 8 = 19
        list 안 데이터 를 8개씩 자르고
        이 과정을 19번 처리
        """
        data = GetInfectiousDiseasesbyRegion()
        data = await data.SubCrawler()
        covertData = []; count = 0; div = 8
        length = len(data)

        r = None
        append2 = covertData.append
        for source in range(count, length + div, div):
            res = data[count:count + div]
            if res != []:
                r: List[float] = res
            count = count + div
            append2(r)
        result = covertData[1:]
        jsonTemplate = {
            "status": True,
            "data": {
                "seoul": {

                }
            }
        }
        return jsonTemplate




    async def Classification(self, regionNumber: int):
        data = GetInfectiousDiseasesbyRegion()
        rt = await data.AllRegion()
        jsondata = await route(data=rt, regionNumber=regionNumber)
        return jsondata


