class Person:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
    
    
    def describe(self):
        print("{} is a {} person.".format(self.name, self.gender))


luci = Person("Xia Luciana" "Female")
dad = Person("Xia Feng", "Male")
mom = Person("Wang Ping", "Female")

people = [luci, dad, mom]

print(f"There are three people, {luci.name}, {dad.name}, and {mom.name}.")

for person in people:
    person.describe()