import re
import aiohttp
import asyncio
import lxml
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
import sys
sys.setrecursionlimit(10000)
class Performance:
    def __init__(self):
        self.running_threads = 0 
        self.max_threads = 6

    async def run_in_threadpool(self, function):
        global running_threads

        while self.running_threads >= self.max_threads:
            await asyncio.sleep(1)

        with ThreadPoolExecutor(max_workers=1) as thread_pool:
            running_threads = self.running_threads + 1

            loop = asyncio.get_event_loop()
            result = loop.run_in_executor(thread_pool, function)
            try:
                result = await result
            except Exception as e:
                raise e
            finally:
                running_threads = running_threads - 1
                thread_pool.shutdown(wait=True)
            return result



class kcdcAPI:
    def __init__(self, mode):
        """Initialize
        mode: 
            11 -> 발생동향
            12 -> 확진환자 이동경로
            13 -> 시도별 발생동향
        """
        self.loop = Performance()
        # 질병관리본부 COVID-19 URL
        self.url = "http://ncov.mohw.go.kr/bdBoardList_Real.do"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 10.0.0; SM-F700NZPAKOO) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.101 Mobile Safari/537.36"
        }
        self.payload = {
            "brdGubun": mode 
        }

    async def GetInfectiousDiseases(self):
        """국내 감염증 정보 파싱"""
        async with aiohttp.ClientSession(headers=self.headers) as session:
            async with session.get(url=self.url, params=self.payload) as resp:
                info = await resp.text()
        soup = await self.loop.run_in_threadpool(lambda: BeautifulSoup(info, 'lxml'))
        return soup