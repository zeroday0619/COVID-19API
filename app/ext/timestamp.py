import datetime as pydatetime


def get_now():
    """현재 시스템 시간을 datetime 형으로 반환"""
    return pydatetime.datetime.now()


def get_now_timestamp() -> float:
    """현재 시스템 시간을 POSIX timestamp float 형으로 반환"""
    return get_now().timestamp()
