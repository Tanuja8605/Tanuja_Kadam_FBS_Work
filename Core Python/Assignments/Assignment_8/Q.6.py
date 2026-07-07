def fibo(n):
  a = 0
  b = 1
  total = 0
  if n >= 1:
    print(a,end = ' ')
  if n >= 2:
    print(b,end = ' ')
  for i in range(3,n+1):
    c = a+b
    print(c,end = ' ')
    a = b
    b = c
  

  
num = int(input('Enter n:'))
fibo(num)


  