import re
import aiohttp
import asyncio
import lxml
from bs4 import BeautifulSoup


class NaverAPI:
    """TODO: 네이버 내부 API로 데이터 받아오지만 추후 질병관리본부 크롤링을 통한 수집이 필요함 > Request Block 가능성 높음"""
    def __init__(self):
        # NAVER COVID-19 URL
        self.naverurl = "https://m.search.naver.com/p/csearch/content/nqapirender.nhn"
        self.headers = {
            "Host": "m.search.naver.com",
            "User-Agent": "Mozilla/5.0 (Linux; Android 10.0.0; SM-F700NZPAKOO) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.101 Mobile Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
            "Connection": "keep-alive",
            "Referer": "https://m.search.naver.com/search.naver?sm=mtp_hty.top&where=m&query=%EC%BD%94%EB%A1%9C%EB%82%98",
            "TE": "Trailers"
        }
        self.payload = {
            "where": "m",
            "pkid": "9005",
            "key": "regionAPI",
            "sort": "sort_1",
            "direction": "desc",
            "u1": "13867393"
        }
    async def GetInfectiousDiseasesbyRegion(self):
        """지역별 감염증 현황"""
        loop = asyncio.get_event_loop()
        async with aiohttp.ClientSession(headers=self.headers) as session:
            async with session.get(url=self.naverurl, params=self.payload) as resp:
                info = await resp.json()
        return info['result']['regions']