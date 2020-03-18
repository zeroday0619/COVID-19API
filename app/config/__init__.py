"""
COVID-19 API
copyright (c) 2020 zeroday0619/EuiseoCha
"""
headers = {"user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:74.0) Gecko/20100101 Firefox/74.0"}

# csseApi.py Config
csseAPI_URL = "https://services1.arcgis.com/0MSEUqKaxRlEPj5g/arcgis/rest/services/ncov_cases/FeatureServer/2/query"
csseAPI_query_syn = {"f": "json", "where": "Confirmed>0", "outFields": "*", "orderByFields": "OBJECTID"}

# ecdcApi.py Config
ecdcAPI_URL = "https://www.ecdc.europa.eu/en/cases-2019-ncov-eueea"
ecdcAPI_ListA = []
ecdcAPI_ListB = []
ecdcAPI_xpath = '/html/body/div/div/div[1]/main/section[2]/div/div/div/div[2]/div/section/div/div[3]/div[2]/div/table/tbody/tr/td'

# kcdcAPI.py Config
kdckAPI_ncovURL = "http://ncov.mohw.go.kr/bdBoardList_Real.do"
kcdcAPI_homeURL = "http://ncov.mohw.go.kr/"

# Naver News Config
NaverNewsUrl = "https://search.naver.com/search.naver"
NaverConfig = {"where": "news", "query": '코로나19 "코로나19" -정치 ', "oquery": '코로나19 "코로나19"', "mynews": '0', "tqi": "UEfQtdp0YiRssPppOAossssstyG-455013"}