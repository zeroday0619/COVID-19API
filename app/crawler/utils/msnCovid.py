from async_lru import alru_cache
import aiohttp


class MsnCovid:
    def __init__(self):
        self.url = "https://www.bing.com/covid/data?IG=7CB83DF3C0334A0081A1DC0460B47766"
        self.headers = {
            "dnt": "1",
            "referer": "https://www.bing.com/covid",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36 Edg/80.0.361.69"

        }

    @alru_cache(maxsize=32)
    async def MsnRequest(self):
        async with aiohttp.ClientSession(headers=self.headers) as session:
            async with session.get(url=self.url) as resp:
                _json = await resp.json()
        return _json