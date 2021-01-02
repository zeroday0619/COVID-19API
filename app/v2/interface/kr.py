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
