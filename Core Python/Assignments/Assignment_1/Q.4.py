# 4. Write a program to enter P, T, R and calculate simple Interest.P = 50000

###Take input from user
P = int(input("Enter Principle:"))
T = int(input("Enter Time:"))
R = int(input("Enter Rate:"))

###Perform Operation

SI = P * R * T/100
print('Simple Interest is',SI)