# 5. Write a Python program to find the longest common prefix of all
# strings. Use the Python set.

def common_prefix(li):
   
   min_len = len(li[0])

   for word in li:

    if len(word) < min_len:
      min_len = len(word)

   prefix = ''

   for i in range(min_len):
      ch_set = set()

      for word in li:
       ch_set.add(word[i])

      if len(ch_set) == 1:
        prefix = prefix + li[0][i]
      else:
       len(ch_set) > 1
       break

   print(prefix)




    


li = ['flower','flow','flight']
common_prefix(li)