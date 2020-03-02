import aiohttp
import asyncio
import ujson

class InfectiousDiseasesbyRegion:
    def __init__(self):
        self.url = "https://m.search.naver.com/p/csearch/content/nqapirender.nhn"
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
        self.Templit = {
            "Region": None,
            "ConfirmationNumberPatients": None,
            "Ratio": None,
        }
        self.listdata = []

    async def Get(self):
        async with aiohttp.ClientSession(headers=self.headers) as session:
            async with session.get(url=self.url, params=self.payload) as resp:
                JsonData = await resp.json()
        return JsonData

    async def Search(self):
        IDR = InfectiousDiseasesbyRegion()
        jsondata = await IDR.Get()
        data = jsondata['result']['regions']
        length = len(data)
        # 17
        listdata = self.listdata
        for i in range(length):
            Templit = self.Templit
            Templit['Region'] = data[i]['title']
            Templit['ConfirmationNumberPatients'] = data[i]['count']
            Templit['Ratio'] = data[i]['rate']
            listdata.append(Templit)
        return listdata

def main():
    loop = asyncio.get_event_loop()
    data = InfectiousDiseasesbyRegion()
    db = loop.run_until_complete(data.Search())
    loop.close()
    print(db)

main()