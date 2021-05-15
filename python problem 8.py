#                                    Rohan Das is a Fraud

def iscorrect(table, number):
    for value in range(0, len(table)+1):
        if table[value] != number*(value+1):
            return f"Index value is {value+1}"

    return None


print(iscorrect([5, 10, 15, 20, 25, 40, 35, 40, 46, 50], 5))