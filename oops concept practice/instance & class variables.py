# Class variables

# 1. variables which are shared by all the objects of the perticular class.
# 2. class varible have specific value for all the objects of a class.
# 3. class variable can only be changed though class name.

# Instance Variables 

# 1. Instance variables are those variables which are created for specific object of a class.
# 2. Instance variables have specific value for each objects or instances of class.
# 3. Their specific value can only changed though object name.



class Employee:
    no_of_employee = 10   # class variable
    pass

# Object
nitesh = Employee()
rohan = Employee()

# object variable or instance variable
nitesh.name = "Nitesh"
nitesh.salary = 435
nitesh.role = "Instructor"

rohan.name = "Rohan"
rohan.salary = 4554
rohan.role = "student"

print(Employee.no_of_employee)
print(Employee.__dict__)

Employee.no_of_employee = 15  # we can change class variable only through class name
print(Employee.no_of_employee)
print(Employee.__dict__)

nitesh.no_of_leaves = 20
print(Employee.no_of_employee)  # we cannot change class variable though object name. This will just create 
# an another instance variable of harry object.
print(nitesh.__dict__)