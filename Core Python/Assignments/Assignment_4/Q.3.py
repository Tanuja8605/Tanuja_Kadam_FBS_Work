# 3. WAP to print sum of series upto n.
n = int(input('Enter the terms:'))
i = 1
sum = 0
while(i <= n): 
  sum = sum + i
  i += 1
print('Sum is',sum)