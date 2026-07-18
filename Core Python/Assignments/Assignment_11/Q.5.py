# 5. Python Program to Sort a List According to the Length of the Elements
# within the list.
def len_lisort(li):
  size = len(li)
  for i in range(size-1):
    for j in range(size-i-1):
     if len(li[j]) > len(li[j + 1]):
       li[j],li[j+1] = li[j+1],li[j]

  return li
li = [[2,3,4],[4,5],[5,6,7,8]]
res = len_lisort(li)
print(res)
      
