import requests


def weather_data(city):
    city = city
    URL = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=af88e26010932bab33aa15ec76b9bf2e"
    re = requests.get(URL)
    weather_data = re.json()
    temp = round(weather_data["main"]["temp"]-273, 2)
    weather = weather_data["weather"][0]["main"]
    return {"temp": temp, "weather": weather}

# print(a) - > {'temp': 30.62, 'weather': 'Clouds'}
# city_list = ["seoul", "Gyeonggi-do", "Incheon", "Gangwon-do",
#              "Chungcheongbuk-do", "Chungcheongnam-do", "Jeollabuk-do", "Jeollanam-do", "Gyeongsangbuk-do", "Gyeongsangnam-do", "Busan", "Jeju"]
