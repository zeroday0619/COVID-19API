# COVID-19API
코로나바이러스감염증-19(COVID-19)의 발생 동향 조회 API
======================================================
![pythonVersion](https://img.shields.io/badge/python-v3.8-blue) ![License](https://img.shields.io/badge/License-MIT-blue)

## DESCRIPTION
**COVID-19API는 대한민국 질병관리본부가 공개한 자료를 사용합니다.**


## Usage
```
pip3 install -r requirements.txt
```
```
sudo uvicorn run:app --host 0.0.0.0 --port 80
```

## API documentation

-> http://ncov.zeroday0619.kr/docs

-> http://ncov.zeroday0619.kr/redoc

## Extreme optimization
    - Use FastAPI framework
    - Cache: Redis
    - asynchronous
![TTFB 15.66ms](/src/img/TTFB.png)