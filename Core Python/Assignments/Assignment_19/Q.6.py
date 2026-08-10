# 6. Use a dictionary comprehension to count the length of each word
# in a sentence (take input from user)

di = input("Enter any string:")
s = {i:len(i) for i in di.split()}
print(s)