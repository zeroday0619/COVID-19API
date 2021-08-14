"""
:author: zeroday0619
:contact: zeroday0619(at)kakao.com
:copyright: Copyright 2020, zeroday0619
"""
__version__ = "Ver 3.1"

import uvicorn
from fastapi import FastAPI
from apis import root
from starlette.middleware.cors import CORSMiddleware


app = FastAPI(
    title="COVID-19 API",
    description="## 코로나바이러스감염증-19 (COVID-19) API \n\n ### Project Repo: [Github]("
                "https://github.com/zeroday0619/COVID-19API)",
    version=__version__,
    debug=False
)


if __name__ == "__main__":
    app.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(router=root, prefix="/api")
    uvicorn.run(app, host="127.0.0.1", port=8899)
