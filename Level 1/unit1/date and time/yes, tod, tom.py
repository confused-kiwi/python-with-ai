import datetime
display = """
-------------------------------
Please select delivery option:
f for Regular 4 days (Free)
t for Express 2 days ($9.99)
-------------------------------
"""
print(display)
days = input("")
now = datetime.datetime.now()
return_window = datetime.timedelta(days=30)

delivery_time = datetime.timedelta(days=2)
if days == "f":
    delivery_time = datetime.timedelta(days=4)

returning_time = now + return_window

estimated_arrival = now + delivery_time

print(f"Your order has been placed at {now.strftime('%b %d,%Y %I:%M%p')}")
print(f"Estimated delivery date is {estimated_arrival.strftime('%b %d,%Y')}")
print(f"The retun windows is by {returning_time.strftime('%b %d,%Y')}")