# 9. Python Program to Calculate the Number of Words and the Number of
# Characters Present in a String
def num_words_char(s):
  word_count = 1
  char_count = 0
  for ch in s:
    char_count += 1
    if ch == ' ':
      word_count += 1
  return word_count,char_count

str = 'Python is easy'
words,character = num_words_char(str)
print('chracter count:',character)
print('wordcount:',words)

    
