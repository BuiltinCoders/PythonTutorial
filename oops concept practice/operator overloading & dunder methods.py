# Defining a method for an operator and that process is called operator overloading.
# Operator overloading refers to setting up the functionality of perticular operator for perticular situation.
# Operator in python can be overloaded using dunder method.
# These methods are called when a given operator is used on the objects.

class Employee:
    no_of_employee = 8

    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role

    def printdetails(self):
        return f"Employee name is {self.name}, his salary is {self.salary} and his role is {self.role}"
    
    def __add__(self, other):
        return self.salary + other.salary
    
    def __truediv__(self, other):
        return self.salary / other.salary
    
    def __sub__(self, other):
        return self.salary - other.salary

    def __repr__(self):
        return f"Employee('{self.name}',{self.salary}, '{self.role}')"
    
    def __str__(self):
        return f"Employee name is {self.name}, his salary is {self.salary} and his role is {self.role}"

emp1 = Employee("harry", 346, "programmer")
emp2 = Employee("rohan", 563, "tester")

# print(emp1.printdetails())
print(emp1 + emp2)
print(emp2 / emp1)
print(emp1 - emp2)

print(str(emp1))
print(repr(emp1))
print(emp1.__str__())