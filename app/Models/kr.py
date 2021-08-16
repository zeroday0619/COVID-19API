from typing import Union, List
from pydantic import BaseModel
from .kdca import KDCAResponseModel as KDCARM
from .kdca import DATAModel
from .kdca import KDCASelectResponseModel
from .dgk import VAC_ROOT_DATA

class system(BaseModel):
    code: int
    message: str


class KRResponseModel(BaseModel):
    status: bool
    system: system
    source: Union[list[KDCARM], None]
    timestemp: float


class RegionListModel(BaseModel):
    status: bool
    system: system
    source: Union[list[str], None]
    timestemp: float


class KRTotalModel(BaseModel):
    status: bool
    system: system
    source: Union[DATAModel, None]
    timestemp: float


class KRSelectResponseModel(BaseModel):
    status: bool
    system: system
    source: Union[KDCASelectResponseModel, None]
    timestemp: float

class KRVacModel(BaseModel):
    status: bool
    system: system
    source: Union[VAC_ROOT_DATA, None]
    timestemp: float
    
class KRVacRgsModel(BaseModel):
    status: bool
    system: system
    source: Union[List[VAC_ROOT_DATA], None]
    timestemp: float