async def OneJson(jsondata):
    process = {
        "covid-19": jsondata,
        "notice": {
            "message": "Covid-19API는 질병관리본부와 네이버 뉴스 자료를 사용합니다.",
            "GithubRepo": "https://github.com/zeroday0619/COVID-19API",
            "Email": "zeroday0619@kakao.com",
            "License": "MIT License",
            "info" :"Copyright (C) zeroday0619 [Euiseo Cha, 차의서]. All rights reserved"
        }
    }
    return process