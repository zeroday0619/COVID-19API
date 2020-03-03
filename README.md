# COVID-19API
코로나바이러스감염증-19(COVID-19)의 국내 발생 동향 조회 API


# Usage
```
pip3 install -r requirements.txt
```

```
uvicorn app.main:covid
```

## 국내 COVID-19 발생 현황
```http
HTTP GET /info
```

## 국내 시도별 발생 동향
```http
HTTP GET /idr
```