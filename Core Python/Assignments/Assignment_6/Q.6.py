for i in range(1,6):
  num = i+1
  for j in range(1,6-i):
    print(' ',end = ' ')
  for j in range(1,i+1):
    print(j,end = ' ')
  for j in range(1,i):
    print(num,end = ' ')
    num += 1
 
  print()