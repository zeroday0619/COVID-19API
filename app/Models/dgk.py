from pydantic import BaseModel


class VAC_DATA(BaseModel):
    base_date: str
    first_cnt: int
    second_cnt: int
    total_first_cnt: int
    total_second_cnt: int
    accumulated_first_cnt: int
    accumulated_second_cnt: int


class VAC_ROOT_DATA(BaseModel):
    """
    source = {
        "region": json_data.sido,
        "data": {
            "base_date": json_data.baseDate,
            "first_cnt": json_data.firstCnt,
            "second_cnt": json_data.secondCnt,
            "total_first_cnt": json_data.totalFirstCnt,
            "total_second_cnt": json_data.totalSecondCnt,
            "accumulated_first_cnt": json_data.accumulatedFirstCnt,
            "accumulated_second_cnt": json_data.accumulatedSecondCnt
        }
    }
    """
    region: str
    data: VAC_DATA