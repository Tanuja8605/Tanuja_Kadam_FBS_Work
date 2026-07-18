# 6. Python Program to Find the Union of two Lists
def liunion(li1,li2):
  new_li = []
  for i in li1:
   new_li.append(i)
  for j in li2:
   if j not in new_li:
     new_li.append(j)
  print(f'Union of two lists is',new_li)

      
li1 = [1,5,3,4]
li2 = [3,4,5,6]
liunion(li1,li2)