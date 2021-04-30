class Employee:
    no_of_employee = 8

    def __init__(self, oname, osalary, orole):
        self.name = oname
        self.salary = osalary
        self.role = orole
    
    @staticmethod
    def printgood(string):
        return f"This is good {string}"
    

harry = Employee("Harry", 235, "Instructor")
rohan = Employee("Rohan", 453, "Student")

print(harry.printgood("harry"))
print(Employee.printgood("harry"))