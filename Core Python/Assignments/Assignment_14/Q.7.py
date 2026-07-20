# 7. Given two sets of numbers, write a Python program to find the missing
# numbers in the second set as compared to the first and vice versa.
# Use the Python set.

def missing_num(s1,s2):
  print("Missing in second set",s1.difference(s2))
  print("Missing in first set:",s2.difference(s1))
  

s1 = {1,2,3,4}
s2 = {2,5,6}
missing_num(s1,s2)