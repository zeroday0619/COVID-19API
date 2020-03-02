import asyncio
import aiohttp
import lxml
import re
from bs4 import BeautifulSoup

def cleanText(text):
    cleanT = re.sub('<.+?>', '', str(text))
    return cleanT

async def GetInfectiousDiseases():
    loop = asyncio.get_event_loop()
    url = "http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=&brdGubun=&ncvContSeq=&contSeq=&board_id=&gubun="
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            info = await resp.text()
    soup = await loop.run_in_executor(None, BeautifulSoup, info, 'lxml')
    return soup

async def ConfirmationPatient():
    soup = await GetInfectiousDiseases()
    td = soup.select("#content > div > div.bv_content > div > div:nth-child(3) > table > tbody > tr:nth-child(1) > td")
    cp = cleanText(text=td[0])
    return cp

async def ConfirmationPatientIsolation():
    soup = await GetInfectiousDiseases()
    td = soup.select("#content > div > div.bv_content > div > div:nth-child(3) > table > tbody > tr:nth-child(2) > td")
    xp = cleanText(text=td[0])
    return xp

async def Dead():
    soup = await GetInfectiousDiseases()
    td = soup.select("#content > div > div.bv_content > div > div:nth-child(3) > table > tbody > tr:nth-child(3) > td")
    vp = cleanText(text=td[0])
    return vp

async def Inspection():
    soup = await GetInfectiousDiseases()
    td = soup.select("#content > div > div.bv_content > div > div:nth-child(3) > table > tbody > tr:nth-child(4) > td")
    xo = cleanText(text=td[0])
    return xo

