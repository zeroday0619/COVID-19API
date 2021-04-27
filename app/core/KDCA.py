import aiohttp
from pydantic import ValidationError
from ..Models.kdca import KDCAModel
from scrapy import Selector
from fastapi import HTTPException
from typing import Union


class KDCA:
    """Korea Disease Control and Prevention Agency"""
    params: dict[str, Union[int, str]]
    headers: dict[str, str]

    def __init__(self) -> None:
        self.ncov_url: str = "http://ncov.mohw.go.kr/en/bdBoardList.do"
        self.params = {"brdId": 16, "brdGubun": 162, "ncvContSeq": "", "contSeq": "", "board_id": "", "gubun": ""}
        self.headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.66"}

        # TODO: Variable naming should be consistently modified [1]
        # region
        self.region_css: str = 'th[scope=row]::text'
        # daily_change
        self.increasing_xpath: str = '//*[@id="content"]/div/div[5]/table/tbody/tr/td[1]/text()'
        # confirmed_cases
        self.cc_sum_xpath: str = '//*[@id="content"]/div/div[5]/table/tbody/tr/td[4]/text()'
        # isolated
        self.isolating_xpath: str = '//*[@id="content"]/div/div[5]/table/tbody/tr/td[5]/text()'
        # recovered
        self.recovered_xpath: str = '//*[@id="content"]/div/div[5]/table/tbody/tr/td[6]/text()'
        # deceased
        self.dead_xpath: str = '//*[@id="content"]/div/div[5]/table/tbody/tr/td[7]/text()'
        # incidence
        self.incidence_xpath: str = '//*[@id="content"]/div/div[5]/table/tbody/tr/td[8]/text()'

    async def get_html(self) -> str:
        async with aiohttp.ClientSession(headers=self.headers) as session:
            async with session.get(url=self.ncov_url, params=self.params) as resp:
                if resp.status != 200:
                    raise HTTPException(status_code=resp.status, detail="Processing Error")
                res: str = await resp.text()
        return res

    @staticmethod
    async def refactor(source: list) -> list:
        nx = []
        ap = nx.append
        for ix in source:
            x = ix.replace(',', '').replace('-', '0')
            ap(x)
        return nx

    @staticmethod
    async def re_pack(source, key) -> list:
        index = []
        _index = index.append
        for x in source[key]:
            js_d = {
                key: x
            }
            _index(js_d)
        return index

    @staticmethod
    async def delete(source: list) -> list:
        source.pop(0)
        source.pop(-1)
        return source

    async def parse_html(self) -> list:
        html = await self.get_html()
        source = Selector(text=html)

        region = source.css(self.region_css).getall()
        # TODO: Variable naming should be consistently modified [2]
        increasing = await self.refactor(source.xpath(self.increasing_xpath).getall())
        cc_sum = await self.refactor(source.xpath(self.cc_sum_xpath).getall())
        isolating = await self.refactor(source.xpath(self.isolating_xpath).getall())
        recovered = await self.refactor(source.xpath(self.recovered_xpath).getall())
        dead = await self.refactor(source.xpath(self.dead_xpath).getall())
        incidence = await self.refactor(source.xpath(self.incidence_xpath).getall())
        return [region, increasing, cc_sum, isolating, recovered, dead, incidence]

    async def get_total(self) -> dict:
        src = await self.parse_html()
        pack = {
            'daily_change': src[1][0],
            'confirmed_cases': src[2][0],
            'isolated': src[3][0],
            'recovered': src[4][0],
            'deceased': src[5][0],
            'incidence': src[6][0]
        }
        return pack

    async def find_only_region(self) -> dict:
        src = await self.parse_html()
        pack = {
            'region': await self.delete(src[0]),
            'daily_change': await self.delete(src[1]),
            'confirmed_cases': await self.delete(src[2]),
            'isolated': await self.delete(src[3]),
            'recovered': await self.delete(src[4]),
            'deceased': await self.delete(src[5]),
            'incidence': await self.delete(src[6])
        }
        try:
            re_typed = KDCAModel(**dict(pack))
            result = re_typed.dict()
        except ValidationError as ex:
            raise HTTPException(status_code=500, detail=ex)
        return result

    async def region_list(self) -> list:
        source = await self.find_only_region()
        region = await self.re_pack(source, "region")

        nx = []
        _nx = nx.append
        for i in region:
            _nx(i['region'])
        json_data = nx
        return json_data

    async def covid_data(self) -> list:
        source = await self.find_only_region()
        pack_1 = await self.re_pack(source, "region")
        pack_2 = await self.re_pack(source, "daily_change")
        pack_3 = await self.re_pack(source, "confirmed_cases")
        pack_4 = await self.re_pack(source, "isolated")
        pack_5 = await self.re_pack(source, "recovered")
        pack_6 = await self.re_pack(source, "deceased")
        pack_7 = await self.re_pack(source, "incidence")

        update = []
        _update = update.append

        for i in range(0, len(pack_1)):
            json_model = {
                'region': pack_1[i]['region'],
                "data": [
                    {**pack_2[i], **pack_3[i], **pack_4[i], **pack_5[i], **pack_6[i], **pack_7[i]}
                ],
            }
            _update(json_model)
        return update

    async def selectRegion(self, region) -> Union[dict, None]:
        source = await self.covid_data()
        for reg in source:
            if reg["region"] == region:
                return {
                    "region": reg["region"],
                    "data": reg["data"][0]
                }
        return None
