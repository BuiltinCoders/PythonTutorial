f1 = open('records.txt')
try:
    f = open('does.txt')
except Exception as e:
    print(e)
else:
    print('except is not working')
finally:
    print('run anyway...')
    # f.close()
    f1.close()

print("Important stuff")