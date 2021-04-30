class Employee:
    no_of_employee = 8

    def __init__(self, oname, osalary, orole):
        self.name = oname
        self.salary = osalary
        self.role = orole
    
    @classmethod
    def split_string(cls, string):
        param = string.split("-")
        print(param)
        return cls(param[0], int(param[1]), param[2])

harry = Employee("harry", 252, "Instructor")
rohan = Employee("Rohan", 376, "Student")
karan = Employee.split_string("Karan-567-Student")

print(karan.salary)
print(harry.name)
print(rohan.role)