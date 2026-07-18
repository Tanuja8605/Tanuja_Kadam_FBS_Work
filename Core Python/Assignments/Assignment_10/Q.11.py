# 11. Write a program to print all numbers which are divisible by m and n in the
#  list.

def divisible_by_m_n(li, m, n):
    new_li = []

    for num in li:
        if num % m == 0 and num % n == 0:
            new_li.append(num)

    return new_li


li = [2, 4, 6, 8, 9, 10, 11, 45]

m = int(input("Enter value of m: "))
n = int(input("Enter value of n: "))

res = divisible_by_m_n(li, m, n)

print(res)