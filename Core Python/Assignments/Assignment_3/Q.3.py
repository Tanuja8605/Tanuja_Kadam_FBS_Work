# 3. Write a program to input angles of a triangle and check whether triangle is valid or not.

# Take input from user
ang1 = int(input('Enter first angle:'))
ang2 = int(input('Enter second angle:'))
ang3 = int(input('Enter third angle:'))

# Calculate sum
total = ang1 + ang2 + ang3

if(ang1 > 0, ang2 > 0, ang3 > 0):
  if(total == 180):
    print('Triangle is valid')
  else:
    print('Triangle is not valid')
else:
  print('Not valid')
  
  