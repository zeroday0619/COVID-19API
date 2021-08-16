from typing import Dict


class APIException(Exception):
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
    def __init__(self, status: bool, system: Dict[str, int], source: None):
        self.status = status
        self.system = system
        self.source = source
