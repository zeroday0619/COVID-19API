import aiohttp


class MsnCovid:
    def __init__(self):
        self.url = "https://www.bing.com/covid"
        self.headers = {
            "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:74.0) Gecko/20100101 Firefox/74.0"
        }

    async def MsnRequest(self):
        async with aiohttp.ClientSession(headers=self.headers) as session:
            async with session.get(url=self.url) as resp:
                HTML = await resp.text()
        return HTML