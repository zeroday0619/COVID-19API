from scrapy.selector import Selector
from app.ext.utils.Performance import Performance
from .utils import cleanText
from .utils.msnCovid import MsnCovid


class CoronaVirusDiseaseStatus:
    def __init__(self):
        self.loop = Performance()
        self.source = MsnCovid()