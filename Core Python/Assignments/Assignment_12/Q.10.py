# 10.Python Program to Take in Two Strings and Display the Larger String
# without Using Built-in Functions
def greater_string(s1,s2):
  count1 = 0
  for i in s1:
    count1 += 1

  count2 = 0
  for i in s2:
      count2+=1
  if count1 > count2:
     print(s1)
  elif count2 > count1:
     print(s2)
  else:
     print("Both strings have equal length")

s1 = 'python'
s2 = 'firstbit'
greater_string(s1,s2)
