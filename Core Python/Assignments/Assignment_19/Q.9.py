# 2. Implement a generator function that yields palindrome numbers.
# Palindromes are numbers that read the same backward as forward
# (e.g., 121, 1331). Generate palindromes lazily and infinitely.

def palindrome(num):
    while True:
        temp = num
        rev = 0

        while temp > 0:
            d = temp % 10
            rev = rev * 10 + d
            temp = temp // 10

        if rev == num:
            yield num

        num += 1


p = palindrome(10)

print(next(p))
print(next(p))
print(next(p))
print(next(p))