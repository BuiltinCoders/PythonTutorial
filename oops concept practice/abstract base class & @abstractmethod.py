# abstractmethod created in parent class force their child class to define particular function,  method, etc.

from abc import ABCMeta, abstractmethod

class Shape(metaclass = ABCMeta):
    @abstractmethod
    def printarea(self):
        return 0

class Quadrilateral(Shape):
    type = 'Rectangle'
    sides = 4

    def __init__(self):
        self.length = 6
        self.breath = 5

    # def printarea(self):
        # return self.length * self.breath

q1 = Quadrilateral()
# q2 = Shape()  ----- error
# print(q1.printarea())