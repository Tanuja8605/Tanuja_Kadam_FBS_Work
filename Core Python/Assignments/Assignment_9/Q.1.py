# 1. Write a program to find sum of following series using recursive functions:

# i. 1! + 2! + 3! + 4! +..... + n!

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def sum(n):
    if n == 1:
        return factorial(1)
    else:
        return factorial(n) + sum(n - 1)

n = int(input("Enter n: "))
res = sum(n)
print("Sum =", res)
  


