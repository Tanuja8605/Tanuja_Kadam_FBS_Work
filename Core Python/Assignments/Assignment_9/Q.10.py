# 10. Write a program to reverse a number using recursion.
def iscount(num):
  if num == 0:
   return 0
  else:
    return(1 + iscount(num//10))
def isreverse(num,count):
  if num == 0:
    return 0
  else:
     d = num % 10
     return d * 10 **(count - 1) + isreverse(num//10,count - 1)
  
num = int(input('Enter number:'))
count = iscount(num)
res = isreverse(num,count)
print(f'{num} is reverse is {res}')

