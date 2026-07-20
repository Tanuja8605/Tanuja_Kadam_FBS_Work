# 3. Write a Python program to find all the unique words and count the
# frequency of occurrence from a given list of strings. Use Python set
# data type.

def unique_words(ss):
  unique_words = set(ss)
  for word in unique_words:
    count = 0
    for i in ss:
      if i == word:
        count += 1
    print(word,':',count)

      
li = ["python","is","easy","python","python"]
unique_words(li)