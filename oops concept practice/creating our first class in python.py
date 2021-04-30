class Student:
    pass

nitesh = Student()
jake = Student()

nitesh.name = "Nitesh"
nitesh.std = 12
nitesh.section = 1

jake.std = 9
jake.subjects = ["Hindi", "Physics"]

print(nitesh.name)
print(nitesh.std)
print(jake.std)
print(nitesh.section, jake.subjects)

print(jake.name)  # '''showing error because we have not defined name attribute in jake object '''
