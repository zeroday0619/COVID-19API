import ujson
from app.crawler.mohw import GetInfectiousDiseasesbyRegion

async def KrStatusRegion(cache, loop):
	if not await cache.exists('idr'):
		data = GetInfectiousDiseasesbyRegion()
		result = await data.AllRegion()
		jsondata = {
			"idr": result
		}
		ob = await loop.run_in_threadpool(lambda: ujson.dumps(jsondata).encode('utf-8'))
		#await cache.set('idr', ob, expire=3600)
		return jsondata
	else:
		abc = await cache.get('idr', encoding='utf-8')
		adad = await loop.run_in_threadpool(lambda: ujson.loads(abc))
		return adad