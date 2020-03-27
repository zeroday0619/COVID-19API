"""
:author: zeroday0619
:contact: zeroday0619(at)kakao.com
:copyright: Copyright 2020, zeroday0619
"""
import pydantic
import logging
import fastapi_plugins
from fastapi import FastAPI
from API.v1 import router
__author__ = 'zeroday0619 <zeroday0619(at)kakao.com>'
__copyright__ = 'Copyright 2020, zeroday0619/Euiseo Cha'


class OtherSettings(pydantic.BaseSettings):
    other: str = 'other'


class AppSettings(OtherSettings, fastapi_plugins.RedisSettings):
    api_name: str = str(__name__)


app = FastAPI(
    title="COVID-19 API",
    description="## 코로나 바이러스 감염증 -19 (COVID-19)의 국내/해외 현황/뉴스 제공 API \n\n ### Project Repo: [Github]("
                "https://github.com/zeroday0619/COVID-19API)",
    version="2020.03.20 Prerelease V1409",
    debug=True
)
config = AppSettings()


@app.on_event('startup')
async def on_startup() -> None:
    await fastapi_plugins.redis_plugin.init_app(app, config=config)
    await fastapi_plugins.redis_plugin.init()


@app.on_event('shutdown')
async def on_shutdown() -> None:
    await fastapi_plugins.redis_plugin.terminate()

app.include_router(router, prefix="/v1", tags=["v1"])