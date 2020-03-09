from ..crawler.mohw import InfectiousDiseases
import ujson

async def krstatus(cache, loop):
	if not await cache.exists('info'):
		data = InfectiousDiseases()
		Result = await data.Convert()
		rs = {
			'info': Result
		}
		pb = await loop.run_in_threadpool(lambda: ujson.dumps(rs).encode('utf-8'))
		await cache.set('info', pb, expire=3600)
		return rs
	else:
		abc = await cache.get('info', encoding='utf-8')
		adad = await loop.run_in_threadpool(lambda: ujson.loads(abc))
		return adad