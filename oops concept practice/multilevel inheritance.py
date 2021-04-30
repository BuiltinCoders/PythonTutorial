# multilevel inheritance occurs when child class become the parent class of another child class

class Dad:
    basketball = 6

class Son(Dad):
    dance = 1
    basketball = 9

    def isdance(self):
        return f"Yes I dance {self.dance} no. of times"

class Grandson(Son):
    dance = 6
    guitar = 1

    def isdance(self):
        return f"Jackson veah!"\
            f" Yes I dance very awesomely {self.dance} no. of times"

darry = Dad()
larry = Son()
harry = Grandson()

print(harry.basketball)
print(harry.isdance())
print(harry.isdance())     # if isdance method of Grandson is commented
print(darry.isdance())  # error