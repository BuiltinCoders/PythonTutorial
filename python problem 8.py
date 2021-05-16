#                                    Rohan Das is a Fraud
import random

def rohanTable(number):
    wrong = random.randint(0, 9)
    table = [i*number for i in range(1, 11)]
    table[wrong] = table[wrong]+wrong
    return table


def iscorrect(table, number):
    for value in range(0, len(table)+1):
        if table[value] != number*(value+1):
            return f"This table is wrong at index value {value+1}"
    return None

number = int(input("Enter the number: "))

table = rohanTable(number)
print(table)
print(iscorrect(table, number))