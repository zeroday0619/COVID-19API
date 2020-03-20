import ujson
from app.crawler.csse import CSSEApi
from app.crawler.WorldStatus import CoronaVirusDiseaseStatus
from fastapi import HTTPException

async def globalStatus(cache, loop):
    if not await cache.exists('global'):
        ads = CSSEApi()
        data = await ads.apiProcess()
        global_ = {
            "global": data
        }
        _global = await loop.run_in_threadpool(
            lambda: ujson.dumps(global_, ensure_ascii=False, escape_forward_slashes=False, sort_keys=True).encode(
                'utf-8'))
        await cache.set('global', _global, expire=3600)
        return global_
    else:
        global_ = await cache.get('global')
        _global = await loop.run_in_threadpool(lambda: ujson.loads(global_))
        return _global


async def GlobalCoronaStatus(cache, loop):
    if not await cache.exists('world'):
        source = CoronaVirusDiseaseStatus()
        data = await source.GlobalCoronaVirusDisease()
        gcs_ = {
            "world": data
        }
        _gcs = await loop.run_in_threadpool(
            lambda: ujson.dumps(gcs_, ensure_ascii=False, escape_forward_slashes=False, sort_keys=True).encode(
                'utf-8'))
        await cache.set('world', _gcs, expire=3600)
        return gcs_
    else:
        gcs_ = await cache.get('world')
        _gcs = await loop.run_in_threadpool(lambda: ujson.loads(gcs_))
        return _gcs


async def GlobalCoronaSearch(cache, loop, location):
    if not await cache.exists(location):
        source = CoronaVirusDiseaseStatus()
        areas = await source.SearchGlobalCoronaVirusDisease()
        try:
            for index in areas:
                if index['id'] == location.lower():
                    jsonData = {
                        index['id']: {
                            "country": index['country'],
                            "totalDeaths": index['totalDeaths'],
                            "totalRecovered": index['totalRecovered'],
                            "lastUpdated": index['lastUpdated']
                        }
                    }
                    data = jsonData
                    _data = await loop.run_in_threadpool(lambda: ujson.dumps(data, ensure_ascii=False, escape_forward_slashes=False, sort_keys=True).encode('utf-8'))
                    await cache.set(location, _data, expire=3600)
                    return data
        except Exception as x:
            raise HTTPException(status_code=422, detail=f"Validation Error :{str(x)}")
    else:
        try:
            data_ = await cache.get(location)
            _data = await loop.run_in_threadpool(lambda: ujson.loads(data_))
            return _data
        except Exception as e:
            return HTTPException(status_code=422, detail=f"Validation Error :{str(x)}")
