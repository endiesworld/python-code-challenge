#
from datetime import datetime,  timezone
timestamp = 25309472.357246
timestamp = datetime.fromtimestamp(timestamp, tz=timezone.utc)
timestamp_2 = datetime.now(tz=timezone.utc)
date_time = timestamp_2 - timestamp
print(date_time.days)
# date_time = datetime.fromtimestamp(date_time)
# str_date_time = date_time.strftime("%d-%m-%Y, %H:%M:%S")
# year = date_time.year
# month = date_time.month
# day = date_time.day
# hour = date_time.hour
# minute = date_time.minute
# second = date_time.second
# print("Current timestamp", str_date_time)
# print({'year': year, 'month': month, 'day': day,
#       'hour': hour, 'munite': minute, 'second': second})
