import ujson
from fastapi import HTTPException
    
async def loc(location, data, loop, cache):
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
		raise HTTPException(status=404, detail="Location not found")
		