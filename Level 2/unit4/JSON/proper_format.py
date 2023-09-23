import json
customer = {
    "name": "John",
    "age": 30,
    "married": True,
    "children": ["Ann","Billy"],
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}

customer_json = json.dumps(customer, indent=4, sort_keys=True)

f = open("customer_info.json", "a")
f.write(customer_json)
f.close()
print('done!')