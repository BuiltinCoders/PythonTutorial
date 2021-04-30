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
    def from_desh(cls, string):
        params = string.split("-")
        return cls(params[0], params[1], params[2])
    
    @staticmethod
    def printgood(string):
        print(f"This is good {string}")
        return "keep it up"

harry = Employee("Harry", 75000, "Manager")
rohan = Employee("Rohan", 50000, "Student")
nitesh = Employee.from_desh("Nitesh-100000-Student")



harry.change_leaves(9)
print(rohan.no_of_leaves)

print(nitesh.salary)
print(nitesh.role)

print(Employee.printgood("Nitesh"))