# Write a program to check whether the triangle is equilateral, isosceles or scalene triangle.
# Take input from user
a = int(input('Enter value of a:'))
b = int(input('Enter value of b:'))
c = int(input('Enter value of c:'))


if((a + b > c)and(a + c > b)and(b + c > a)):
  if(a == b == c):
      print('Equilateral')
  elif(a == b or b == c or a == c):
       print('Isosceles')
  else:
        print('Scalene')
else:
    print('Invalid Triangle')
     





