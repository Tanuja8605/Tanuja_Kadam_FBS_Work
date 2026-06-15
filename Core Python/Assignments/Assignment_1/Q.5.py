# 5. Write a program to enter P, T, R and calculate Compound Interest.

###Take input from user
P = int(input("Enter the principle amount:"))
R = int(input("Enter the rate:"))
T = int(input("Enter the Time:"))

###Perform Operation

CI = P * (1 + R / 100) ** T

print(f'compound interest of {P} is {CI}')