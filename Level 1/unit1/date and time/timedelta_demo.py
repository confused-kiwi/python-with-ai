import datetime
import time

start = datetime.datetime(2023, 6, 20, 9, 20)
end = datetime.datetime(2023, 6, 21, 9, 30)
duration = end - start
# print(f"{duration.days} days and {duration.seconds} seconds ")

duration = datetime.timedelta(days=1) #  if added to a datetime variable, makes days go forward 1
now = datetime.datetime.now()

for looper in range(4):
    now += duration
    print(f"It is the day: {now.date()}")
    print("The duck waddles away, unaffected.\n")
    time.sleep(2.5)