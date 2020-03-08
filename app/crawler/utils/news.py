import asyncio
import aiohttp

from bs4 import BeautifulSoup
from ...ext import Performance


class CoronaNewsCrawler:
    def __init__(self):
        self.loop = Performance()