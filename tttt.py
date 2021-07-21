import datetime
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

print(start_today)
print(end_today)
