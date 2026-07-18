# 2. Python Program to Merge Two Lists and Sort it
def merge_and_sort(li1,li2):
  new_li = li1 + li2
  new_li.sort()
  return new_li
li1 = [3,2,5,7,8,9]
li2 = [1,4,6,11,10]
res = merge_and_sort(li1,li2)
print(res)
  