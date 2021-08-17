from typing import Any, Union, List
from pydantic import BaseModel
from .kr import system


class DATAModel(BaseModel):
    date: str
    cases: int
    deaths: int

class ROOT_MODEL(BaseModel):
    country: str
    data: DATAModel

class EuropaResponseModel(BaseModel):
    status: bool
    system: system
    source: Union[List[ROOT_MODEL], None]
    timestemp: float