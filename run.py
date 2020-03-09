"""
:author: zeroday0619
:contact: zeroday0619(at)kakao.com
:copyright: Copyright 2020, zeroday0619
"""
from app.crawler.mohw import InfectiousDiseases
from app.crawler.mohw import GetInfectiousDiseasesbyRegion
from app.crawler.krnews import KrNewsParser
from app.ext.Performance import Performance
from datetime import datetime, timedelta
from fastapi import FastAPI
from pydantic import BaseModel
import fastapi
import typing
import ujson
import pydantic
import fastapi_plugins
import aioredis

__author__ = 'zeroday0619 <zeroday0619(at)kakao.com>'
__copyright__ = 'Copyright 2020, zeroday0619'

class OtherSettings(pydantic.BaseSettings):
    other: str = 'other'
class AppSettings(OtherSettings, fastapi_plugins.RedisSettings):
    api_name: str = str(__name__)

app = FastAPI()
config = AppSettings()



@app.get("/")
async def RootGet(cache: aioredis.Redis=fastapi.Depends(fastapi_plugins.depends_redis),) -> typing.Dict:
    return dict(ping=await cache.ping())

@app.get("/kr/status", tags=['/kr/status'])
async def covidInfo(cache: aioredis.Redis=fastapi.Depends(fastapi_plugins.depends_redis),) -> typing.Dict:
	"""# 국내 COVID-19 현황"""
	loop = Performance()
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

@app.get("/kr/status/region", tags=['/kr/status/region'])
async def covidIDR(cache: aioredis.Redis=fastapi.Depends(fastapi_plugins.depends_redis),) -> typing.Dict:
	"""# 지역 별 COVID-19 현황 조회"""
	loop = Performance()
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

