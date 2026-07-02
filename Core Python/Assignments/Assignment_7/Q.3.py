for i in range(1,6):
  for j in range(1,i+1):
    if i == 5 or i == j or j == 1:
      print(j,end = ' ')
    else:
      print(' ',end = ' ')
  print()