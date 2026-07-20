# 8. Write a Python program to find all the anagrams and group them
# together from a given list of strings.

def Anagram_grp(li):

  d = {}
  for i in li:
    key = ''.join(sorted(i))

    if key in d:
      d[key].append(i)
    else:
       d[key] = [i]
  
  for grp in d.values():
    print(grp)

li = ["cat", "act", "dog", "god", "tac"]
Anagram_grp(li)







     

