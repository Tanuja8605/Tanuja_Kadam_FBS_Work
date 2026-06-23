# 9. WAP to print all numbers in a range divisible by a given number.
start = int(input('Enter starting:'))
stop = int(input('Enter stop:'))
num = int(input('Enter divisior:'))
for i in range(start,stop + 1):
  if i % num == 0:
    print(i)

