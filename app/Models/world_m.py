from typing import Any, Union, List
from pydantic import BaseModel
from .kr import system

class DATAModel(BaseModel):
    doses_admin: Any
    raw_full_vac: Any
    percent_full_vac: Any
    date: Any


class GlobalVaccines(BaseModel):
    country: str
    data: DATAModel


class GlobalVaccinesResponseModel(BaseModel):
    status: bool
    system: system
    source: Union[List[GlobalVaccines], None]
    timestemp: float

class _day(BaseModel):
    date: str
    value: int

class _week(BaseModel):
    date: str
    value: int

class _month(BaseModel):
    date: str
    value: int


class _confirmed_cases(BaseModel):
    all: int
    day: int
    week: int
    month: int

class _deaths(BaseModel):
    all: int
    day: int
    week: int
    month: int

class _confirmed_cases_dict(BaseModel):
    day: _day
    week: _week
    month: _month

class _deaths_dict(BaseModel):
    day: _day
    week: _week
    month: _month

class _records(BaseModel):
    confirmed_cases: _confirmed_cases_dict
    deaths: _deaths_dict

class ROOT_MODEL(BaseModel):
    confirmed_cases: _confirmed_cases
    deaths: _deaths
    records: _records

class DATA_A_MODEL(BaseModel):
    country: str
    data: ROOT_MODEL

class GlobalModel(BaseModel):
    status: bool
    system: system
    source: Union[DATA_A_MODEL, None]
    timestemp: float