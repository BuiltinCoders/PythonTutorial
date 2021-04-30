# Multiple Inheritance
# Multiple Inheritance occurs when child class inherits more then one parent class

class Employee:
    no_of_employee = 8
    var = 8
    
    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role
    
    def printdetails(self):
        print(f"Employee name is {self.name}, his salary is {self.salary} and his role is {self.role}")


class Player:
    var = 9
    no_of_games = 4

    def __init__(self, name, game):
        self.name = name
        self.game = game
    
    def printdetails(self):
        print(f"Employee name is {self.name} and his game is {self.game}")


class CoolProgrammer(Player, Employee):
    var = 10
    language = "c++"

    def printlanguage(self):
        print(self.language)

harry = Employee("Harry", 256, "Instructor")
rohan = Player("Rohan", ["Cricket"])
karan = CoolProgrammer("Karan", ["Cricket"])

# print(harry.printdetails())
# print(rohan.printdetails())
# print(karan.printdetails())
# print(karan.printlanguage())

print(karan.var)