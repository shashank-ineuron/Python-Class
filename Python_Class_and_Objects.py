# How to create a class in Python
class Employee:
    # Constructor of class
    # it is mainly used for assignment of instance variables
    def __init__(self, name, salary ):
        # instance variable or instance attributes
        self.emp_name = name
        self.emp_salary = salary
    # method of a class
    def displayEmployeeInfo(self):
        print("Employee name : ",self.emp_name, " , Employee Salary : ",self.emp_salary)

emp1 = Employee('Shashank', 1000)
emp2 = Employee('Rahul', 2000)

emp1.displayEmployeeInfo()
emp2.displayEmployeeInfo()

print(emp1.emp_name)
print(emp2.emp_name)










