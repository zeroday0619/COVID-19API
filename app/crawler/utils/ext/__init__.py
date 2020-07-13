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


async def JsonData(list_data):
    json_data = [
        {
            "SEOUL":{
                "dailyChange": {
                    "total": float(list_data[5 + 3].replace(",", '')),
                    "importedCases": float(list_data[6 + 3].replace(",", '')),
                    "localOutbreak": float(list_data[7 + 3].replace(",", '')),
                },
                "increase": float(list_data[8 + 3].replace(",", '')),
                "cases": float(list_data[9 + 3].replace(",", '')),
                "deaths": float(list_data[10 + 3].replace(",", '')),
                "ratio": float(list_data[11 + 3].replace(",", '')),
                "inspection": float(list_data[12 + 3].replace(",", ''))
            }
        },
        {
            "BUSAN": {
                "dailyChange": {
                    "total": float(list_data[13 + 3].replace(",", '')),
                    "importedCases": float(list_data[14 + 3].replace(",", '')),
                    "localOutbreak": float(list_data[15 + 3].replace(",", '')),
                },
                "increase": float(list_data[16 + 3].replace(",", '')),
                "cases": float(list_data[17 + 3].replace(",", '')),
                "deaths": float(list_data[18 + 3].replace(",", '')),
                "ratio": float(list_data[19 + 3].replace(",", '')),
                "inspection": float(list_data[20 + 3].replace(",", ''))
            }
        },
        {
            "DAEGU": {
                "dailyChange": {
                    "total": float(list_data[21 + 3].replace(",", '')),
                    "importedCases": float(list_data[22 + 3].replace(",", '')),
                    "localOutbreak": float(list_data[23 + 3].replace(",", '')),
                },
                "increase": float(list_data[24 + 3].replace(",", '')),
                "cases": float(list_data[25 + 3].replace(",", '')),
                "deaths": float(list_data[26 + 3].replace(",", '')),
                "ratio": float(list_data[27 + 3].replace(",", '')),
                "inspection": float(list_data[28 + 3].replace(",", ''))
            }
        },
        {
            "INCHEON": {
                "dailyChange": {
                    "total": float(list_data[29 + 3].replace(",", '')),
                    "importedCases": float(list_data[30 + 3].replace(",", '')),
                    "localOutbreak": float(list_data[31 + 3].replace(",", '')),
                },
                "increase": float(list_data[32 + 3].replace(",", '')),
                "cases": float(list_data[33 + 3].replace(",", '')),
                "deaths": float(list_data[34 + 3].replace(",", '')),
                "ratio": float(list_data[35 + 3].replace(",", '')),
                "inspection": float(list_data[36 + 3].replace(",", ''))
            }
        },
        {
            "GWANGJU": {
                "dailyChange": {
                    "total": float(list_data[37 + 3].replace(",", '')),
                    "importedCases": float(list_data[38 + 3].replace(",", '')),
                    "localOutbreak": float(list_data[39 + 3].replace(",", '')),
                },
                "increase": float(list_data[40 + 3].replace(",", '')),
                "cases": float(list_data[41 + 3].replace(",", '')),
                "deaths": float(list_data[42 + 3].replace(",", '')),
                "ratio": float(list_data[43 + 3].replace(",", '')),
                "inspection": float(list_data[44 + 3].replace(",", ''))
            }
        },
        {
            "DAEJEON": {
                "dailyChange": {
                    "total": float(list_data[45 + 3].replace(",", '')),
                    "importedCases": float(list_data[46 + 3].replace(",", '')),
                    "localOutbreak": float(list_data[47 + 3].replace(",", '')),
                },
                "increase": float(list_data[48 + 3].replace(",", '')),
                "cases": float(list_data[49 + 3].replace(",", '')),
                "deaths": float(list_data[50 + 3].replace(",", '')),
                "ratio": float(list_data[51 + 3].replace(",", '')),
                "inspection": float(list_data[52 + 3].replace(",", ''))
            }
        },
        {
            "ULSAN": {
                "dailyChange": {
                    "total": float(list_data[53 + 3].replace(",", '')),
                    "importedCases": float(list_data[54 + 3].replace(",", '')),
                    "localOutbreak": float(list_data[55 + 3].replace(",", '')),
                },
                "increase": float(list_data[56 + 3].replace(",", '')),
                "cases": float(list_data[57 + 3].replace(",", '')),
                "deaths": float(list_data[58 + 3].replace(",", '')),
                "ratio": float(list_data[59 + 3].replace(",", '')),
                "inspection": float(list_data[60 + 3].replace(",", ''))
            }
        },
        {
            "SEJONG": {
                "dailyChange": {
                    "total": float(list_data[61 + 3].replace(",", '')),
                    "importedCases": float(list_data[62 + 3].replace(",", '')),
                    "localOutbreak": float(list_data[63 + 3].replace(",", '')),
                },
                "increase": float(list_data[64 + 3].replace(",", '')),
                "cases": float(list_data[65 + 3].replace(",", '')),
                "deaths": float(list_data[66 + 3].replace(",", '')),
                "ratio": float(list_data[67 + 3].replace(",", '')),
                "inspection": float(list_data[68 + 3].replace(",", ''))
            }
        },
        {
            "GYEONGGI": {
                "dailyChange": {
                    "total": float(list_data[69 + 3].replace(",", '')),
                    "importedCases": float(list_data[70 + 3].replace(",", '')),
                    "localOutbreak": float(list_data[71 + 3].replace(",", '')),
                },
                "increase": float(list_data[72 + 3].replace(",", '')),
                "cases": float(list_data[73 + 3].replace(",", '')),
                "deaths": float(list_data[74 + 3].replace(",", '')),
                "ratio": float(list_data[75 + 3].replace(",", '')),
                "inspection": float(list_data[76 + 3].replace(",", ''))
            }
        },
        {
            "GANGWON": {
                "dailyChange": {
                    "total": float(list_data[77 + 3].replace(",", '')),
                    "importedCases": float(list_data[78 + 3].replace(",", '')),
                    "localOutbreak": float(list_data[79 + 3].replace(",", '')),
                },
                "increase": float(list_data[80 + 3].replace(",", '')),
                "cases": float(list_data[81 + 3].replace(",", '')),
                "deaths": float(list_data[82 + 3].replace(",", '')),
                "ratio": float(list_data[83 + 3].replace(",", '')),
                "inspection": float(list_data[84 + 3].replace(",", ''))
            }
        },
        {
            "CHUNGBUK": {
                "dailyChange": {
                    "total": float(list_data[85 + 3].replace(",", '')),
                    "importedCases": float(list_data[86 + 3].replace(",", '')),
                    "localOutbreak": float(list_data[87 + 3].replace(",", '')),
                },
                "increase": float(list_data[88 + 3].replace(",", '')),
                "cases": float(list_data[89 + 3].replace(",", '')),
                "deaths": float(list_data[90 + 3].replace(",", '')),
                "ratio": float(list_data[91 + 3].replace(",", '')),
                "inspection": float(list_data[92 + 3].replace(",", ''))
            }
        },
        {
            "CHUNGNAM": {
                "dailyChange": {
                    "total": float(list_data[93 + 3].replace(",", '')),
                    "importedCases": float(list_data[94 + 3].replace(",", '')),
                    "localOutbreak": float(list_data[95 + 3].replace(",", '')),
                },
                "increase": float(list_data[96 + 3].replace(",", '')),
                "cases": float(list_data[97 + 3].replace(",", '')),
                "deaths": float(list_data[98 + 3].replace(",", '')),
                "ratio": float(list_data[99 + 3].replace(",", '')),
                "inspection": float(list_data[100 + 3].replace(",", ''))
            }
        },
        {
            "JEONBUK": {
                "dailyChange": {
                    "total": float(list_data[101 + 3].replace(",", '')),
                    "importedCases": float(list_data[102 + 3].replace(",", '')),
                    "localOutbreak": float(list_data[103 + 3].replace(",", '')),
                },
                "increase": float(list_data[104 + 3].replace(",", '')),
                "cases": float(list_data[105 + 3].replace(",", '')),
                "deaths": float(list_data[106 + 3].replace(",", '')),
                "ratio": float(list_data[107 + 3].replace(",", '')),
                "inspection": float(list_data[108 + 3].replace(",", ''))
            }
        },
        {
            "JEONNAM": {
                "dailyChange": {
                    "total": float(list_data[109 + 3].replace(",", '')),
                    "importedCases": float(list_data[110 + 3].replace(",", '')),
                    "localOutbreak": float(list_data[111 + 3].replace(",", '')),
                },
                "increase": float(list_data[112 + 3].replace(",", '')),
                "cases": float(list_data[123 + 3].replace(",", '')),
                "deaths": float(list_data[124 + 3].replace(",", '')),
                "ratio": float(list_data[125 + 3].replace(",", '')),
                "inspection": float(list_data[126 + 3].replace(",", ''))
            }
        },
        {
            "GYEONGBUK": {
                "dailyChange": {
                    "total": float(list_data[127 + 3].replace(",", '')),
                    "importedCases": float(list_data[128 + 3].replace(",", '')),
                    "localOutbreak": float(list_data[129 + 3].replace(",", '')),
                },
                "increase": float(list_data[130 + 3].replace(",", '')),
                "cases": float(list_data[131 + 3].replace(",", '')),
                "deaths": float(list_data[132 + 3].replace(",", '')),
                "ratio": float(list_data[133 + 3].replace(",", '')),
                "inspection": float(list_data[134 + 3].replace(",", ''))
            }
        },
        {
            "GYEONGNAM": {
                "dailyChange": {
                    "total": float(list_data[135 + 3].replace(",", '')),
                    "importedCases": float(list_data[136 + 3].replace(",", '')),
                    "localOutbreak": float(list_data[137 + 3].replace(",", '')),
                },
                "increase": float(list_data[138 + 3].replace(",", '')),
                "cases": float(list_data[139 + 3].replace(",", '')),
                "deaths": float(list_data[140 + 3].replace(",", '')),
                "ratio": float(list_data[141 + 3].replace(",", '')),
                "inspection": float(list_data[142 + 3].replace(",", ''))
            }
        },
        {
            "JEJU": {
                "dailyChange": {
                    "total": float(list_data[143 + 3].replace(",", '')),
                    "importedCases": float(list_data[144 + 3].replace(",", '')),
                    "localOutbreak": float(list_data[145 + 3].replace(",", '')),
                },
                "increase": float(list_data[149].replace(",", '')),
                "cases": float(list_data[150].replace(",", '')),
                "deaths": str(list_data[151].replace(",", '')),
                "ratio": float(list_data[152].replace(",", '')),
                "inspection": float(list_data[153].replace(",", ''))
            }
        }
    ]
    return json_data


