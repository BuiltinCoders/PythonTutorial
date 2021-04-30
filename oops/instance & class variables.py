class Employee:
    no_of_leaves = 8
    pass
# Employee is class
# We should write first letter of class name in capital because it is a good practice

harry = Employee()
rohan = Employee()
# Here, harry and rohan are instances

harry.name = "Harry"
harry.salary = 25000
harry.role = "Instructor"

rohan.name = "Rohan"
rohan.salary = 20000
rohan.role = "student"

# print(harry.name)
# print(rohan.no_of_leaves)

# we can change class variables only from class name like:-
# Employee.no_of_leaves = 9
# print(Employee.no_of_leaves)
# This works but-

# print(Employee.no_of_leaves)
# rohan.no_of_leaves = 9
# print(Employee.no_of_leaves)
# This didn't work. So we can only change class variables with class name

# Verification

# on instances
# print(Employee.no_of_leaves)
# print(rohan.__dict__)
# rohan.no_of_leaves = 9
# print(rohan.__dict__)
# print(Employee.no_of_leaves)

# on class variables
print(Employee.no_of_leaves)
print(Employee.__dict__)
Employee.no_of_leaves = 9
print(Employee.__dict__)
print(Employee.no_of_leaves)