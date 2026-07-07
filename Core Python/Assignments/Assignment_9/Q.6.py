# 6. Write a program to print Fibonacci series using recursion.
def fibo(num):
  if num == 0:
    return 0
  elif num == 1:
    return 1
  else:
    return fibo(num - 1) + fibo(num-2)
  
num = int(input('Enter number:'))
for i in range(num):
  print(fibo(i), end=" ")



  