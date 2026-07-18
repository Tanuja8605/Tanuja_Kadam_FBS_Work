# 4. Write a program to reverse the list.
def reverse(li):
 start = 0
 end = len(li) - 1
 while start < end:
   li[start],li[end] = li[end],li[start]
   start += 1
   end -= 1
 return li

li = [50,40,30,20,10]
res = reverse(li)
print(f'Reversed list {res}')

