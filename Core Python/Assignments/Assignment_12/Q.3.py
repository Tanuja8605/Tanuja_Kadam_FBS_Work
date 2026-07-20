# 3. Python Program to Detect if Two Strings are Anagrams

def isAnagram(s1,s2):
  if sorted(s1) == sorted(s2):
    print('string is Anagram')
  else:
    print('String is not Anagram')

s1 = 'listen'
s2 = 'silent'
isAnagram(s1,s2)