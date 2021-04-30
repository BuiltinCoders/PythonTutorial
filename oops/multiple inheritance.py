class Employee():
    var = 8
    no_of_leaves = 8
    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role
    
    def printdetail(self):
        return f"The Employee name is {self.name}, salary is {self.salary} and role is {self.role}"
    
    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))
    
    @staticmethod
    def printgood(string):
        print("This is a good" + string)

class Player:
    var = 9
    no_of_games = 4
    def __init__(self, name, game):
        self.name = name
        self.game = game
    
    def printdata(self):
        return f"Name of player is {self.name} and game is {self.game}"

class Coolprogrammer(Player, Employee):
    # var = 10
    language = "c++"
    def printlanguage(self):
        print(self.language)
harry = Employee("Harry", 75000, "Instructor")
rohan = Employee("Rohan", 50000, "Student")

shubham = Player("Shubhum", ["Cricket"])
karan = Coolprogrammer("Karan", ["Cricket"])
# det = karan.printdetail()
# print(karan.printlanguage())
# print(det)
print(karan.var)