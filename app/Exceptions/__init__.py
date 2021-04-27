from typing import Dict
from app.Models import BaseExceptionToJsonModel


class ReturnErrorMSG:
    """
    example:
        {
            "status": bool,
            "system": {
                "code": int,
                "message": str
            },
            "data": None,
        }
    """
    def __init__(self, status: bool, code: int, message: str) -> None:
        self.status: bool = status
        self.http_status_code: int = code
        self.message: str = message

    def __dict__(self):
        return {
            "status": self.status,
            "system": {
                "code": self.http_status_code,
                "message": self.message
            },
            "data": None,
        }
