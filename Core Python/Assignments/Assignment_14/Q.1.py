# 1. Write a Python program to find elements in a given set that are not in
# another set.

def unique_ele(s1,s2):

  print(s1.difference(s2))

s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
unique_ele(s1,s2)

