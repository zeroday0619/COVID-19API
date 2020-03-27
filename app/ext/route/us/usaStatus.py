from app.crawler.us.usa import Usa
from fastapi import HTTPException
from app.ext.utils.Performance import Performance
import ujson


class UsaCovid19:
    def __init__(self):
        self.loop = Performance()
        self.source = Usa()

    async def StatesCovidStatus(self, cache):
        if not await cache.exists('usa'):
            source = await self.source.StatesProcess()
            jsondata = {
                "usa": source
            }
            converted = await self.loop.run_in_threadpool(lambda: ujson.dumps(jsondata).encode('utf-8'))
            await cache.set('usa', converted, expire=3600)
            return jsondata["usa"]
        else:
            NoneConverted = await cache.get('usa', encoding='utf-8')
            Converted = await self.loop.run_in_threadpool(lambda: ujson.loads(NoneConverted))
            return Converted["usa"]

    async def StatesCovidSearcher(self, cache, state):
        if not await cache.exists(state.lower()):
            try:
                source = await self.source.StatesProcess()
                for index in source:
                    n = index['state']
                    if n.lower() == state.lower():
                        jsonData = {
                            state: {
                                "state": index['state'].lower(),
                                "totalCases": index['totalConfirmed'],
                                "totalDeaths": index['totalDeaths'],
                                "totalRecovered": index['totalRecovered'],
                                "lastUpdated": index['lastUpdated']
                            }
                        }
                        data = jsonData
                        _data = await self.loop.run_in_threadpool(
                            lambda: ujson.dumps(
                                data, ensure_ascii=False,
                                escape_forward_slashes=False,
                                sort_keys=False
                            ).encode('utf-8')
                        )
                        await cache.set(state.lower(), _data, expire=3600)
                        return data[state.lower()]
            except Exception as x:
                raise HTTPException(status_code=422, detail=f"Validation Error {str(x)}")
        else:
            NoneConverted = await cache.get(state)
            Converted = await self.loop.run_in_threadpool(lambda: ujson.loads(NoneConverted))
            return Converted[state.lower()]