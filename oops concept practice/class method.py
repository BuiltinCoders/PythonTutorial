class Employee:
    no_of_employee = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole
    
    def printdetails(self):
        return f"The name is {self.name}, salary is {self.salary} and role is {self.role}"
    
    @classmethod
    def changeemployee(cls, newemployee):
        cls.no_of_employee = newemployee

harry = Employee("Harry", 455, "Instructor")
rohan = Employee("Rohan", 4554, "Student")

harry.changeemployee(73)

print(harry.no_of_employee)