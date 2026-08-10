### Assignment on Generator
# 1. We want to generate Fibonacci numbers up to a certain limit.
# Instead of computing and storing the entire sequence in memory,
# create generator to yield Fibonacci numbers one by one,
# conserving memory and allowing for easy iteration.

def fibo(n):
  a = 0
  b = 1
  for i in range(1,n+1):
    yield(a)
    c = a+b
    a = b
    b = c
f = fibo(5)
print(next(f))
print(next(f))
print(next(f))

print(next(f))

  
