class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    def printcontact(self):
        print(f"{self.name} {self.email} ")
    
    
    def selfintroduction(self):
        print(f"Hi, my name is {self.name}")


class Student(Person):
    pass


class Teacher(Person):
    pass


person = Person("Peter","peter@anywhere.com")
student = Student("Simon","simon@myschool.com")
teacher = Teacher("Tara","tara@myschool.com")

person.printcontact()
student.printcontact()
teacher.printcontact()

print("person.selfintroduction() \n")
person.selfintroduction()

print("student.selfintroduction() \n")
student.selfintroduction()

print("teacher.selfintroduction() \n")
teacher.selfintroduction()