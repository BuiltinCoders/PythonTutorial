class Employee():
    no_of_leaves = 8
    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role
    
    def printdetail(self):
        return f"The Employee name is {self.name}, salary is {self.salary} and role is {self.role}"
    
    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))
    
    @staticmethod
    def printgood(string):
        print("This is a good" + string)

class Programmer(Employee):
    def __init__(self, name, salary, role, languages):
        self.name = name
        self.salary = salary
        self.role = role
        self.languages = languages

    def printprog(self):
        return f"Programmer name is {self.name}, salary is {self.salary}, role is {self.role} and languages are {self.languages}"
    
harry = Employee("Harry", 75000, "Instructor")
rohan = Employee("Rohan", 50000, "Student")
nitesh = Employee.from_dash("Nitesh-100000-Student")
mohan = Programmer("Mohan", 23000, "Programmer", ["Python"])
sohan = Programmer("Sohan", 73000, "Programmer", ["Python", "c++"])

print(mohan.printprog())
print(mohan.printdetail())
print(sohan.printprog())