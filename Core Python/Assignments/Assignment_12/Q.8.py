# 8. Python Program to Remove the Characters of Odd Index Values in a
# String
def remove_ch(s):
  new_s = ''
  for i in range(len(s)):
    if i % 2 == 0:
      new_s = new_s + s[i]
  return new_s
s = input('Enter string:')
res = remove_ch(s)
print(res)
 
      


