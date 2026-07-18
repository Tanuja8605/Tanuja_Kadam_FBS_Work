# 1. Python Program to Put Even and Odd elements of a List into two Different
# Lists

def even_odd(li):
    even_li = list(filter(lambda x: x % 2 == 0, li))
    odd_li = list(filter(lambda x: x % 2 != 0, li))

    return even_li, odd_li


li = [3, 2, 6, 8, 9, 3, 5, 6, 7, 10, 23, 15, 67]

even_list, odd_list = even_odd(li)

print("Even numbers list:", even_list)
print("Odd numbers list :", odd_list)