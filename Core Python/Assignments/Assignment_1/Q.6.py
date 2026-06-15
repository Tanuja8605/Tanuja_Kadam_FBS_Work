# 6. Write a Program to input two angles from user and find third angle of the triangle.

###Take input from user
ang1 = int(input("Enter first angle:"))
ang2 = int(input("Enter second angle:"))

###Perform Operation
ang3 = 180 - (ang1 + ang2)

print(f'Third angle is {ang3}')