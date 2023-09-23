import datetime
now = datetime.datetime.now()
print("Formatting the date and time right now!")
print(now)
print(now.strftime("%a, %B %d, %Y"))
print(now.strftime("%a, %b %d, %Y"))
print(now.strftime("%a, %b %d"))
print(now.strftime("%m/%d/%y"))