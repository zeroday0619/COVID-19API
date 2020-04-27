from app.ext.utils.Performance import Performance
from app.crawler.utils.kr.kcdcAPI import kcdcAPI
import re


KcdcApi = kcdcAPI


async def cleanText(text):
    loop = Performance()
    # cleanT = await loop.run_in_executor(None, re.sub, "<.+?>", "", str(text), 0, re.I|re.S)
    cleanT = await loop.run_in_threadpool(lambda: re.sub("<.+?>", "", str(text), 0, re.I|re.S))
    return cleanT.replace("-", "0").replace(",", "")

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
        {
            "SEOUL":{
                "dailyChange": {
                    "total": float(listdata[5+3].replace(",", '')),
                    "importedCases": float(listdata[6+3].replace(",", '')),
                    "localOutbreak": float(listdata[7+3].replace(",", '')),
                },
                "increase": float(listdata[8+3].replace(",", '')),
                "cases": float(listdata[9+3].replace(",", '')),
                "deaths": float(listdata[10+3].replace(",", '')),
                "ratio": float(listdata[11+3].replace(",", '')),
                "inspection": float(listdata[12+3].replace(",", ''))
            }
        },
        {
            "BUSAN": {
                "dailyChange": {
                    "total": float(listdata[13+3].replace(",", '')),
                    "importedCases": float(listdata[14+3].replace(",", '')),
                    "localOutbreak": float(listdata[15+3].replace(",", '')),
                },
                "increase": float(listdata[16+3].replace(",", '')),
                "cases": float(listdata[17+3].replace(",", '')),
                "deaths": float(listdata[18+3].replace(",", '')),
                "ratio": float(listdata[19+3].replace(",", '')),
                "inspection": float(listdata[20+3].replace(",", ''))
            }
        },
        {
            "DAEGU": {
                "dailyChange": {
                    "total": float(listdata[21+3].replace(",", '')),
                    "importedCases": float(listdata[22+3].replace(",", '')),
                    "localOutbreak": float(listdata[23+3].replace(",", '')),
                },
                "increase": float(listdata[24+3].replace(",", '')),
                "cases": float(listdata[25+3].replace(",", '')),
                "deaths": float(listdata[26+3].replace(",", '')),
                "ratio": float(listdata[27+3].replace(",", '')),
                "inspection": float(listdata[28+3].replace(",", ''))
            }
        },
        {
            "INCHEON": {
                "dailyChange": {
                    "total": float(listdata[29+3].replace(",", '')),
                    "importedCases": float(listdata[30+3].replace(",", '')),
                    "localOutbreak": float(listdata[31+3].replace(",", '')),
                },
                "increase": float(listdata[32+3].replace(",", '')),
                "cases": float(listdata[33+3].replace(",", '')),
                "deaths": float(listdata[34+3].replace(",", '')),
                "ratio": float(listdata[35+3].replace(",", '')),
                "inspection": float(listdata[36+3].replace(",", ''))
            }
        },
        {
            "GWANGJU": {
                "dailyChange": {
                    "total": float(listdata[37+3].replace(",", '')),
                    "importedCases": float(listdata[38+3].replace(",", '')),
                    "localOutbreak": float(listdata[39+3].replace(",", '')),
                },
                "increase": float(listdata[40+3].replace(",", '')),
                "cases": float(listdata[41+3].replace(",", '')),
                "deaths": float(listdata[42+3].replace(",", '')),
                "ratio": float(listdata[43+3].replace(",", '')),
                "inspection": float(listdata[44+3].replace(",", ''))
            }
        },
        {
            "DAEJEON": {
                "dailyChange": {
                    "total": float(listdata[45+3].replace(",", '')),
                    "importedCases": float(listdata[46+3].replace(",", '')),
                    "localOutbreak": float(listdata[47+3].replace(",", '')),
                },
                "increase": float(listdata[48+3].replace(",", '')),
                "cases": float(listdata[49+3].replace(",", '')),
                "deaths": float(listdata[50+3].replace(",", '')),
                "ratio": float(listdata[51+3].replace(",", '')),
                "inspection": float(listdata[52+3].replace(",", ''))
            }
        },
        {
            "ULSAN": {
                "dailyChange": {
                    "total": float(listdata[53+3].replace(",", '')),
                    "importedCases": float(listdata[54+3].replace(",", '')),
                    "localOutbreak": float(listdata[55+3].replace(",", '')),
                },
                "increase": float(listdata[56+3].replace(",", '')),
                "cases": float(listdata[57+3].replace(",", '')),
                "deaths": float(listdata[58+3].replace(",", '')),
                "ratio": float(listdata[59+3].replace(",", '')),
                "inspection": float(listdata[60+3].replace(",", ''))
            }
        },
        {
            "SEJONG": {
                "dailyChange": {
                    "total": float(listdata[61+3].replace(",", '')),
                    "importedCases": float(listdata[62+3].replace(",", '')),
                    "localOutbreak": float(listdata[63+3].replace(",", '')),
                },
                "increase": float(listdata[64+3].replace(",", '')),
                "cases": float(listdata[65+3].replace(",", '')),
                "deaths": float(listdata[66+3].replace(",", '')),
                "ratio": float(listdata[67+3].replace(",", '')),
                "inspection": float(listdata[68+3].replace(",", ''))
            }
        },
        {
            "GYEONGGI": {
                "dailyChange": {
                    "total": float(listdata[69+3].replace(",", '')),
                    "importedCases": float(listdata[70+3].replace(",", '')),
                    "localOutbreak": float(listdata[71+3].replace(",", '')),
                },
                "increase": float(listdata[72+3].replace(",", '')),
                "cases": float(listdata[73+3].replace(",", '')),
                "deaths": float(listdata[74+3].replace(",", '')),
                "ratio": float(listdata[75+3].replace(",", '')),
                "inspection": float(listdata[76+3].replace(",", ''))
            }
        },
        {
            "GANGWON": {
                "dailyChange": {
                    "total": float(listdata[77+3].replace(",", '')),
                    "importedCases": float(listdata[78+3].replace(",", '')),
                    "localOutbreak": float(listdata[79+3].replace(",", '')),
                },
                "increase": float(listdata[80+3].replace(",", '')),
                "cases": float(listdata[81+3].replace(",", '')),
                "deaths": float(listdata[82+3].replace(",", '')),
                "ratio": float(listdata[83+3].replace(",", '')),
                "inspection": float(listdata[84+3].replace(",", ''))
            }
        },
        {
            "CHUNGBUK": {
                "dailyChange": {
                    "total": float(listdata[85+3].replace(",", '')),
                    "importedCases": float(listdata[86+3].replace(",", '')),
                    "localOutbreak": float(listdata[87+3].replace(",", '')),
                },
                "increase": float(listdata[88+3].replace(",", '')),
                "cases": float(listdata[89+3].replace(",", '')),
                "deaths": float(listdata[90+3].replace(",", '')),
                "ratio": float(listdata[91+3].replace(",", '')),
                "inspection": float(listdata[92+3].replace(",", ''))
            }
        },
        {
            "CHUNGNAM": {
                "dailyChange": {
                    "total": float(listdata[93+3].replace(",", '')),
                    "importedCases": float(listdata[94+3].replace(",", '')),
                    "localOutbreak": float(listdata[95+3].replace(",", '')),
                },
                "increase": float(listdata[96+3].replace(",", '')),
                "cases": float(listdata[97+3].replace(",", '')),
                "deaths": float(listdata[98+3].replace(",", '')),
                "ratio": float(listdata[99+3].replace(",", '')),
                "inspection": float(listdata[100+3].replace(",", ''))
            }
        },
        {
            "JEONBUK": {
                "dailyChange": {
                    "total": float(listdata[101+3].replace(",", '')),
                    "importedCases": float(listdata[102+3].replace(",", '')),
                    "localOutbreak": float(listdata[103+3].replace(",", '')),
                },
                "increase": float(listdata[104+3].replace(",", '')),
                "cases": float(listdata[105+3].replace(",", '')),
                "deaths": float(listdata[106+3].replace(",", '')),
                "ratio": float(listdata[107+3].replace(",", '')),
                "inspection": float(listdata[108+3].replace(",", ''))
            }
        },
        {
            "JEONNAM": {
                "dailyChange": {
                    "total": float(listdata[109+3].replace(",", '')),
                    "importedCases": float(listdata[110+3].replace(",", '')),
                    "localOutbreak": float(listdata[111+3].replace(",", '')),
                },
                "increase": float(listdata[112+3].replace(",", '')),
                "cases": float(listdata[123+3].replace(",", '')),
                "deaths": float(listdata[124+3].replace(",", '')),
                "ratio": float(listdata[125+3].replace(",", '')),
                "inspection": float(listdata[126+3].replace(",", ''))
            }
        },
        {
            "GYEONGBUK": {
                "dailyChange": {
                    "total": float(listdata[127+3].replace(",", '')),
                    "importedCases": float(listdata[128+3].replace(",", '')),
                    "localOutbreak": float(listdata[129+3].replace(",", '')),
                },
                "increase": float(listdata[130+3].replace(",", '')),
                "cases": float(listdata[131+3].replace(",", '')),
                "deaths": float(listdata[132+3].replace(",", '')),
                "ratio": float(listdata[133+3].replace(",", '')),
                "inspection": float(listdata[134+3].replace(",", ''))
            }
        },
        {
            "GYEONGNAM": {
                "dailyChange": {
                    "total": float(listdata[135+3].replace(",", '')),
                    "importedCases": float(listdata[136+3].replace(",", '')),
                    "localOutbreak": float(listdata[137+3].replace(",", '')),
                },
                "increase": float(listdata[138+3].replace(",", '')),
                "cases": float(listdata[139+3].replace(",", '')),
                "deaths": float(listdata[140+3].replace(",", '')),
                "ratio": float(listdata[141+3].replace(",", '')),
                "inspection": float(listdata[142+3].replace(",", ''))
            }
        },
        {
            "JEJU": {
                "dailyChange": {
                    "total": float(listdata[143+3].replace(",", '')),
                    "importedCases": float(listdata[144+3].replace(",", '')),
                    "localOutbreak": float(listdata[145+3].replace(",", '')),
                },
                "increase": float(listdata[149].replace(",", '')),
                "cases": float(listdata[150].replace(",", '')),
                "deaths": str(listdata[151].replace(",", '')),
                "ratio": float(listdata[152].replace(",", '')),
                "inspection": float(listdata[153].replace(",", ''))
            }
        }
    ]
    return jsondata


