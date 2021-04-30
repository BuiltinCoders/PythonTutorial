# # Simple Class
# class Employee:
#     pass

# # Objects are also known as Instances

# # Objects(instances)
# harry = Employee()
# rohan = Employee()

# # harry instance variables
# harry.name = "Harry"
# harry.salary = 7500
# harry.role = "manager"

# # rohan instance variables
# rohan.name = "Rohan"
# rohan.salary = 50000
# rohan.role = "student"


# print(harry.name)


# # Advance Class with self & __int__(constructor)

# self --> self stands for objects of class
# __init__ --> __init__ is a constructor which contains instance variables
# __init__ constructor increases code reusability

class Employee:
    # using __init__ constructor
    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole
    # creating class methods
    def print_details(self):
        return f"Employee name is {self.name}, Salary is {self.salary} and Role is {self.role}"

# using self first
# harry = Employee()
# rohan = Employee()

# harry.name = "Harry"
# harry.salary = 75000
# harry.role = "manager"

# rohan.name = "Rohan"
# rohan.salary = 50000
# rohan.role = "student"

# print(harry.print_details())


# using self with __init__ constructor
# objects(instances) of final modified Employee class

harry = Employee("Harry", 75000, "manager")
rohan = Employee("Rohan", 50000, "student")

print(harry.name)
print(rohan.name)
print(harry.salary)
print(rohan.salary)
print(harry.role)
print(rohan.role)