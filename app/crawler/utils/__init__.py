from .kcdcAPI import kcdcAPI
from .NaverAPI import NaverAPI
import re

def cleanText(text):
    cleanT = re.sub('<.+?>', '', str(text))
    return cleanT

KcdcApi = kcdcAPI
NaverApi = NaverAPI