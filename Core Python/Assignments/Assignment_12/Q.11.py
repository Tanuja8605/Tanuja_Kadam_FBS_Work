# 12. Python Program to count number of lowercase characters in a string.

def count_lowercse(s):
  count = 0
  for ch in s:
    if ch > 'a' and ch < 'z':
      count += 1
  return count
s = 'FirstBit'
res = count_lowercse(s)
print(res)

