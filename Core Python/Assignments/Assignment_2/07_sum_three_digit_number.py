# 7. Find the sum of three-digit number.

###Take input from user
num = int(input("Enter four digit number:"))

###Perform Operation
#hundreds = num // 100
#tens = (num // 10) % 10
#units = num % 10

#sum = hundreds + tens + units

d1 = num % 10
num = num // 10

d2 = num % 10
num = num // 10

d3 = num % 10
num = num // 10

d4 = num % 10
num = num // 10

sum = d1 + d2 + d3 + d4

print('sum of digits is :',sum)