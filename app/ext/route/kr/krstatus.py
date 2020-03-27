from app.crawler.kr.mohw import InfectiousDiseases
import ujson


async def krstatus(cache, loop):
    if not await cache.exists('krstatus'):
        data = InfectiousDiseases(mode=11)
        Result = await data.Convert()
        rs = {
            'krstatus': Result
        }
        pb = await loop.run_in_threadpool(lambda: ujson.dumps(rs).encode('utf-8'))
        await cache.set('krstatus', pb, expire=3600)
        return rs
    else:
        abc = await cache.get('krstatus', encoding='utf-8')
        adad = await loop.run_in_threadpool(lambda: ujson.loads(abc))
        return adad


async def InspectionDetail(cache, loop):
    """InspectionDetail
	검사현황 - Detail
	"""
    if not await cache.exists('inspectionDetail'):
        data = InfectiousDiseases()
        Result = await data.InspectionStatusDetail()
        isd = {
            "inspectionDetail": Result
        }
        pb = await loop.run_in_threadpool(lambda: ujson.dumps(isd).encode('utf-8'))
        await cache.set('inspectionDetail', pb, expire=3600)
        return isd
    else:
        abc = await cache.get('inspectionDetail', encoding='utf-8')
        txt = await loop.run_in_threadpool(lambda: ujson.loads(abc))
        return txt
