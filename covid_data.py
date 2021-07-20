import json
import requests
import xmltodict
import csv


def covid_data(city):
    URL = "http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19SidoInfStateJson?serviceKey=JH6zbvkA5BVV28%2F1gV5kf8ekn%2BcrdLd%2FKemfsr7Gou3Xvfb5R7hFDhQqz1gzamqB0il%2BA4f%2BIKcXSnbPPX4v%2Bw%3D%3D&pageNo=1&numOfRows=10"
    re = requests.get(URL)
    result = xmltodict.parse(re.text)
    dd = json.loads(json.dumps(result))
    covid_data = dd["response"]["body"]["items"]["item"]

    target = []
    for x in covid_data:
        if city == x["gubunEn"]:
            print("Found Target data")
            target.append(x)
            break
    return target[0]['incDec']

# 확진자 수 리턴 -> 전체데이터 리턴도 가능
