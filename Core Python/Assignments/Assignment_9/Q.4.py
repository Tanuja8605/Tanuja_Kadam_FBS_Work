# 4. Write a program to find sum of n numbers using recursion.
def sumofn(n):
  if n == 1:
    return 1
  else:
    return n + sumofn(n-1)
n = int(input('Enter n:'))
res = sumofn(n)
print(res)