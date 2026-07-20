# 1. Python Program to Replace all Occurrences of ‘a’ with $ in a String

def replace_char(str):
  return str.replace('a',' $ ')

str = input('Enter String:')
res = replace_char(str)
print('After replacing:',res)