import ujson
import aiohttp

from app.Exceptions import APIException
from datetime import date as dt, timedelta


class ECDC:
    def __init__(self) -> None:
        self.url = "https://opendata.ecdc.europa.eu/covid19/nationalcasedeath_eueea_daily_ei/json/"
    
    async def fetch_json_data(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(self.url) as resp:
                if resp.status == 200:
                    return await resp.json()
                else:
                    raise APIException(
                        status=False,
                        system={
                            "code": resp.status,
                            "message": "ECDC API error"
                        }
                    )
    
    async def last_records(self):
        """ECDC API returns a list of records, so we need to get the last one"""
        yesterday = dt.today() - timedelta(1)
        
        # date (str): date in format DD/MM/YYYYs
        date = yesterday.strftime('%d/%m/%Y') 
        data = await self.fetch_json_data()
        records = data["records"]
        last_records = []
        _last_records = last_records.append
        
        for record in records:
            if record["dateRep"] == date:
                _last_records({
                    "country": record["countriesAndTerritories"],
                    "data": {
                        "date": record["dateRep"],
                        "cases": record["cases"],
                        "deaths": record["deaths"]
                    }
                })
            else:
                del record
        return last_records