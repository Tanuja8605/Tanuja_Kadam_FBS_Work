# 7. Python Program to Find the Intersection of Two Lists

def liintersection(li1,li2):
  new_li = []
  for i in li1:
   if i in li2 and i not in new_li:
    new_li.append(i)
  print(new_li)
li1 = [1,2,3,5,5,4]
li2 = [3,4,5,5,6]
liintersection(li1,li2)
     
   
