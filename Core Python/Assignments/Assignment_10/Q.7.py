# 7. Write a program to create a new list from existing list which contains cube of
# each number of list.
def liCube(li):
 new_li = []
 for num in li:
    new_li.append(num**3)
 return new_li

li = [3,4,6,9,1,2,8]
res = liCube(li)
print(res)
