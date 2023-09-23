import json

x='''
[
    {"model":"BMW 230","mpg":27.5},
    {"model":"Ford Edge","mpg": 24.1}
]
'''

cars = json.loads(x)
print("Cars")
print("---------------")
for car in cars:
    print(car["model"])