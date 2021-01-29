import datetime

date = "4/3"
time = "12:34"

(month, day) = date.split("/")
(hour, minute) = time.split(":")

date_str = datetime.datetime(2021, int(month), int(day), int(hour), int(minute))

print(date_str)
