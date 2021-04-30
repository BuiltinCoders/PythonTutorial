# Type of access specifiers
# i) Public variables
# ii) Private Variables
# iii) protected Variables

# i) Public Variables
# Public Variables are those variables, the value of these variables are public thoughtout out the code.

# ii) Private Variables
# The values of private variables are not easy to derive. Private Variables use name angling to hide the value of the
# the variable.

# Private variables are donated by the prefixing two uderscores before the variables. Example:-
# __name, __class or __anythingelse

# iii) Protected Variables
# Protected Variables are those variables which are the accessible only by the members of the class or by thier
# child classes.

# Protected Variables are donated by the prefixing single underscore before the variables. Example:-
# _name, _class or _anythingelse


class Employee:
    no_of_leaves = 8

    _favfood = "aaloo dum"                   # Protected Variables
    __hobies = "playing video games"         # Private Variables

    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role
    
    def printdetails(self):
        return f"Employee name is {self.name}, his salary is {self.salary} and his role is {self.role}"
    
sam = Employee("Sam", 356, "Programmer")

# print(sam.printdetails())
print(sam._favfood)             # geting values of protected variables

print(sam.__hobies)             # will show error, because we can't get values of private variables directly
print(sam._Employee__hobies)    # use this type of syntax to get the values of the private values