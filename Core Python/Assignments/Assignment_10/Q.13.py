# 13 . Write a program to print list after removing even numbers.
def remove_even(li):
    new_li = []

    for num in li:
        if num % 2 != 0:
            new_li.append(num)

    return new_li


li = [2, 3, 4, 5, 6, 7, 8, 10]

res = remove_even(li)

print("After removing even numbers:", res)