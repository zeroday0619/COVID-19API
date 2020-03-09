from ..crawler.krnews import KrNewsParser
import ujson

async def KrNews(cache, loop):
	if not await cache.exists('news'):
		data = KrNewsParser()
		d = await data.query()
		news = {
			"news": d
		}
		_news = await loop.run_in_threadpool(lambda: ujson.dumps(news, ensure_ascii=False, escape_forward_slashes=False).encode('utf-8'))
		await cache.set('news', _news, expire=600)
		return news
	else:
		news = await cache.get('news')
		_news = await loop.run_in_threadpool(lambda: ujson.loads(news))
		return _news