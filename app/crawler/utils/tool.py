import re
import aiohttp
import asyncio
import lxml
from bs4 import BeautifulSoup

def cleanText(text):
    cleanT = re.sub('<.+?>', '', str(text))
    return cleanT

class Requests:
    def __init__(self):
        # 질병관리본부 COVID-19 URL
        self.mohurl = "http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=&brdGubun=&ncvContSeq=&contSeq=&board_id=&gubun="
        
        # NAVER COVID-19 URL
        self.headers = {
            "Host": "m.search.naver.com",
            "User-Agent": "Mozilla/5.0 (Linux; Android 10.0.0; SM-F700NZPAKOO) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.101 Mobile Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
            "Connection": "keep-alive",
            "Referer": "https://m.search.naver.com/search.naver?sm=mtp_hty.top&where=m&query=%EC%BD%94%EB%A1%9C%EB%82%98",
            "TE": "Trailers"
        }
        self.naverurl = "https://m.search.naver.com/p/csearch/content/nqapirender.nhn"
        self.payload = {
            "where": "m",
            "pkid": "9005",
            "key": "regionAPI",
            "sort": "sort_1",
            "direction": "desc",
            "u1": "13867393"
        }

    async def GetInfectiousDiseases(self):
        """국내 감염증 현황"""
        loop = asyncio.get_event_loop()
        async with aiohttp.ClientSession() as session:
            async with session.get(url=self.mohurl) as resp:
                info = await resp.text()
        soup = await loop.run_in_executor(None, BeautifulSoup, info, 'lxml')
        return soup

    async def GetInfectiousDiseasesbyRegion(self):
        """지역별 감염증 현황"""
        loop = asyncio.get_event_loop()
        async with aiohttp.ClientSession(headers=self.headers) as session:
            async with session.get(url=self.naverurl, params=self.payload) as resp:
                info = await resp.json()
        return info['result']['regions']