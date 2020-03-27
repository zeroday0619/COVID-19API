import ujson
from fastapi import HTTPException

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


async def euroSelect(loop, cache, db, name: str, num: int):
    if not await cache.exists(name):
        data = await db.EuroCovid()
        euro_ = {
            name: data['result'][num]
        }
        _euro = await loop.run_in_threadpool(lambda: ujson.dumps(euro_, ensure_ascii=False, escape_forward_slashes=False, sort_keys=False).encode('utf-8'))
        await cache.set(name, _euro, expire=3600)
        return euro_
    else:
        euro_ = await cache.get(name)
        _euro = await loop.run_in_threadpool(lambda: ujson.loads(euro_))
        return _euro


async def euroSelectStatus(loop, cache, db, select):
    if select.lower() == "it":
        source = await euroSelect(loop=loop, cache=cache, db=db, name="region1", num=0)
        return source
    elif select.lower() == "es":
        source = await euroSelect(loop=loop, cache=cache, db=db, name="region2", num=1)
        return source
    elif select.lower() == "fr":
        source = await euroSelect(loop=loop, cache=cache, db=db, name="region3", num=2)
        return source
    elif select.lower() == "de":
        source = await euroSelect(loop=loop, cache=cache, db=db, name="region4", num=3)
        return source
    elif select.lower() == "gb":
        source = await euroSelect(loop=loop, cache=cache, db=db, name="region5", num=4)
        return source
    elif select.lower() == "nl":
        source = await euroSelect(loop=loop, cache=cache, db=db, name="region6", num=5)
        return source
    elif select.lower() == "at":
        source = await euroSelect(loop=loop, cache=cache, db=db, name="region7", num=6)
        return source
    elif select.lower() == "no":
        source = await euroSelect(loop=loop, cache=cache, db=db, name="region8", num=7)
        return source
    elif select.lower() == "be":
        source = await euroSelect(loop=loop, cache=cache, db=db, name="region9", num=8)
        return source
    elif select.lower() == "se":
        source = await euroSelect(loop=loop, cache=cache, db=db, name="region10", num=9)
        return source
    elif select.lower() == "dk":
        source = await euroSelect(loop=loop, cache=cache, db=db, name="region11", num=10)
        return source
    elif select.lower() == "pt":
        source = await euroSelect(loop=loop, cache=cache, db=db, name="region12", num=11)
        return source
    elif select.lower() == "cz":
        source = await euroSelect(loop=loop, cache=cache, db=db, name="region13", num=12)
        return source
    elif select.lower() == "gr":
        source = await euroSelect(loop=loop, cache=cache, db=db, name="region14", num=13)
        return source
    elif select.lower() == "fi":
        source = await euroSelect(loop=loop, cache=cache, db=db, name="region15", num=14)
        return source
    elif select.lower() == "ie":
        source = await euroSelect(loop=loop, cache=cache, db=db, name="region16", num=15)
        return source
    elif select.lower() == "si":
        source = await euroSelect(loop=loop, cache=cache, db=db, name="region17", num=16)
        return source
    elif select.lower() == "is":
        source = await euroSelect(loop=loop, cache=cache, db=db, name="region18", num=17)
        return source
    elif select.lower() == "pl":
        source = await euroSelect(loop=loop, cache=cache, db=db, name="region19", num=18)
        return source
    elif select.lower() == "ee":
        source = await euroSelect(loop=loop, cache=cache, db=db, name="region20", num=19)
        return source
    elif select.lower() == "ro":
        source = await euroSelect(loop=loop, cache=cache, db=db, name="region21", num=20)
        return source
    elif select.lower() == "lu":
        source = await euroSelect(loop=loop, cache=cache, db=db, name="region22", num=21)
        return source
    elif select.lower() == "sk":
        source = await euroSelect(loop=loop, cache=cache, db=db, name="region23", num=22)
        return source
    elif select.lower() == "bg":
        source = await euroSelect(loop=loop, cache=cache, db=db, name="region24", num=23)
        return source
    elif select.lower() == "hr":
        source = await euroSelect(loop=loop, cache=cache, db=db, name="region25", num=24)
        return source
    elif select.lower() == "lv":
        source = await euroSelect(loop=loop, cache=cache, db=db, name="region26", num=25)
        return source
    elif select.lower() == "hu":
        source = await euroSelect(loop=loop, cache=cache, db=db, name="region27", num=26)
        return source
    elif select.lower() == "cy":
        source = await euroSelect(loop=loop, cache=cache, db=db, name="region28", num=27)
        return source
    elif select.lower() == "mt":
        source = await euroSelect(loop=loop, cache=cache, db=db, name="region29", num=28)
        return source
    elif select.lower() == "lt":
        source = await euroSelect(loop=loop, cache=cache, db=db, name="region30", num=29)
        return source
    elif select.lower() == "li":
        source = await euroSelect(loop=loop, cache=cache, db=db, name="region31", num=30)
        return source
    else:
        raise HTTPException(status_code=404, detail="select not found")