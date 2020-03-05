from .kcdcAPI import kcdcAPI
import re

def cleanText(text):
    cleanT = re.sub('<.+?>', '', str(text))
    return cleanT

KcdcApi = kcdcAPI