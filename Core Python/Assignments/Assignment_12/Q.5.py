# 5. Python Program to Count the Number of Vowels in a String

def count_vowels(s):
    vowels = []
    count = 0

    for ch in s:
        if ch in "aeiouAEIOU" and ch not in vowels:
            vowels.append(ch)
            count += 1

    return count

s = input("Enter a string: ")
print(count_vowels(s))











