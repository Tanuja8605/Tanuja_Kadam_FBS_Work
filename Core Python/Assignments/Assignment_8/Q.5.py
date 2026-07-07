def even_sum(n):
  total = 0
  for i in range(1,n+1):
     if i % 2== 0:
        total+=i
  return total
num = int(input('Enter value of n:'))
result = even_sum(num)
print(result)