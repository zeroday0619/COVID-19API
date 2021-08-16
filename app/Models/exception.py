from pydantic import BaseModel

"""
ERROR 발생시 다음 json 형식으로 반환
{
    "status": self.status,
    "system": {
        "code": self.http_status_code,
        "message": self.message
    },
    "data": None,
}
"""


class SystemModel(BaseModel):
    code: int
    message: str


class BaseExceptionToJsonModel(BaseModel):
    status: bool
    system: SystemModel
    source: None
    timestemp: float


__all__ = ['BaseExceptionToJsonModel']