async def EuroJsonData(listdata):
    euroJsonData = {"result": [
        {"country": "it", "cases": int(listdata[1]), "deaths": int(listdata[2])},
        {"country": "es", "cases": int(listdata[4]), "deaths": int(listdata[5])},
        {"country": "fr", "cases": int(listdata[7]), "deaths": int(listdata[8])},
        {"country": "de", "cases": int(listdata[10]), "deaths": int(listdata[11])},
        {"country": "gb", "cases": int(listdata[13]), "deaths": int(listdata[14])},
        {"country": "nl", "cases": int(listdata[16]), "deaths": int(listdata[17])},
        {"country": "at", "cases": int(listdata[19]), "deaths": int(listdata[20])},
        {"country": "no", "cases": int(listdata[22]), "deaths": int(listdata[23])},
        {"country": "be", "cases": int(listdata[25]), "deaths": int(listdata[26])},
        {"country": "se", "cases": int(listdata[28]), "deaths": int(listdata[29])},
        {"country": "dk", "cases": int(listdata[31]), "deaths": int(listdata[32])},
        {"country": "pt", "cases": int(listdata[34]), "deaths": int(listdata[35])},
        {"country": "cz", "cases": int(listdata[37]), "deaths": int(listdata[38])},
        {"country": "gr", "cases": int(listdata[40]), "deaths": int(listdata[41])},
        {"country": "fi", "cases": int(listdata[43]), "deaths": int(listdata[44])},
        {"country": "ie", "cases": int(listdata[46]), "deaths": int(listdata[47])},
        {"country": "si", "cases": int(listdata[49]), "deaths": int(listdata[50])},
        {"country": "is", "cases": int(listdata[52]), "deaths": int(listdata[53])},
        {"country": "pl", "cases": int(listdata[55]), "deaths": int(listdata[56])},
        {"country": "ee", "cases": int(listdata[58]), "deaths": int(listdata[59])},
        {"country": "ro", "cases": int(listdata[61]), "deaths": int(listdata[62])},
        {"country": "lu", "cases": int(listdata[64]), "deaths": int(listdata[65])},
        {"country": "sk", "cases": int(listdata[67]), "deaths": int(listdata[68])},
        {"country": "bg", "cases": int(listdata[70]), "deaths": int(listdata[71])},
        {"country": "hr", "cases": int(listdata[73]), "deaths": int(listdata[74])},
        {"country": "lv", "cases": int(listdata[76]), "deaths": int(listdata[77])},
        {"country": "hu", "cases": int(listdata[79]), "deaths": int(listdata[80])},
        {"country": "cy", "cases": int(listdata[82]), "deaths": int(listdata[83])},
        {"country": "mt", "cases": int(listdata[85]), "deaths": int(listdata[86])},
        {"country": "lt", "cases": int(listdata[88]), "deaths": int(listdata[89])},
        {"country": "li", "cases": int(listdata[91]), "deaths": int(listdata[92])}
    ], "total": {"cases": int(listdata[94]), "deaths": int(listdata[95])}
    }
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