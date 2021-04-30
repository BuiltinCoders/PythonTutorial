# object introspection refers introspect the object and about their class, attributes, objects.

class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    # self.email = f"{fname}.{lname}@email.com"

    def explain(self):
        return f"This employee is {self.fname}{self.lname}"
    
    @property
    def email(self):
        if self.fname==None or self.lname==None:
            return "Email is not set yet"
        return f"{self.fname}.{self.lname}@email.com"
    
    @email.setter
    def email(self, string):
        print("Setting now...")
        names = string.split('@')[0]
        fname = names.split('.')[0]
        lname = names.split('.')[1]
    
    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None

skillf = Employee('Skill', 'F')

# print(skillf.email)

# Type   --------------- shows class of object and their type
# print(type(skillf))

# ID   ----------------- shows the id of the object
# print(id(skillf))

# Dir   --------------- shows functions and attributes of the object wwhich we can on it
# print(dir(skillf))

# Inspect  --------------- shows all members of the object. Gives all information related to object
import inspect
print(inspect.getmembers(skillf))