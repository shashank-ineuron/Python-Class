# # Inheritance in Python

# # Base Class aka Parent Class
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

# How to initialize constructor of Base Class
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

    def __init__(self,emp_name, id_num, salary, designation):
        self.idnumber = id_num
        self.emp_salary = salary
        self.emp_designation = designation

        # Calling constructor of Base Class
        # Person.__init__(self,emp_name)
        super().__init__(emp_name)
        
    def isEmployed(self):
        print(self.name," is Employed !!")

    def employeeDetails(self):
        print("Employee Id is ",self.idnumber,
        " Employee Salary is ",self.emp_salary,
        " Employee Designation is ",self.emp_designation)

emp1 = Employee('Shashank',5432,1000,'Data Engineer - 3')
emp1.displayName()
print(emp1.name)
emp1.employeeDetails()
