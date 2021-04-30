#                            Dimond Shape Problem

#                                    A
#                                   / \
#                                  /   \
#                                 /     \
#                                B       C
#                                 \      /
#                                  \    /
#                                   \  /
#                                     D


# Dimond Shape Problem
# In this problem coder can't understand the inheritance sequence

class A:
    def met(self):
        print("This is method from class A")

class B(A):
    def met(self):
        print("This is method from class B")

class C(A):
    def met(self):
        print("This is method from class C")
    var = 779

class D(B, C): # or class D(C, B):
    def met(self):
        print("This is method from class D")


a = A()
b = B()
c = C()
d = D()

d.met()
print(d.var)