from typing import Union
from pydantic import BaseModel
from .kdca import KDCAResponseModel as KDCARM
from .kdca import DATAModel
from .kdca import KDCASelectResponseModel


class system(BaseModel):
    code: int
    message: str


class KRResponseModel(BaseModel):
    status: bool
    system: system
    source: Union[list[KDCARM], None]


class RegionListModel(BaseModel):
    status: bool
    system: system
    source: Union[list[str], None]


class KRTotalModel(BaseModel):
    status: bool
    system: system
    source: Union[DATAModel, None]


class KRSelectResponseModel(BaseModel):
    status: bool
    system: system
    source: Union[KDCASelectResponseModel, None]
