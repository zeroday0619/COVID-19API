# COVID-19API

### 코로나 바이러스 감염증-19(COVID-19, SARS-CoV-2)의 국내/외 발생 동향 조회 API
### Corona Virus Infectious Disease-19 (COVID-19, SARS-CoV-2) outbreak trend inquiry API

 ![License](https://img.shields.io/badge/License-MIT-blue)![pythonVersion](https://img.shields.io/badge/python-v3.8-blue)

---

COVID-19API는 대한민국 질병관리본부가 공개한 자료를 사용하며 해외 정보는 Coronavirus COVID-19 (CSSE) at Johns Hopkins University (JHU)를 사용합니다.

COVID-19API uses data published by the Korea Centers for Disease Control and Prevention, and Coronavirus COVID-19 (CSSE) at Johns Hopkins University (JHU) for overseas information.

    + NAVER NEWS, KCDC, ECDC, Johns Hopkins University(CSSE) 

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

  - [https://ncov.zeroday0619.dev/docs](https://ncov.zeroday0619.dev/docs)
  - [https://ncov.zeroday0619.dev/redoc](https://ncov.zeroday0619.dev/redoc)

### - Example

```python
import requests
import json
url = "https://ncov.zeroday0619.dev/v1/kr/status"
resp = requests.get(url).json()
result = resp['krstatus']
print(result)
```


## License
--> [**MIT License**](https://github.com/zeroday0619/COVID-19API/blob/master/LICENSE)
**Copyright (c) 2020 zeroday0619/Euiseo Cha**
- zeroday0619@kakao.com
- EuiseoCha@zeroday0619.dev
