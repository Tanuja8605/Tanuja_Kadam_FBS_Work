# 11. WAP to check if given number Strong Number.
num = int(input('Enter number:'))
temp = num
sum = 0
while temp > 0:
  digit = temp % 10
  fact = 1
  for i in range(1,digit+1):
    fact = fact*i
  sum = sum + fact
  temp = temp // 10
if sum == num:
  print(f'{num} is strong number')
else:
  print(f'{num} is not strong number')
