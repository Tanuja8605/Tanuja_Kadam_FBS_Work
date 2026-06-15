# 12. Write a program to check if given 3 digit number is a palindrome or not.
num = int(input('Enter number:'))
orig_num = num

unit_digit = num % 10
tens_digit = (num // 10) % 10
h_digit = num // 100

reverse = unit_digit*100 + tens_digit*10 + h_digit

if(orig_num == reverse):
  print('num is palindrome')
else:
  print('num is not palindrome')