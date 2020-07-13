import ujson
from app.crawler.kr.mohw import GetInfectiousDiseasesRegion


async def KrStatusRegion(cache, loop):
    if not await cache.exists('region'):
        data = GetInfectiousDiseasesRegion()
        result = await data.AllRegion()
        jsondata = {
            "region": result
        }
        ob = await loop.run_in_threadpool(lambda: ujson.dumps(jsondata).encode('utf-8'))
        await cache.set('region', ob, expire=3600)
        return jsondata["region"]
    else:
        abc = await cache.get('region', encoding='utf-8')
        adad = await loop.run_in_threadpool(lambda: ujson.loads(abc))
        return adad["region"]
