# 2. Write a program to find maximum and minimum element in a list.

def findMaxMin(li):
    min = li[0]
    max = li[0]

    for num in li:
        if num > max:
            max = num

        if num < min:
            min = num

    return max, min


li = [5, 30, 10, 4, 8, 2, 30, 45, 12]

maximum, minimum = findMaxMin(li)

print("Maximum =", maximum)
print("Minimum =", minimum)