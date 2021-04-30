# # # self in classes indicates object name 

# class Employee:
#     no_of_employee = 8

#     def printdetail(self):
#         return f"name is {self.name}, salary is {self.salary} and role is {self.role}"

# harry = Employee()
# rohan = Employee()

# harry.name = "Harry"
# harry.salary = 455
# harry.role = "instructor"

# rohan.name = "Rohan"
# rohan.salary = 4554
# rohan.role = "student"

# print(rohan.printdetail())
# print(harry.printdetail())


# # __init__(constructor)
# constructor runs automatically
# constructor creates framwork for the objects

class Employee:
    no_of_employee = 8
    
    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole
    
harry = Employee("Harry", 455, "Instructor")
rohan = Employee("Rohan", 4554, "student")

print(harry.name)
print(harry.salary)
print(harry.role)
print(rohan.name)
print(rohan.salary)
print(rohan.role)