# # Class Methods
 # class methods are the functions defined in a class

class Employee:
    no_of_leaves = 8
    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role
    
    def printdetails(self):
        return f"The employee name is {self.name}, salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

harry = Employee("Harry", 75000, "Manager")
rohan = Employee("Rohan", 50000, "Student")

# print(harry.salary)


# how to change class variables
 # we must change class variable with employee name not with instance name 

# print(harry.no_of_leaves)
# # Employee.no_of_leaves = 89
# harry.no_of_leaves = 89
# print(Employee.__dict__)
# print(harry.no_of_leaves)
# print(harry.__dict__)


# When we change class variable value using instance name:-
# 1. instance first, searches the variable in the instance variable then in absence, it goes to class variable