# Inheritance
# A class that inherits props and methods from another

class  Person:
    def __init__(self, name, age, contry):
        self.name = name
        self.age = age
        self.contry = contry

    def say_hello(self):
        print(f'Hello, {self.name}!')

class Student(Person):
    def __init__(self, name, age, contry, course, grade):
        super().__init__(name, age, contry)
        self.course = course
        self.grade = grade

    def get_course(self):
        return self.course

    def get_grade(self):
        return self.grade
    
# instances
wesley = Student('Wesley', 25, 'Brazil', 'Computer Science', 5)
print(wesley.get_course())