# 5. Python Program to Sum All the Items in a Dictionary

def sum_items(d):
  total = 0
  for value in d.values():
    total += value
  return total

d = {'a':10,'b':30,'c':15}
res = sum_items(d)
print('sum of all dictionary items:',res)
    