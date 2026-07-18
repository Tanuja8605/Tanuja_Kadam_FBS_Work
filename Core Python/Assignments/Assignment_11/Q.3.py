# 3. Python Program to Sort the List According to the Second Element in Sublist

def sort_second(li):
    li.sort(key=lambda x: x[1])
    return li


li = [[10, 3], [20, 1], [30, 2], [40, 5], [50, 4]]

res = sort_second(li)

print("Sorted List:", res)