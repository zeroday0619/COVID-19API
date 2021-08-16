from app.db import c_code
from app.Exceptions import APIException

class CountryCodeUtil(object):

    @staticmethod
    def get_all_country_name() -> list:
        data = c_code["data"]
        return [{cn["name"]: cn["alpha_3"]} for cn in data]

    @staticmethod
    def get_country_code(alpha_3):
        data = c_code["data"]
        for item in data:
            if item["alpha_3"].lower() == alpha_3.lower():
                return item["alpha_2"].lower()
        raise APIException(
            status=False,
            system={
                "code": 422,
                "message": "Country name not found"
            },
            source=None
        )