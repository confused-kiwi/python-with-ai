import json
file = "customers.json"
f = open(file,"r")
text = f.read()
customers = json.loads(text)
f.close()
customer = {
    "name": "Ken",
    "age": 32,
    "married": True,
    "children": ["Cindy","Paul"],
    "pets": None,
    "cars": [
        {"model": "Honda Civic", "mpg": 21.5}
    ]
}


customers.append(customer)
f = open(file,"w")
f.write(json.dumps(customers, indent=2))
f.close()