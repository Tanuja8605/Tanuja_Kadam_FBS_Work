# 2. Python Program to Concatenate Two Dictionaries Into One

def dict_concatinate(dict1,dict2):

  new_dict = {}

  for key in dict1:
    new_dict[key] = dict1[key]

  for key in dict2:
    new_dict[key] = dict2[key]

  return new_dict

dict1 = {'name':'Ram','City':'Pune'}

dict2 = {'salary':34000,'dept':'IT'}

res = dict_concatinate(dict1,dict2)

print(res)

