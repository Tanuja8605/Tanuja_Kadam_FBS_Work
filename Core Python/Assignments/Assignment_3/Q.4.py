# 4. Write a program to input all sides of a triangle and check whether triangle is valid or not.
# Take input from User
side_1 = int(input('Enter 1st side of triangle:'))
side_2 = int(input('Enter 2nd side of triangle:'))
side_3 = int(input('Enter 3rd side of triangle:'))

if((side_1 + side_2 > side_3)and(side_1 + side_3 > side_2)and(side_3 + side_2 > side_1)):
  print('Triangle is valid')
else:
  print('Triangle is not valid')