@app.get("/kr/status/region/{location}", tags=['/kr/status/region/{location}'])
async def ClassificationCOVID19(location: str, cache: aioredis.Redis=fastapi.Depends(fastapi_plugins.depends_redis),) -> typing.Dict:
	"""# 시도별 COVID-19 선택 현황 조회
	## location
		- seoul		- chungbuk
		- busan		- chungnam
		- daegu		- jeonbuk
		- incheon	- jeonnam
		- gwangju	- gyeongbuk
		- daejeon	- gyeongnam
		- ulsan		- jeju
		- sejong	- gyeonggi
		- gangwon
	"""
	data = GetInfectiousDiseasesbyRegion()
	loop = Performance()
	if location == 'seoul':
		if not await cache.exists('seoul'):
			seoul = await data.Classification(regionNumber=0)
			_seoul = await loop.run_in_threadpool(lambda: ujson.dumps(seoul).encode('utf-8'))
			await cache.set('seoul', _seoul, expire=3600)
			return seoul
		else:
			seoul = await cache.get('seoul', encoding='utf-8')
			_seoul = await loop.run_in_threadpool(lambda: ujson.loads(seoul))
			return _seoul
	elif location == 'busan':
		if not await cache.exists('busan'):
			busan = await data.Classification(regionNumber=1)
			_busan = await loop.run_in_threadpool(lambda: ujson.dumps(busan).encode('utf-8'))
			await cache.set('busan', _busan, expire=3600)
			return busan
		else:
			busan = await cache.get('busan', encoding='utf-8')
			_busan = await loop.run_in_threadpool(lambda: ujson.loads(busan))
			return _seoul
	elif location == 'daegu':
		if not await cache.exists('daegu'):
			daegu = await data.Classification(regionNumber=2)
			_daegu = await loop.run_in_threadpool(lambda: ujson.dumps(daegu).encode('utf-8'))
			await cache.set('daegu', _daegu, expire=3600)
			return daegu
		else:
			daegu = await cache.get('daegu', encoding='utf-8')
			_daegu = await loop.run_in_threadpool(lambda: ujson.loads(daegu))
			return _daegu
	elif location == 'incheon':
		if not await cache.exists('incheon'):
			incheon = await data.Classification(regionNumber=3)
			_incheon = await loop.run_in_threadpool(lambda: ujson.dumps(incheon).encode('utf-8'))
			await cache.set('incheon', _incheon, expire=3600)
			return incheon
		else:
			incheon = await cache.get('incheon')
			_incheon = await loop.run_in_threadpool(lambda: ujson.loads(incheon))
			return _incheon
	elif location == 'gwangju':
		if not await cache.exists('gwangju'):
			gwangju = await data.Classification(regionNumber=4)
			_gwangju = await loop.run_in_threadpool(lambda: ujson.dumps(gwangju).encode('utf-8'))
			await cache.set('gwangju', _gwangju, expire=3600)
			return gwangju
		else:
			gwangju = await cache.get('gwangju')
			_gwangju = await loop.run_in_threadpool(lambda: ujson.loads(gwangju))
			return _gwangju
	elif location == 'daejeon':
		if not await cache.exists('daejeon'):
			daejeon = await data.Classification(regionNumber=5)
			_daejeon = await loop.run_in_threadpool(lambda: ujson.dumps(daejeon).encode('utf-8'))
			await cache.set('daejeon', _daejeon, expire=3600)
			return daejeon
		else:
			daejeon = await cache.get('daejeon')
			_daejeon = await loop.run_in_threadpool(lambda: ujson.loads(daejeon))
			return _daejeon
	elif location == 'ulsan':
		if not await cache.exists('ulsan'):
			ulsan = await data.Classification(regionNumber=6)
			_ulsan = await loop.run_in_threadpool(lambda: ujson.loads(ulsan).encode('utf-8'))
			await cache.set('ulsan', _ulsan, expire=3600)
			return ulsan
		else:
			ulsan = await cache.get('ulsan')
			_ulsan = await loop.run_in_threadpool(lambda: ujson.loads(ulsan))
			return _ulsan
	elif location == 'sejong':
		if not await cache.exists('sejong'):
			sejong = await data.Classification(regionNumber=7)
			_sejong = await loop.run_in_threadpool(lambda: ujson.dumps(sejong).encode('utf-8'))
			await cache.set('sejong', _sejong, expire=3600)
			return sejong
		else:
			sejong = await cache.get('sejong')
			_sejong = await loop.run_in_threadpool(lambda: ujson.loads(sejong))
			return _sejong
	elif location == 'gyeonggi':
		if not await cache.exists('gyeonggi'):
			gyeonggi = await data.Classification(regionNumber=8)
			_gwangju = await loop.run_in_threadpool(lambda: ujson.dumps(gyeonggi).encode('utf-8'))
			await cache.set('gyeonggi', _gwangju, expire=3600)
			return gyeonggi
		else:
			gyeonggi = await cache.get('gyeonggi')
			_gyeonggi = await loop.run_in_threadpool(lambda: ujson.loads(gyeonggi))
			return _gyeonggi
	elif location == 'gangwon':
		if not await cache.exists('gangwon'):
			gangwon = await data.Classification(regionNumber=9)
			_gangwon = await loop.run_in_threadpool(lambda: ujson.dumps(gangwon).encode('utf-8'))
			await cache.set('gangwon', _gangwon, expire=3600)
			return gangwon
		else:
			gangwon = await cache.get('gangwon')
			_gangwon = await loop.run_in_threadpool(lambda: ujson.loads(gangwon))
	elif location == 'chungbuk':
		if not await cache.exists('chungbuk'):
			chungbuk = await data.Classification(regionNumber=10)
			_chungbuk = await loop.run_in_threadpool(lambda: ujson.dumps(chungbuk).encode('utf-8'))
			await cache.set('chungbuk', _chungbuk, expire=3600)
			return chungbuk
		else:
			chungbuk = await cache.get('chungbuk')
			_chungbuk = await loop.run_in_threadpool(lambda: ujson.loads(chungbuk))
			return _chungbuk
	elif location == 'chungnam':
		if not await cache.exists('chungnam'):
			chungnam = await data.Classification(regionNumber=11)
			_chungnam = await loop.run_in_threadpool(lambda: ujson.dumps(chungnam).encode('utf-8'))
			await cache.set('chungnam', _chungnam, expire=3600)
			return chungnam
		else:
			chungnam = await cache.get('chungnam')
			_chungnam = await loop.run_in_threadpool(lambda: ujson.loads(chungnam))
			return _chungnam
	elif location == 'jeonbuk':
		if not await cache.exists('jeonbuk'):
			jeonbuk = await data.Classification(regionNumber=12)
			_jeonbuk = await loop.run_in_threadpool(lambda: ujson.dumps(jeonbuk).encode('utf-8'))
			await cache.set('jeonbuk', _jeonbuk, expire=3600)
			return jeonbuk
		else:
			jeonbuk = await cache.get('jeonbuk')
			_jeonbuk = await loop.run_in_threadpool(lambda: ujson.loads(jeonbuk))
			return _jeonbuk
	elif location == 'jeonnam':
		if not await cache.exists('jeonnam'):
			jeonnam = await data.Classification(regionNumber=13)
			_jeonnam = await loop.run_in_threadpool(lambda: ujson.dumps(jeonnam).encode('utf-8'))
			await cache.set('jeonnam', _jeonnam, expire=3600)
			return jeonnam
		else:
			jeonnam = await cache.get('jeonnam')
			_jeonnam = await loop.run_in_threadpool(lambda: ujson.loads(jeonnam))
			return _jeonnam
	elif location == 'gyeongbuk':
		if not await cache.exists('gyeongbuk'):
			gyeongbuk = await data.Classification(regionNumber=14)
			_gwangju = await loop.run_in_threadpool(lambda: ujson.dumps(gyeongbuk).encode('utf-8'))
			await cache.set('gyeongbuk', _gwangju, expire=3600)
			return gyeongbuk
		else:
			gyeongbuk = await cache.get('gyeongbuk')
			_gyeongbuk = await loop.run_in_threadpool(lambda: ujson.loads(gyeongbuk))
			return _gyeongbuk
	elif location == 'gyeongnam':
		if not await cache.exists('gyeongnam'):
			gyeongnam = await data.Classification(regionNumber=15)
			_gyeongnam = await loop.run_in_threadpool(lambda: ujson.dumps(gyeongnam).encode('utf-8'))
			await cache.set('gyeongnam', _gyeongnam, expire=3600)
			return gyeongnam
		else:
			gyeongnam = await cache.get('gyeongnam')
			_gyeongnam = await loop.run_in_threadpool(lambda: ujson.loads(gyeongnam))
			return _gyeongnam
	elif location == 'jeju':
		if not await cache.exists('jeju'):
			jeju = await data.Classification(regionNumber=16)
			_jeju = await loop.run_in_threadpool(lambda: ujson.dumps(jeju).encode('utf-8'))
			await cache.set('jeju', _jeju, expire=3600)
			return jeju
		else:
			jeju = await cache.get('jeju')
			_jeju = await loop.run_in_threadpool(lambda: ujson.loads(jeju))
			return _jeju
	else:
		return {"Error": "Error"}

@app.get("/kr/news", tags=["/kr/news"])
async def KrCoronaNews(cache: aioredis.Redis=fastapi.Depends(fastapi_plugins.depends_redis),) -> typing.Dict:
	"""국내 코로나 관련 뉴스를 제공합니다.
		10분 간격으로 news 정보 업데이트 됩니다.
	"""
	loop = Performance()
	if not await cache.exists('news'):
		data = KrNewsParser()
		d = await data.query()
		news = {
			"news": d
		}
		_news = await loop.run_in_threadpool(lambda: ujson.dumps(news, ensure_ascii=False, escape_forward_slashes=False).encode('utf-8'))
		await cache.set('news', _news, expire=600)
		return 
	else:
		news = await cache.get('news')
		_news = await loop.run_in_threadpool(lambda: ujson.loads(news))
		return _news

@app.on_event('startup')
async def on_startup() -> None:
    await fastapi_plugins.redis_plugin.init_app(app, config=config)
    await fastapi_plugins.redis_plugin.init()

@app.on_event('shutdown')
async def on_shutdown() -> None:
    await fastapi_plugins.redis_plugin.terminate()