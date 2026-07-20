# 6. Python Program to Take in a String and Replace Every Blank Space
# with Hyphen

def replace_space(str):
  new_str = ''
  for ch in str:
    if ch == ' ':
      new_str = new_str + '-'
    else:
      new_str = new_str + ch
  return new_str
str = 'python is easy'
res = replace_space(str)
print(res)
    









