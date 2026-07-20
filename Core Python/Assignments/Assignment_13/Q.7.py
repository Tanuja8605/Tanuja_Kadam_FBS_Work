# 7. Python Program to Remove the Given Key from a Dictionary

def remove_key(di, key):

    if key in di:
      del di[key]
    else:
      print("Key not found")
    return di


di = {'name':'Ram','City':'Pune','Sal':45000,'Dept':'IT'}
key = input("Enter key which you want to remove: ")

res = remove_key(di, key)
print("After removing given key:", res)