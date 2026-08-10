# 5. Find all of the words in a string that are less than 5 letters (take
# input from user)

s = input("Enter any string: ")

res = [i for i in s.split() if len(i) < 5]

print(res)