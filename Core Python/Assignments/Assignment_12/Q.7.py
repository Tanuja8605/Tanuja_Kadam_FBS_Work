# 7. Python Program to Calculate the Length of a String Without Using a
#  Library Function

def count_len(s):
    count = 0
    for ch in s:
        count += 1
    return count

s = input("Enter text: ")
res = count_len(s)
print(res)









