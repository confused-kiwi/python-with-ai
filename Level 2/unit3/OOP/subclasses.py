class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    def intro(self):
        return f"I'm {self.name}."


class Student(Person):
    def __init__(self, name, email, classroom):
        super().__init__(name, email)
        self.classroom = classroom
    def student_class(self):
        return f"My class is {self.classroom}. My name is {self.name}"


student = Student("Billy Bobasaur", "xia.cheese@victorguo.com", "5BF")
print(student.student_class())