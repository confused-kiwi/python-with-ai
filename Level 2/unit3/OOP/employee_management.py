class Employee:
    def __init__(self, name, hiredDate,department,employeeID):
        self.name = name
        self.hiredDate = hiredDate
        self.department = department
        self.employeeID = employeeID
    
    def print(self):
        print(f"{self.name} {self.employeeID} {self.hiredDate} {self.department}")


kirk = Employee("James Kirk",2018,"Finance",2265)
spock = Employee("Spock",2017,"Marketing",2254)
mccoy = Employee("Leonard McCoy",2016,"HR",2266)
sophia = Employee("Sophia Baker",2015,"IT",2159)

employees = []
employees.append(kirk)
employees.append(spock)
employees.append(mccoy)
employees.append(sophia)


keyword = ""
while keyword !="Q":
    keyword = input("Search for employee. Enter Q to exit ")
    for employee in employees:
        if keyword in employee.name :
            employee.print()
            break

print("Thanks for using Employee Management Application!")
