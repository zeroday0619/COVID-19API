from .utils.csseAPI import CSSEParser


class CSSEApi:
    def __init__(self):
        self.data = CSSEParser()
    
    async def apiProcess(self):
        data = await self.data.return_wd_dat()
        return data