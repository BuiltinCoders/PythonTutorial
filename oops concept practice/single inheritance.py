# creating a new class from the existing class content is inheritance.

# Type of inheritance :-
# i) single inheritance
# ii) multiple inheritance
# iii) multilevel inheritance

# Single Inheritance
# single inheritance occures when child class inherits only one parent class


class Employee:               # -------------------> Parent Class or base class
    no_of_employee = 8
    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role
    
    def printdeltails(self):
        return f"The Employee name is {self.name}, its salary is {self.salary} and his role is {self.role}"

class CoolProgrammer(Employee):     # ----------------------> Child Class or Derived Class
    # Child class will inherite all the functions and attributed of the parent class.

    def __init__(self, name, salary, role, language):  # ----------------> instead of creating new constructor we can use super attribute
        self.name = name
        self.salary = salary
        self.role = role
        self.language = language

# here we can also overwrite or add new attributes and methods in programmer class

harry = Employee("Harry", 256, "Instructor")
rohan = Employee("Rohan", 365, "student")
karan = CoolProgrammer("Karan", 456, "Manager", "Python")

print(harry.printdeltails())
print(karan.printdeltails())
print(karan.language)