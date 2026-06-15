# 1. Write a program to calculate the percentage of student based on marks of any 5 subjects.

##Take input from user
m1 = int(input("Enter first sub marks:"))
m2 = int(input("Enter second sub marks:"))
m3 = int(input("Enter third sub marks:"))
m4 = int(input("Enter fourth sub marks:"))
m5 = int(input("Enter fifth sub marks:"))

obtained_marks = m1+m2+m3+m4+m5

total = 500

###Perform Operation

percentage = obtained_marks/total * 100

print(f'percentage of best 5 is {obtained_marks}/{total} is {percentage}')

print(id(m1))
print(id(m2))
print(id(m3))
print(id(m4))
print(id(m5))
print(id(total))
print(id(obtained_marks))
print(id(percentage))




