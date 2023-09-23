import datetime
now = datetime.datetime.now()
birthday = datetime.datetime(now.year, 11, 3)
if birthday < now:
    birthday = datetime.datetime(now.year + 1, 11, 3)

td = birthday - now
print(td)