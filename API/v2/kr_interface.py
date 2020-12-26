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


class KCDAResponseA(BaseModel):
    response: list[KCDAModel]
    timestamp: float
