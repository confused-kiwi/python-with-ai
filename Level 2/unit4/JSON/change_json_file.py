import json
file = "customers.json"
f = open(file,"r")
text = f.read()
customers = json.loads(text)
f.close()
for customer in customers:
    if customer["name"] == "John":
        customer["age"] = 31
        break

f = open(file,"w")
f.write(json.dumps(customers,indent=2))
f.close()

print("Customer data has been updated.")