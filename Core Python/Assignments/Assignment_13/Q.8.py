# 8. Python Program to Count the Frequency of Words Appearing in a String Using a Dictionary.

def word_frequency(di):

  words = di.split()
  d = {}

  for word in words:

    if word in d:
      d[word] += 1
    else:
      d[word] = 1

  for key , value in d.items():
    print(key , ':',value)

di = 'python is easy and python is simple'
word_frequency(di)


