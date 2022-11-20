class Employee:

    # Class attribute
    empCount = 0

    # Constructor of class
    # it is mainly used for assignment of instance variables
    def __init__(self, name, salary ):
        # instance variable or instance attributes
        self.emp_name = name
        self.emp_salary = salary
        Employee.empCount += 1

    # method of a class
    def displayEmployeeInfo(self):
        print("Employee name : ",self.emp_name, " , Employee Salary : ",self.emp_salary)

        # method of a class
    def displayEmployeeCount(self):
        print("Employee Count : ",Employee.empCount)

emp1 = Employee('Shashank', 1000)
emp1.displayEmployeeInfo()
emp1.displayEmployeeCount()

emp2 = Employee('Rahul', 2000)
emp2.displayEmployeeInfo()
emp2.displayEmployeeCount()


emp1.displayEmployeeCount()
emp2.displayEmployeeCount()

# print instance variables of a object
print(emp1.emp_name)
print(emp1.emp_salary)
print(emp2.emp_name)
print(emp2.emp_salary)

# lets access Class variable from instance itself
print(emp1.empCount)
print(emp2.empCount)

emp1.empCount = 10
emp2.empCount = 20

print(emp1.empCount)
print(emp2.empCount)
print(Employee.empCount)


# What is Static Method in python??
class Car:
    def __init__(self, name, color):
        self.car_name = name
        self.car_color = color
    
    def displayCarDetails(self):
        print("Car name is ",self.car_name," and Car color is ",self.car_color)

    @staticmethod
    def initialMessage():
        print("Nice Car !!!!!")

Car.initialMessage()
car1 = Car('XUV 700', 'Red')
car1.displayCarDetails()

# This will not work
# Car.displayCarDetails()

# iNeuron Company
class Employee:
    @staticmethod
    def isEmployeeOf():
        print("Employee Class for iNeuron !!")
    
Employee.isEmployeeOf()


class Calculation:
    @staticmethod
    def addTwoNums( num1, num2 ):
        print("Sum of two numbers = ", num1 + num2)
    
Calculation.addTwoNums(10,5)
