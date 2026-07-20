# 1. Python Program to Add a Key-Value Pair to the Dictionary
def dictionary(dict):
  key = input("Enter key: ")
  value = int(input("Enter value: "))
  dict[key] = value
  
  return dict

dict = {'name':'Ram', 'city':'Pune'}
res = dictionary(dict)
print('After creating dictionary:',res)