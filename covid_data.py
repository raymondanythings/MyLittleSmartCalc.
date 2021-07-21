import json
import requests
import xmltodict
import datetime


def covid_data(city):
    today_data = datetime.datetime.now()
    year = today_data.year
    if int(today_data.month) < 10:
        month = f"0{today_data.month}"
    else:
        month = today_data.month
    if int(today_data.day) < 10:
        day = f"0{today_data.day}"
    else:
        day = today_data.day
    start_today = f"{year}{month}{day-1}"
    end_today = f"{year}{month}{day}"
    API_KEY = "JH6zbvkA5BVV28%2F1gV5kf8ekn%2BcrdLd%2FKemfsr7Gou3Xvfb5R7hFDhQqz1gzamqB0il%2BA4f%2BIKcXSnbPPX4v%2Bw%3D%3D"
    URL = f"http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19SidoInfStateJson?serviceKey={API_KEY}&pageNo=1&numOfRows=10&startCreateDt={start_today}&endCreateDt={end_today}"
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
