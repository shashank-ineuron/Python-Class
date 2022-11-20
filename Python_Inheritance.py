# Inheritance in Python

# Base Class aka Parent Class
class Person():
    def __init__(self, name):
        self.name = name 

    def displayName(self):
        print(self.name) 

    # By default we can say that particular perosn is unemployed
    def isEmployed(self):
        print(self.name," is Un-Employed !!")

# Derived Class aka Child Class
class Employee(Person):

    def isEmployed(self):
        print(self.name," is Employed !!")


emp = Person('Shashank')
emp.displayName()
emp.isEmployed()

emp1 = Employee('Rahul')
emp1.displayName()
emp1.isEmployed()
