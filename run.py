"""
:author: zeroday0619
:contact: zeroday0619(at)kakao.com
:copyright: Copyright 2020, zeroday0619
"""
__version__ = "2020.12.26 dev release"

import uvicorn
from fastapi import FastAPI
from API.v2 import v2_router

app = FastAPI(
    title="COVID-19 API",
    description="## 코로나 바이러스 감염증 -19 (COVID-19)의 국내/해외 현황/뉴스 제공 API \n\n ### Project Repo: [Github](https://github.com/zeroday0619/COVID-19API)",
    version=__version__,
    debug=False
)
app.include_router(router=v2_router, prefix="/v2", tags=["v2"])


if __name__ == "__main__":
    uvicorn.run(app)