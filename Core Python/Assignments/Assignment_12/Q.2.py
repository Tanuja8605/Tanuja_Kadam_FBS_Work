# 2. Python Program to Remove the nth Index Character from a Non-Empty
# String

def remove_nth(s):
  li = list(s)
  li.pop()
  s = ''.join(li)
  return s
s = 'firstbit'
res = remove_nth(s)
print('After removing nth:',res)
