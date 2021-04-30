class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{self.fname}.{lname}@email.com"
    def explain(self):
        return f"This employee is {self.fname}, {self.lname}"

    @property
    def email(self):
        if self.fname==None or self.lname==None:
            return "Email is not set. Try to set it using setter."
        return f"{self.fname}.{self.lname}@email.com"

    @email.setter
    def email(self, string):
        print("setting now...")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None

hindustani_supportor = Employee("Hindustani", "Supportor")

print(hindustani_supportor.email)

hindustani_supportor.fname = "US"
print(hindustani_supportor.email)

hindustani_supportor.email = "this.that@email.com"
print(hindustani_supportor.email)
print(hindustani_supportor.fname)
print(hindustani_supportor.lname)

# del hindustani_supportor.email
# print(hindustani_supportor.email)

hindustani_supportor.email = 'joker.haa@email.com'
print(hindustani_supportor.email)