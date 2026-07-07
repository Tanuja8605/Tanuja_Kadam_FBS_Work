# 3. Write a program to reverse a given number using recursive function.
def iscount(num):
  if num == 0:
    return 0
  else:
    return 1 + iscount(num//10)
  
def rev(num,count):
  if num == 0:
    return 0
  else:
    d = num % 10
    return d * (10 ** (count - 1)) + rev(num // 10, count - 1)
  
  



num = int(input('Enter number:'))
count = iscount(num)
res = rev(num,count)
print(res)