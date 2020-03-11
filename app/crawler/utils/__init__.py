from .kcdcAPI import kcdcAPI
from .kcdcAPI import Performance
import asyncio
import re


KcdcApi = kcdcAPI


async def cleanText(text):
    loop = Performance()
    # cleanT = await loop.run_in_executor(None, re.sub, "<.+?>", "", str(text), 0, re.I|re.S)
    cleanT = await loop.run_in_threadpool(lambda: re.sub("<.+?>", "", str(text), 0, re.I|re.S))
    return cleanT

async def JsonData(listdata):
    jsondata = [
            {"SEOUL":{"increase": float(listdata[5]),"patient": float(listdata[6]),"death": float(listdata[7]),"ratio": float(listdata[8]),"inspection": float(listdata[9])}},
            {"BUSAN":{"increase": float(listdata[10]),"patient": float(listdata[11]),"death": float(listdata[12]),"ratio": float(listdata[13]),"inspection": float(listdata[14])}},
            {"DAEGU":{"increase": float(listdata[15]),"patient": float(listdata[16]),"death": float(listdata[17]),"ratio": float(listdata[18]),"inspection": float(listdata[19])}},
            {"INCHEON":{"increase": float(listdata[20]),"patient": float(listdata[21]),"death": float(listdata[22]),"ratio": float(listdata[23]),"inspection": float(listdata[24])}},
            {"GWANGJU":{"increase": float(listdata[25]),"patient": float(listdata[26]),"death": float(listdata[27]),"ratio": float(listdata[28]),"inspection": float(listdata[29])}},
            {"DAEJEON":{"increase": float(listdata[30]),"patient": float(listdata[31]),"death": float(listdata[32]),"ratio": float(listdata[33]),"inspection": float(listdata[34])}},
            {"ULSAN":{"increase": float(listdata[35]),"patient": float(listdata[36]),"death": float(listdata[37]),"ratio": float(listdata[38]),"inspection": float(listdata[39])}},
            {"SEJONG":{"increase": float(listdata[40]),"patient": float(listdata[41]),"death": float(listdata[42]),"ratio": float(listdata[43]),"inspection": float(listdata[44])}},
            {"GYEONGGI":{"increase": float(listdata[45]),"patient": float(listdata[46]),"death": float(listdata[47]),"ratio": float(listdata[48]),"inspection": float(listdata[49])}},
            {"GANGWON":{"increase": float(listdata[50]),"patient": float(listdata[51]),"death": float(listdata[52]),"ratio": float(listdata[53]),"inspection": float(listdata[54])}},
            {"CHUNGBUK":{"increase": float(listdata[55]),"patient": float(listdata[56]),"death": float(listdata[57]),"ratio": float(listdata[58]),"inspection": float(listdata[59])}},
            {"CHUNGNAM":{"increase": float(listdata[60]),"patient": float(listdata[61]),"death": float(listdata[62]),"ratio": float(listdata[63]),"inspection": float(listdata[64])}},
            {"JEONBUK":{"increase": float(listdata[65]),"patient": float(listdata[66]),"death": float(listdata[67]),"ratio": float(listdata[68]),"inspection": float(listdata[69])}},
            {"JEONNAM":{"increase": float(listdata[70]),"patient": float(listdata[71]),"death": float(listdata[72]),"ratio": float(listdata[73]),"inspection": float(listdata[74])}},
            {"GYEONGBUK":{"increase": float(listdata[75]),"patient": float(listdata[76]),"death": float(listdata[77]),"ratio": float(listdata[78]),"inspection": float(listdata[79])}},
            {"GYEONGNAM":{"increase": float(listdata[80]),"patient": float(listdata[81]),"death": float(listdata[82]),"ratio": float(listdata[83]),"inspection": float(listdata[84])}},
            {"JEJU":{"increase": float(listdata[85]),"patient": float(listdata[86]),"death": float(listdata[87]),"ratio": float(listdata[88]),"inspection": float(listdata[89])}}
    ]
    return jsondata

async def NewsNogadaJsonData(a, b, c, d):
    """노가다"""
    #TODO: 노가다 노가다 노가다 노가다 노가다 노가다 노가다 노가다 노가다 노가다 노가다 노가다 노가다 노가다 노가다
    jsondata =[
        {
            "press": a[0],
            "title": b[0],
            "summary": c[0],
            "link": d[0]
        },
        {
            "press": a[1],
            "title": b[1],
            "summary": c[1],
            "link": d[1]
        },
        {
            "press": a[2],
            "title": b[2],
            "summary": c[2],
            "link": d[2]
        },
        {
            "press": a[3],
            "title": b[3],
            "summary": c[3],
            "link": d[3]
        },
        {
            "press": a[4],
            "title": b[4],
            "summary": c[4],
            "link": d[4]
        },
        {
            "press": a[5],
            "title": b[5],
            "summary": c[5],
            "link": d[5]
        },
        {
            "press": a[6],
            "title": b[6],
            "summary": c[6],
            "link": d[6]
        },
        {
            "press": a[7],
            "title": b[7],
            "summary": c[7],
            "link": d[7]
        },
        {
            "press": a[8],
            "title": b[8],
            "summary": c[8],
            "link": d[8]
        },
        {
            "press": a[9],
            "title": b[9],
            "summary": c[9],
            "link": d[9]
        }
    ]
    return jsondata