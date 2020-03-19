import ujson


async def euroStatus(loop, cache, db):
    if not await cache.exists('euro'):
        data = await db.EuroCovid()
        euro_ = {
            "euro": data
        }
        _euro = await loop.run_in_threadpool(lambda: ujson.dumps(euro_, ensure_ascii=False, escape_forward_slashes=False, sort_keys=False).encode('utf-8'))
        await cache.set('euro', _euro, expire=3600)
        return euro_
    else:
        euro_ = await cache.get('euro')
        _euro = await loop.run_in_threadpool(lambda: ujson.loads(euro_))
        return _euro