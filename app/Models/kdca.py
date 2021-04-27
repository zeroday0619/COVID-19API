from pydantic import BaseModel


class KDCAModel(BaseModel):
    """KDCA HTML | Item"""
    region: list[str]
    daily_change: list[int]
    confirmed_cases: list[int]
    isolated: list[int]
    recovered: list[int]
    deceased: list[int]
    incidence: list[float]


class DATAModel(BaseModel):
    daily_change: int
    confirmed_cases: int
    isolated: int
    recovered: int
    deceased: int
    incidence: float


class KDCAResponseModel(BaseModel):
    region: str
    data: list[DATAModel]
