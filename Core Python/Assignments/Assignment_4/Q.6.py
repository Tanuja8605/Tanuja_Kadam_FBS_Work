# 6. WAP to check if a given number is prime number or not.
num = int(input('Enter number:'))
if num <= 1:
  print(f'{num} is not prime and nor composite')
else:
  for i in range(2,num):
    if num % i == 0:
      print(f'{num} is not prime')
      break
  else:
    print(f'{num} is prime')