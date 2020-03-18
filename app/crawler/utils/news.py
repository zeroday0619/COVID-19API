import aiohttp


class CoronaNewsCrawler:
    """COVID-19 | SARS-CoV-2 관련 네이버 뉴스 Crawler
    """
    def __init__(self):
        self.url = "https://search.naver.com/search.naver"
        self.payload = {
            "where": "news",
            "query": '코로나19 "코로나19" -정치 ',
            "oquery": '코로나19 "코로나19"',
            "mynews": '0',
            "tqi": "UEfQtdp0YiRssPppOAossssstyG-455013"
        }

    async def Request(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(url=self.url, params=self.payload) as resp:
                html = await resp.text()
        return html