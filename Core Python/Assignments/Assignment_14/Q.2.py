# 2. Write a Python program to remove the intersection of a second set
# with a first set.

def remove_intersection(s1,s2):
  s1.intersection(s2)
  s1.difference(s2)

  s1.difference_update(s2)
  print(s1)


s1 = {1,2,3,4,5}
s2 = {2,3,4,5,6}

remove_intersection(s1,s2)

  