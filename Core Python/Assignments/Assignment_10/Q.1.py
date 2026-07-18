# 1. Write a program to find sum of all elements of list
def listsum(li):
 total = 0
 for i in li:
   for j in i:
     total += j
 return total
li = [[10,20],[30,40],[50,60]]
res = listsum(li)
print(res)