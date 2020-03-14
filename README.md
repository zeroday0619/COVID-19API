# COVID-19API

### 코로나 바이러스 감염증-19(COVID-19, SARS-CoV-2)의 국내/외 발생 동향 조회 API

 ![License](https://img.shields.io/badge/License-MIT-blue)![pythonVersion](https://img.shields.io/badge/python-v3.8-blue)

---

COVID-19API는 대한민국 질병관리본부가 공개한 자료를 사용하며 해외 정보는 Coronavirus COVID-19 (CSSE) at Johns Hopkins University (JHU)를 사용합니다.

## Installation

- Ubuntu

```shell
sudo apt-get install redis-server
sudo systemctl enable redis-server.service
```

```shell
git clone https://github.com/zeroday0619/COVID-19API.git
cd COVID-19API
```

```shell
python3.8 -m pip install -r requirements.txt
sudo uvicorn run:app --host 0.0.0.0 --port 80
```

- Mac OS

```shell
brew install redis
brew services start redis
```

```shell
git clone https://github.com/zeroday0619/COVID-19API.git
cd COVID-19API
```

```shell
python3.8 -m pip install -r requirements.txt
sudo uvicorn run:app --host 0.0.0.0 --port 80
```

## Usage

### - API Documentation

- 국내 COVID-19 현황 조회 -  /kr/status

- 지역 별 COVID-19 현황 조회 - /kr/status/region

- 지역 별 COVID-19 선택 현황 조회 - /kr/status/region/{location}

- 국내 COVID-19 검사 현황 | 누적 확진률 조회 - /kr/status/inspection

- 국내 COVID-19 검사 현황 상세 조회 - /kr/status/inspection/detail

- 해외 COVID-19 감염, 완치, 사망 정보 조회 - /global/status

- 국내 COVID-19 관련 뉴스 제공 - /kr/news

  See [https://ncov.zeroday0619.kr/docs](https://ncov.zeroday0619.kr/docs)

### - Example

```python
import requests
import json
url = "https://ncov.zeroday0619.kr/kr/status"
resp = requests.get(url).json()
result = resp['krstatus']
print(result)
```

## Extreme optimization
    - Use FastAPI framework
    - Cache: Redis
    - asynchronous
![TTFB 15.66ms](/src/img/TTFB.png)

## License

--> [**MIT License**](https://github.com/zeroday0619/COVID-19API/blob/master/LICENSE)

**Copyright (c) 2020 zeroday0619/Euiseo Cha**
