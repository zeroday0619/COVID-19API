from app.ext.utils.Performance import Performance
from .utils.msnCovid import MsnCovid


class Usa:
    def __init__(self):
        self.loop = Performance()
        self.source = MsnCovid()

    async def Process(self):
        global states
        source = await self.source.MsnRequest()
        for index in source['areas']:
            if index['id'] == "unitedstates":
                states = index['areas']
        return states

    async def StatesProcess(self):
        source = await self.Process()
        ListA = []
        for index in source:
            jsonTemplit = {
                "state": index['displayName'],
                "totalConfirmed": index['totalConfirmed'],
                "totalDeaths": index['totalDeaths'],
                "totalRecovered": index['totalRecovered'],
                "lastUpdated": index['lastUpdated']
            }
            ListA.append(jsonTemplit)
        return ListA