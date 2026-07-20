# 6. Python Program to Multiply All the Items in a Dictionary

def multiply_item(d):
    result = 1
    for value in d.values():
        result *= value
    print('multiplication of all items in dictionary',result)

d = {'a':2, 'b':4, 'c':5}

multiply_item(d)