# 4. Remove all of the vowels in a string (take input from user)
s = input("Enter any string:")
new_s = ''.join([i for i in s if i not in 'aeiouAEIOU'])
print(new_s)
