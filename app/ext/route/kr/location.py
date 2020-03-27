import ujson
from fastapi import HTTPException


async def LocationSelector(cache, loop, name, regionNumber, data):
    if not await cache.exists(name):
        seoul = await data.Classification(regionNumber)
        _seoul = await loop.run_in_threadpool(lambda: ujson.dumps(seoul).encode('utf-8'))
        await cache.set(name, _seoul, expire=3600)
        return seoul[name.upper()]
    else:
        seoul = await cache.get(name, encoding='utf-8')
        _seoul = await loop.run_in_threadpool(lambda: ujson.loads(seoul))
        return _seoul[name.upper()]


async def loc(location, data, loop, cache):
    if location == 'seoul':
        source = await LocationSelector(cache=cache, loop=loop, name=location, regionNumber=0, data=data)
        return source

    elif location == 'busan':
        source = await LocationSelector(cache=cache, loop=loop, name=location, regionNumber=1, data=data)
        return source

    elif location == 'daegu':
        source = await LocationSelector(cache=cache, loop=loop, name=location, regionNumber=2, data=data)
        return source

    elif location == 'incheon':
        source = await LocationSelector(cache=cache, loop=loop, name=location, regionNumber=3, data=data)
        return source

    elif location == 'gwangju':
        source = await LocationSelector(cache=cache, loop=loop, name=location, regionNumber=4, data=data)
        return source

    elif location == 'daejeon':
        source = await LocationSelector(cache=cache, loop=loop, name=location, regionNumber=5, data=data)
        return source

    elif location == 'ulsan':
        source = await LocationSelector(cache=cache, loop=loop, name=location, regionNumber=6, data=data)
        return source

    elif location == 'sejong':
        source = await LocationSelector(cache=cache, loop=loop, name=location, regionNumber=7, data=data)
        return source

    elif location == 'gyeonggi':
        source = await LocationSelector(cache=cache, loop=loop, name=location, regionNumber=8, data=data)
        return source

    elif location == 'gangwon':
        source = await LocationSelector(cache=cache, loop=loop, name=location, regionNumber=9, data=data)
        return source

    elif location == 'chungbuk':
        source = await LocationSelector(cache=cache, loop=loop, name=location, regionNumber=10, data=data)
        return source

    elif location == 'chungnam':
        source = await LocationSelector(cache=cache, loop=loop, name=location, regionNumber=11, data=data)
        return source

    elif location == 'jeonbuk':
        source = await LocationSelector(cache=cache, loop=loop, name=location, regionNumber=12, data=data)
        return source

    elif location == 'jeonnam':
        source = await LocationSelector(cache=cache, loop=loop, name=location, regionNumber=13, data=data)
        return source

    elif location == 'gyeongbuk':
        source = await LocationSelector(cache=cache, loop=loop, name=location, regionNumber=14, data=data)
        return source

    elif location == 'gyeongnam':
        source = await LocationSelector(cache=cache, loop=loop, name=location, regionNumber=15, data=data)
        return source

    elif location == 'jeju':
        source = await LocationSelector(cache=cache, loop=loop, name=location, regionNumber=16, data=data)
        return source
    else:
        raise HTTPException(status_code=404, detail="Location not found")
