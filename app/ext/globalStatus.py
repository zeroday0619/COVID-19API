import ujson
from ..crawler.csse import CSSEApi

async def globalStatus(cache, loop):
	if not await cache.exists('global'):
		ads = CSSEApi()
		data = await ads.apiProcess()
		global_ = {
			"global": data
		}
		_global = await loop.run_in_threadpool(lambda: ujson.dumps(global_, ensure_ascii=False, escape_forward_slashes=False, sort_keys=True).encode('utf-8'))
		await cache.set('global', _global, expire=3600)
		return global_
	else:
		global_ = await cache.get('global')
		_global = await loop.run_in_threadpool(lambda: ujson.loads(global_))
		return _global