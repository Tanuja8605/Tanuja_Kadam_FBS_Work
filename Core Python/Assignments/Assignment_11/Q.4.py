# 4. Python Program to Find the Second Largest Number in a List Using Bubble
# Sort

def sort_bubblesearch(li):
    size = len(li)

    for i in range(1, size):
        for j in range(0, size - i):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]

    largest = li[-1]

    for i in range(size - 2, -1, -1):
        if li[i] != largest:
            return li[i]

    return "Second largest element does not exist"

li = [4,5,6,7,8,9,6]
res = sort_bubblesearch(li)
print("Second largest is", res)