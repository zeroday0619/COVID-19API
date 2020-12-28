from pydantic import BaseModel


class DATAModel(BaseModel):
    daily_change: int
    confirmed_cases: int
    isolated: int
    recovered: int
    deceased: int
    incidence: float


class KCDAModel(BaseModel):
    region: str
    data: list[DATAModel]


class KDCAResponse(BaseModel):
    response: list[KCDAModel]
    timestamp: float


class RegionList(BaseModel):
    regionList: list[str]


class KDCAResponseX(BaseModel):
    response: RegionList
    timestamp: float
