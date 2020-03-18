from app.ext.utils.Performance import Performance
from .kcdcAPI import kcdcAPI
import re


KcdcApi = kcdcAPI


async def cleanText(text):
    loop = Performance()
    # cleanT = await loop.run_in_executor(None, re.sub, "<.+?>", "", str(text), 0, re.I|re.S)
    cleanT = await loop.run_in_threadpool(lambda: re.sub("<.+?>", "", str(text), 0, re.I|re.S))
    return cleanT

def chunker(seq, size=3):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))

async def StringToInteger(string):
    """StringToInteger는 float Type은 처리 할 수 없습니다.\n
    Only String To Integer
    """
    loop = Performance()
    __Integer = await loop.run_in_threadpool(lambda: string.replace(",", '').replace("(", '').replace(")", '').replace(",", '').replace(" ", '').replace("전일대비", '').strip())
    converted = int(__Integer)
    return converted


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

async def EuroJsonData(listdata):
    euroJsonData = [
        {listdata[0]: {"Cases": int(listdata[1]), "Deaths": int(listdata[2])}},
        {listdata[3]: {"Cases": int(listdata[4]), "Deaths": int(listdata[5])}},
        {listdata[6]: {"Cases": int(listdata[7]), "Deaths": int(listdata[8])}},
        {listdata[9]: {"Cases": int(listdata[10]), "Deaths": int(listdata[11])}},
        {listdata[12]: {"Cases": int(listdata[13]), "Deaths": int(listdata[14])}},
        {listdata[15]: {"Cases": int(listdata[16]), "Deaths": int(listdata[17])}},
        {listdata[18]: {"Cases": int(listdata[19]), "Deaths": int(listdata[20])}},
        {listdata[21]: {"Cases": int(listdata[22]), "Deaths": int(listdata[23])}},
        {listdata[24]: {"Cases": int(listdata[25]), "Deaths": int(listdata[26])}},
        {listdata[27]: {"Cases": int(listdata[28]), "Deaths": int(listdata[29])}},
        {listdata[30]: {"Cases": int(listdata[31]), "Deaths": int(listdata[32])}},
        {listdata[33]: {"Cases": int(listdata[34]), "Deaths": int(listdata[35])}},
        {listdata[36]: {"Cases": int(listdata[37]), "Deaths": int(listdata[38])}},
        {listdata[39]: {"Cases": int(listdata[40]), "Deaths": int(listdata[41])}},
        {listdata[42]: {"Cases": int(listdata[43]), "Deaths": int(listdata[44])}},
        {listdata[45]: {"Cases": int(listdata[46]), "Deaths": int(listdata[47])}},
        {listdata[48]: {"Cases": int(listdata[49]), "Deaths": int(listdata[50])}},
        {listdata[51]: {"Cases": int(listdata[52]), "Deaths": int(listdata[53])}},
        {listdata[54]: {"Cases": int(listdata[55]), "Deaths": int(listdata[56])}},
        {listdata[57]: {"Cases": int(listdata[58]), "Deaths": int(listdata[59])}},
        {listdata[60]: {"Cases": int(listdata[61]), "Deaths": int(listdata[62])}},
        {listdata[63]: {"Cases": int(listdata[64]), "Deaths": int(listdata[65])}},
        {listdata[66]: {"Cases": int(listdata[67]), "Deaths": int(listdata[68])}},
        {listdata[69]: {"Cases": int(listdata[70]), "Deaths": int(listdata[71])}},
        {listdata[72]: {"Cases": int(listdata[73]), "Deaths": int(listdata[74])}},
        {listdata[75]: {"Cases": int(listdata[76]), "Deaths": int(listdata[77])}},
        {listdata[78]: {"Cases": int(listdata[79]), "Deaths": int(listdata[80])}},
        {listdata[81]: {"Cases": int(listdata[82]), "Deaths": int(listdata[83])}},
        {listdata[84]: {"Cases": int(listdata[85]), "Deaths": int(listdata[86])}},
        {listdata[87]: {"Cases": int(listdata[88]), "Deaths": int(listdata[89])}},
        {listdata[90]: {"Cases": int(listdata[91]), "Deaths": int(listdata[92])}},
        {listdata[93]: {"Cases": int(listdata[94]), "Deaths": int(listdata[95])}}
    ]
    return euroJsonData

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

