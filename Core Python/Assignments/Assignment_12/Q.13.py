# 14. Python Program to count the occurrences of ach word in a string.
def word_occurence(s):
  word = s.split()
  d = {}
  for word in word:
    if word in d:
      d[word] += 1
    else:
      d[word] = 1
  for key, value in d.items():
    print(key, ":", value)
    
s = 'python is easy and python is programming'
word_occurence(s)

  