from fastapi import APIRouter
from .crawler.mohw import ConfirmationPatient
from .crawler.mohw import ConfirmationPatientIsolation
from .crawler.mohw import Dead
from .crawler.mohw import Inspection
covid = APIRouter()

@covid.get("/info", tags=['info'])
async def covidInfo():
    a = await ConfirmationPatient()
    b = await ConfirmationPatientIsolation()
    c = await Dead()
    d = await Inspection()
    
    return {
        "ConfirmationPatient": a,
        "ConfirmationPatientIsolation": b,
        "Dead": c,
        "Inspection": d
    }


