# 7. Write a program to find sum of digits using recursion.
def sumofdigit(num):
  if num == 0:
    return 0
  d = num % 10
  return d + sumofdigit(num // 10)
num = int(input('Enter number:'))
res = sumofdigit(num)
print(res)