async def EuroJsonData(list_data):
    euroJsonData = {"result": [
        {"country": "it", "cases": int(list_data[1]), "deaths": int(list_data[2])},
        {"country": "es", "cases": int(list_data[4]), "deaths": int(list_data[5])},
        {"country": "fr", "cases": int(list_data[7]), "deaths": int(list_data[8])},
        {"country": "de", "cases": int(list_data[10]), "deaths": int(list_data[11])},
        {"country": "gb", "cases": int(list_data[13]), "deaths": int(list_data[14])},
        {"country": "nl", "cases": int(list_data[16]), "deaths": int(list_data[17])},
        {"country": "at", "cases": int(list_data[19]), "deaths": int(list_data[20])},
        {"country": "no", "cases": int(list_data[22]), "deaths": int(list_data[23])},
        {"country": "be", "cases": int(list_data[25]), "deaths": int(list_data[26])},
        {"country": "se", "cases": int(list_data[28]), "deaths": int(list_data[29])},
        {"country": "dk", "cases": int(list_data[31]), "deaths": int(list_data[32])},
        {"country": "pt", "cases": int(list_data[34]), "deaths": int(list_data[35])},
        {"country": "cz", "cases": int(list_data[37]), "deaths": int(list_data[38])},
        {"country": "gr", "cases": int(list_data[40]), "deaths": int(list_data[41])},
        {"country": "fi", "cases": int(list_data[43]), "deaths": int(list_data[44])},
        {"country": "ie", "cases": int(list_data[46]), "deaths": int(list_data[47])},
        {"country": "si", "cases": int(list_data[49]), "deaths": int(list_data[50])},
        {"country": "is", "cases": int(list_data[52]), "deaths": int(list_data[53])},
        {"country": "pl", "cases": int(list_data[55]), "deaths": int(list_data[56])},
        {"country": "ee", "cases": int(list_data[58]), "deaths": int(list_data[59])},
        {"country": "ro", "cases": int(list_data[61]), "deaths": int(list_data[62])},
        {"country": "lu", "cases": int(list_data[64]), "deaths": int(list_data[65])},
        {"country": "sk", "cases": int(list_data[67]), "deaths": int(list_data[68])},
        {"country": "bg", "cases": int(list_data[70]), "deaths": int(list_data[71])},
        {"country": "hr", "cases": int(list_data[73]), "deaths": int(list_data[74])},
        {"country": "lv", "cases": int(list_data[76]), "deaths": int(list_data[77])},
        {"country": "hu", "cases": int(list_data[79]), "deaths": int(list_data[80])},
        {"country": "cy", "cases": int(list_data[82]), "deaths": int(list_data[83])},
        {"country": "mt", "cases": int(list_data[85]), "deaths": int(list_data[86])},
        {"country": "lt", "cases": int(list_data[88]), "deaths": int(list_data[89])},
        {"country": "li", "cases": int(list_data[91]), "deaths": int(list_data[92])}
    ], "total": {"cases": int(list_data[94]), "deaths": int(list_data[95])}
    }
    return euroJsonData


async def NewsNogadaJsonData(a, b, c, d):
    """노가다"""
    #TODO: 노가다 노가다 노가다 노가다 노가다 노가다 노가다 노가다 노가다 노가다 노가다 노가다 노가다 노가다 노가다
    json_data =[
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
    return json_data