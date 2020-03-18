from scrapy.selector import Selector
import requests
import re
import ujson

def cleanText(text):
    # cleanT = await loop.run_in_executor(None, re.sub, "<.+?>", "", str(text), 0, re.I|re.S)
    cleanT = re.sub("<.+?>", "", str(text), 0, re.I | re.S)
    return cleanT

def chunker(seq, size=3):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))





def res():
    headers = {"user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:74.0) Gecko/20100101 Firefox/74.0"}
    url = "https://www.ecdc.europa.eu/en/cases-2019-ncov-eueea"
    data = requests.get(url, headers).text
    soup = Selector(text=data)
    db = soup.xpath('/html/body/div/div/div[1]/main/section[2]/div/div/div/div[2]/div/section/div/div[3]/div[2]/div/table/tbody/tr/td').getall()
    ListA = []
    ListB = []
    for i in db:
        ListA.append(cleanText(i))

    return ListA
print(res()[0])
