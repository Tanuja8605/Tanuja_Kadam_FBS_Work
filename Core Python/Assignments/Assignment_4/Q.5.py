# 5. WAP to print Fibonacci series upto n.
# n = int(input('How many fibonnaci number you want:'))
# a = -1
# b = 1
# for i in range(n):
#   c = a + b
#   print(f'{a} + {b} = {c}')
#   a = b
#   b = c

start = int(input('Startimg:'))
stop = int(input('Stoping:'))
num = int(input('divisor:'))
for i in range(start,stop + 1):
  if i % num == 0:
    print(i)