import datetime as date
now = date.datetime.now()
print(now)
print(now.year)
print(now.microsecond) #  microsecond is an attribute
print(now.weekday())   #  weekday() is method/function. Monday is 0, Sunday is 6
print(now.strftime("%A, %B the %dth, %Y, "))
# a/A means weekday, b/B means month, d/D means date, y/Y means year


birthday = datetime.datetime(2012, 11, 3, 9, 45, 00, 00)
print(f"Luci's birthday is {birthday}.")

if birthday <= now:
    print("I'm young.")
else:
    print("I'm old.")


#  .date() and .time() are actually things. it shows the date/time independently.

#  .timedelta is the duration between two dates and times. you can measure the duration of something.