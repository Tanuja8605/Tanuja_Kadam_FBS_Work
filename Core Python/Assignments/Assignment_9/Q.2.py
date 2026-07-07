# 2. Write a program to check if given number is Armstrong or not using recursive function.
def isarmstrong(num,power):
  if num == 0:
    return 0
  else:
   d = num % 10
   return (d**power) + isarmstrong(num // 10,power)
  

num = int(input('Enter number:'))
power = len(str(num))
res = isarmstrong(num,power)
if res == num:
  print('is Armstrong')
else:
  print('is not Armstrong')