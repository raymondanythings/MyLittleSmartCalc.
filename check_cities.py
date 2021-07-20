
def check_cities(city):
    city_list = [{"서울": "seoul", "경기": "Gyeonggi-do", "인천": "Incheon", "강원": "Gangwon-do"}, {
        "충북": "Chungcheongbuk-do", "충남": "Chungcheongnam-do", "전북": "Jeollabuk-do", "전남": "Jeollanam-do"}, {"경북": "Gyeongsangbuk-do", "경남": "Gyeongsangnam-do", "부산": "Busan", "제주": "Jeju"}]

    name = ""
    for find in city_list:
        if city in find:
            name = find[city]
    return name
