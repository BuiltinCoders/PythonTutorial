# we can use else with for loop when for loop worked properly or completed his job

items = ['books', 'laptop', 'watch', 'water bottle']

for item in items:
    if item=='watch':
        print(item)
        break
else:
    print('for loop worked properly')