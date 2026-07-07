# 8. Write a program to check whether a number is prime or not using recursion.

def isprime(num, divisor=2):
    if num <= 1:
        return False

    if divisor * divisor > num:
        return True

    if num % divisor == 0:
        return False

    return isprime(num, divisor + 1)

num = int(input("Enter number: "))

if isprime(num):
    print("Prime")
else:
    print("Not Prime")