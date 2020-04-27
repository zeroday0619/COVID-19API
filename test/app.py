# //*[@id="yDmH0d"]/c-wiz/div/div[2]/div/div[2]/div[4]/div[1]/div[1]/div/div[2]/div/div[1]/table/tbody
from scrapy import Selector
import aiohttp
import asyncio
import re
import ujson
from concurrent.futures import ThreadPoolExecutor
import asyncio


class Performance:
    """Performance Module
    - run_in_threadpool
    """
    def __init__(self, max_threads: int = 4):
        """
        ```
        Performance(max_threads: int)
        max_threads:
            Default 4
        ```
        """
        self.running_threads = 0 # Fixed value
        self.max_threads = max_threads

    async def run_in_threadpool(self, function):
        """run_in_threadpool Usage:
        ```
        ...
        async def main():
            data = await run_in_threadpool(lambda: function())
            return data
        ```
        """
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


async def cleanText(text):
    loop = Performance()
    # cleanT = await loop.run_in_executor(None, re.sub, "<.+?>", "", str(text), 0, re.I|re.S)
    cleanT = await loop.run_in_threadpool(lambda: re.sub("<.+?>", "", str(text), 0, re.I|re.S))
    return cleanT


class KrStatusRegion:
    def __init__(self):
        self.loop = asyncio.get_event_loop()
        self.url = "http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=13&ncvContSeq=&contSeq=&board_id=&gubun="

    async def Request(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(url=self.url) as resp:
                html = await resp.read()
        return html

    async def Processing(self):
        source = await self.Request()
        soup = Selector(text=source)
        tbody = soup.xpath(query='//*[@id="content"]/div/div[5]/table/tbody/tr/td').getall()
        data = []
        for i in tbody:
            content = await cleanText(i)
            data.append(content)
        print(ujson.dumps(data, indent=4, ensure_ascii=False))


app = KrStatusRegion()
asyncio.run(app.Processing())