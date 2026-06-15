# 10. Write a program to reverse three-digit number.

###Take input from user
num = int(input("Enter any number:"))
###Reverse the number
u_digit = num % 10
ten_digit = (num //10) % 10
h_digit = (num // 100) 

reverse = u_digit * 100 + ten_digit * 10 + h_digit 

print(f'reverse number of {num} number is {reverse}')