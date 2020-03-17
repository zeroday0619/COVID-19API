from .utils.csseAPI import CSSEParser
import ujson
import asyncio
class CSSEApi:
    def __init__(self):
        self.data = CSSEParser()
    
    async def apiProcess(self):
        data = await asyncio.gather(self.data.return_wd_dat())
        return data