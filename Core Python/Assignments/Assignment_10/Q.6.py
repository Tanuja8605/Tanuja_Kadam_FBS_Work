# 6. Write a program to remove duplicates from the list.

def duplicate(li):
 new_li = []
 for num in li:
   if num not in new_li:
     new_li.append(num)
 return new_li

li = [20,10,30,40,50,40,90,30]
res = duplicate(li)
print(res)
  
    

 


  
  
