import ujson
from app.crawler.utils.ext.country import isoCountries
from app.crawler.world.csse import CSSEApi
from app.crawler.world.WorldStatus import CoronaVirusDiseaseStatus



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
        return global_["global"]
    else:
        global_ = await cache.get('global')
        _global = await loop.run_in_threadpool(lambda: ujson.loads(global_))
        return _global["global"]


async def GlobalCoronaStatus(cache, loop):
    if not await cache.exists('world'):
        source = CoronaVirusDiseaseStatus()
        data = await source.GlobalCoronaVirusDisease()
        gcs_ = {
            "world": data
        }
        _gcs = await loop.run_in_threadpool(lambda: ujson.dumps(gcs_, ensure_ascii=False, escape_forward_slashes=False, sort_keys=True).encode('utf-8'))
        await cache.set('world', _gcs, expire=3600)
        return gcs_["world"]
    else:
        gcs_ = await cache.get('world')
        _gcs = await loop.run_in_threadpool(lambda: ujson.loads(gcs_))
        return _gcs["world"]


async def CountryCodeConverter(source):
    for index in isoCountries:
        if index["ccode"].lower() == source.lower():
            return index["cname"].lower()


async def CountrySelect(country: str):
    data = CSSEApi()
    source = await data.apiProcess()
    for index in source:
        if index['country'].lower() == await CountryCodeConverter(source=country):
            return index


async def GlobalCoronaSearch(cache, loop, country):
    if not await cache.exists(country.lower()):
        data = await CountrySelect(country=country)
        jsonObject = {
            country.lower(): data
        }
        _result = await loop.run_in_threadpool(lambda: ujson.dumps(jsonObject, ensure_ascii=False, escape_forward_slashes=False, sort_keys=True).encode('utf-8'))
        await cache.set(country.lower(), _result, expire=3600)
        return jsonObject[country.lower()]
    else:
        result_ = await cache.get(country.lower())
        _result = await loop.run_in_threadpool(lambda: ujson.loads(result_))
        return _result[country.lower()]



