# 10. Write a program to remove all occurrences of a given element in the list.

def remove_occur(li,num):
  new_li = []
  for ele in li:
    if ele != num:
      new_li.append(ele)
  return new_li

li = [2,4,5,2,8,9,4,2,10,4]
num = int(input('Enter number:'))
res = remove_occur(li,num)
print(f'New list is {res}')
