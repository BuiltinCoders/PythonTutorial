class Employee:
    no_of_leaves = 8
    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role
    
    def printdetails(self):
        return f"The employee name is {self.name}, salary is {self.salary} and role is {self.role}"
    
    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves
    
    @classmethod
    def from_str(cls, string):
        # params = string.split("-")
        # print(params)
        # return cls(params[0], params[1], params[2])
        return cls(*string.split("-"))

harry = Employee("Harry", 75000, "Manager")
rohan = Employee("Rohan", 50000, "Student")
nitesh = Employee.from_str("Nitesh-100000-CEO")

rohan.change_leaves(73)
print(harry.no_of_leaves)

print(nitesh.salary)
print(nitesh.no_of_leaves)