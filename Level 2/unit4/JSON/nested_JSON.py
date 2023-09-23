import json
pyon = """ 
{
  "name" : "Lu",
  "age" : 2,
  "hobby" : "poo",
  "dance" : "do",
  "wife" : "Nu",
  "kids" : {
    "sons" : ["Alex", "Wilbur", "Tommy", "George", "Clay"],
    "daughters" : ["Lizzie", "Tiffany", "Katherine"]
  }
}
"""

person = json.loads(pyon)
print({person['kids']["sons"][3]})