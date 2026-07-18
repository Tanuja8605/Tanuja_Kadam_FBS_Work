# 9. Write a program to create three lists of numbers, their squares and cubes

def sqr_cube(li):
 
 sq = list(map(lambda x:x**2,li))
 cube = list(map(lambda x:x**3,li))

 return li,sq,cube

li = [2,4,6,8,3]

num,sq,cube = sqr_cube(li)

print('numbers:',li)
print('square:',sq)
print('Cube:',cube)




