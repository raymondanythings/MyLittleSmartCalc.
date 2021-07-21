from tkinter import *
from weather_data import weather_data
from covid_data import covid_data
from check_cities import check_cities

# Entry
operator = ["/", "-", "+", "X", "*"]
target_num = ""
weather = "\N{sun behind cloud}"
back = "\U0001F519"

btns = ["C741.", f"{weather}8520", "P963?", "/-+X="]
city_list = [{"서울": "seoul", "경기": "Gyeonggi-do", "인천": "Incheon", "강원": "Gangwon-do"}, {
             "충북": "Chungcheongbuk-do", "충남": "Chungcheongnam-do", "전북": "Jeollabuk-do", "전남": "Jeollanam-do"}, {"경북": "Gyeongsangbuk-do", "경남": "Gyeongsangnam-do", "부산": "Busan", "제주": "Jeju"}]


def draw_calc_btns(weather, img, btns):
    bottom_frame = Frame(t, width=600, height=300)
    bottom_frame.pack()
    bottom_frame2 = Frame(t)
    bottom_frame2.pack(side="bottom")
    label = Label(
        bottom_frame2, text="copyright© 2021. Raymond All rights reserved")
    label.pack()
    for col, titles in enumerate(btns):
        for row, txt in enumerate(titles):
            if txt != "P":
                b1 = Button(bottom_frame, text=txt,
                            font=("Courier", 80), width=2, background="red", command=lambda cmd=txt: btn_click(cmd, bottom_frame, bottom_frame2))
                b1.grid(column=col, row=row, padx=5, pady=15)
            else:
                b1 = Button(bottom_frame, image=img, width=82, height=82,
                            command=lambda cmd=txt: btn_click(cmd, bottom_frame, bottom_frame2))
                b1.grid(column=col, row=row, padx=5, pady=15)


def draw_weather_btns(city_list, emo):
    bottom_frame = Frame(t, width=600, height=300)
    bottom_frame.pack()
    bottom_frame2 = Frame(t)
    bottom_frame2.pack()
    bottom_frame3 = Frame(t)
    bottom_frame3.pack(side="bottom")
    label = Label(
        bottom_frame3, text="copyright© 2021. Raymond All rights reserved")
    label.pack()
    for col, cities in enumerate(city_list):
        for row, city in enumerate(cities):
            b1 = Button(bottom_frame, text=city,
                        font=("Courier", 16), width=15, height=5, command=lambda city=city: weather_click(city, bottom_frame, bottom_frame2, bottom_frame3))
            b1.grid(column=col, row=row, padx=5, pady=15)
    re = Button(bottom_frame2, text=emo, width=30,
                height=4, font=("Courier", 25), command=lambda city=emo: weather_click(city, bottom_frame, bottom_frame2, bottom_frame3))
    re.grid(column=0, row=0)


def draw_covid_btns(city_list, emo):
    bottom_frame = Frame(t, width=600, height=300)
    bottom_frame.pack()
    bottom_frame2 = Frame(t)
    bottom_frame2.pack()
    bottom_frame3 = Frame(t)
    bottom_frame3.pack(side="bottom")
    label = Label(
        bottom_frame3, text="copyright© 2021. Raymond All rights reserved")
    label.pack()
    for col, cities in enumerate(city_list):
        for row, city in enumerate(cities):
            b1 = Button(bottom_frame, text=city,
                        font=("Courier", 16), width=15, height=5, command=lambda city=city: covid_click(city, bottom_frame, bottom_frame2, bottom_frame3))
            b1.grid(column=col, row=row, padx=5, pady=15)
    re = Button(bottom_frame2, text=emo, width=30,
                height=4, font=("Courier", 25), command=lambda city=emo: covid_click(city, bottom_frame, bottom_frame2, bottom_frame3))
    re.grid(column=0, row=0)


def btn_click(txt, bottom_frame, bottom_frame2):
    print(txt)
    global target_num
    if entry.get() == "0":
        entry.delete(0, "end")
    if txt == weather:
        bottom_frame.destroy()
        bottom_frame2.destroy()
        draw_weather_btns(city_list, back)
    elif txt == "P":
        bottom_frame.destroy()
        bottom_frame2.destroy()
        draw_covid_btns(city_list, back)
    elif txt in operator:
        if txt == "X":
            txt = "*"
        print(type(target_num))
        target_num += txt
    elif txt == "=":
        target_num = target_num.rstrip("+-*/")
        entry.delete(0, "end")
        result = str(eval(target_num))
        target_num = str(target_num)
        entry.insert(0, result)
    elif txt == "C":
        entry.delete(0, "end")
        entry.insert(0, "0")
        target_num = ""
    else:
        try:
            if target_num[-1] in operator:
                entry.delete(0, "end")
        except IndexError:
            pass
        try:
            if target_num[-1] in "=":
                entry.delete(0, "end")
        except IndexError:
            pass
        entry.insert("end", txt)
        target_num += txt
        print(f"{target_num} Now!")
        # print(entry.get()) - 프롬프트상의 숫자 가져오기


def weather_click(city, bottom_frame, bottom_frame2, bottom_frame3):
    global city_list
    entry.delete(0, "end")
    if city == back:
        bottom_frame.destroy()
        bottom_frame2.destroy()
        bottom_frame3.destroy()
        draw_calc_btns(weather, covid, btns)
    else:
        name = ""
        for find in city_list:
            if city in find:
                name = find[city]
        result = weather_data(name)
        prompt = f'{result["temp"]}℃, {result["weather"]} Now!'
        entry.insert(0, prompt)


def covid_click(city, bottom_frame, bottom_frame2, bottom_frame3):
    global city_list
    entry.delete(0, "end")
    if city == back:
        bottom_frame.destroy()
        bottom_frame2.destroy()
        bottom_frame3.destroy()
        draw_calc_btns(weather, covid, btns)
    else:
        cityEn = check_cities(city).capitalize()
        data = covid_data(cityEn)
        prompt = f"{city} 확진자 수: {data} Today"
        entry.insert(0, prompt)


t = Tk()
t.title("Webculator")
t.geometry('500x700+100+100')
t.resizable(width=False, height=False)

top_frame = Frame(t, width=470, height=70, relief="sunken", bd=8)
top_frame.pack(pady=20)


entry = Entry(top_frame, width=30, font=("Courier", 20),
              borderwidth=None, justify=RIGHT)
entry.pack()
entry.insert(0, "0")
covid = PhotoImage(file="image/covid.png")

draw_calc_btns(weather, covid, btns)


t.mainloop()
