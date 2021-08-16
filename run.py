"""
:author: zeroday0619
:contact: zeroday0619(at)kakao.com
:copyright: Copyright 2020, zeroday0619
"""
__version__ = "Ver 3.1"

import uvicorn

from fastapi import FastAPI
from fastapi.responses import UJSONResponse
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request
from app.Exceptions import APIException
from fastapi.exceptions import ValidationError

from app.Util.converter import convertStruct
from apis import root


app = FastAPI(
    title="COVID-19 API",
    description="## 코로나바이러스감염증-19 (COVID-19) API \n\n ### Project Repo: [Github]("
                "https://github.com/zeroday0619/COVID-19API)",
    version=__version__,
    debug=False
)


@app.exception_handler(APIException)
async def unicorn_exception_handler(request: Request, exc: APIException):
    return UJSONResponse(
        status_code=exc.system.get("code"),
        content=await convertStruct(
            source=exc.source,
            status=exc.status,
            message=exc.system.get("message"),
            code=exc.system.get("code")
        )
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
