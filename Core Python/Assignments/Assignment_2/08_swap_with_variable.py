# 8. Write a program to swap two numbers using third variable.

###Take input from user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(f'Before swapping: a = {a}, b = {b}')

###Swapping numbers
temp = a
a = b
b = temp

print(f'After swapping: a = {a}, b = {b}')