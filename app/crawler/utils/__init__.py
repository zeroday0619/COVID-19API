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
    jsondata = [{
            "SEOUL":{"increase": listdata[5],"patient": listdata[6],"death": listdata[7],"ratio": listdata[8],"inspection": listdata[9]},
            "BUSAN":{"increase": listdata[10],"patient": listdata[11],"death": listdata[12],"ratio": listdata[13],"inspection": listdata[14]},
            "DAEGU":{"increase": listdata[15],"patient": listdata[16],"death": listdata[17],"ratio": listdata[18],"inspection": listdata[19]},
            "INCHEON":{"increase": listdata[20],"patient": listdata[21],"death": listdata[22],"ratio": listdata[23],"inspection": listdata[24]},
            "GWANGJU":{"increase": listdata[25],"patient": listdata[26],"death": listdata[27],"ratio": listdata[28],"inspection": listdata[29]},
            "DAEJEON":{"increase": listdata[30],"patient": listdata[31],"death": listdata[32],"ratio": listdata[33],"inspection": listdata[34]},
            "ULSAN":{"increase": listdata[35],"patient": listdata[36],"death": listdata[37],"ratio": listdata[38],"inspection": listdata[39]},
            "SEJONG":{"increase": listdata[40],"patient": listdata[41],"death": listdata[42],"ratio": listdata[43],"inspection": listdata[44]},
            "GYEONGGI":{"increase": listdata[45],"patient": listdata[46],"death": listdata[47],"ratio": listdata[48],"inspection": listdata[49]},
            "GANGWON":{"increase": listdata[50],"patient": listdata[51],"death": listdata[52],"ratio": listdata[53],"inspection": listdata[54]},
            "CHUNGBUK":{"increase": listdata[55],"patient": listdata[56],"death": listdata[57],"ratio": listdata[58],"inspection": listdata[59]},
            "CHUNGNAM":{"increase": listdata[60],"patient": listdata[61],"death": listdata[62],"ratio": listdata[63],"inspection": listdata[64]},
            "JEONBUK":{"increase": listdata[65],"patient": listdata[66],"death": listdata[67],"ratio": listdata[68],"inspection": listdata[69]},
            "JEONNAM":{"increase": listdata[70],"patient": listdata[71],"death": listdata[72],"ratio": listdata[73],"inspection": listdata[74]},
            "GYEONGBUK":{"increase": listdata[75],"patient": listdata[76],"death": listdata[77],"ratio": listdata[78],"inspection": listdata[79]},
            "GYEONGNAM":{"increase": listdata[80],"patient": listdata[81],"death": listdata[82],"ratio": listdata[83],"inspection": listdata[84]},
            "JEJU":{"increase": listdata[85],"patient": listdata[86],"death": listdata[87],"ratio": listdata[88],"inspection": listdata[89]}
    }]
    return jsondata