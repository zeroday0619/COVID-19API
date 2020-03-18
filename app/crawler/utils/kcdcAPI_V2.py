import aiohttp


class KcdcApiV2:
    """대한민국 질병관리본부 COVID-19 웹 Request Class
    """
    def __init__(self):
        self.url = "http://ncov.mohw.go.kr/" # 대한민국 질병관리본부 COVID-19(코로나 바이러스 감염증-19 페이지) Home
        self.headers = {
            "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:74.0) Gecko/20100101 Firefox/74.0"
        }

    async def Request(self):
        """HTTP GET Request
        :return: html
        """
        async with aiohttp.ClientSession(headers=self.headers) as session:
            async with session.get(url=self.url) as resp:
                html = await resp.text()
        return html