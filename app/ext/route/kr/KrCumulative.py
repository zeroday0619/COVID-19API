import ujson
from app.crawler.kr.newMohw import Paser


async def KrCumulativeInspection(loop, cache):
    one = Paser()
    if not await cache.exists('kci'):
        d = await one.CumulativeInspection()
        kci = {
            "kci": d
        }
        _kci = await loop.run_in_threadpool(lambda: ujson.dumps(kci, ensure_ascii=False).encode('utf-8'))
        await cache.set('kci', _kci, expire=1800)
        return kci["kci"]
    else:
        kci = await cache.get('kci')
        _kci = await loop.run_in_threadpool(lambda: ujson.loads(kci))
        return _kci["kci"]
