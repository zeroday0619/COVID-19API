from time import time
from app.Models import DefaultModel


async def convertStruct(source, status: bool, code: int, message: str) -> DefaultModel:
    """
    API Response 기본 구조 형성

    :param source: source 값
    :param status: 데이터처리 성공 여부 / 성공 -> True / 실패 -> False
    :param code: 기본적으로는 HTTP Status Code 또는 커스텀 에러 코드
    :param message: 데이터 처리에 대한 내용이나 에러 정보
    """
    frame = {
        "status": status,
        "system": {
            "code": code,
            "message": message
        },
        "source": source,
        "timestemp": time()
    }
    return frame


__all__ = ['convertStruct']
