# 8. Write a program to swap two numbers without using third variable.

###Take input from user
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
###Swapping the numbers
#a = a + b
#b = a - b
#a = a - b

a,b = b,a

print(f'after swapping a is {a} & b is {b}')