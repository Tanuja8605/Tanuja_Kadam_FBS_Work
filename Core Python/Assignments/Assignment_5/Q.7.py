# 6. Write a program to print first n prime numbers.
# a. 1! + 2! + 3! + 4! + .....n!

# n = int(input("Enter n: "))
# sum = 0
# fact = 1

# for i in range(1, n + 1):
#     fact = fact * i
#     sum = sum + fact
#     print(f"{i}! = {fact}")

# print("Sum =", sum)


# b. N + N^2 + N^3+N^4 .....+N^N (here ^ means exponent)
# n = int(input('Enter N: '))
# sum = 0

# for i in range(1, n + 1):
#     term = n ** i
#     sum += term
#     print(f'N^{i} = {term}')

# print("Sum =", sum)


# c. Find the sum of a geometric series from 1 to n where the common ratio is 2.

# n = int(input("Enter n: "))
# term = 1
# sum = 0

# for i in range(n):
#     print(term)
#     sum += term
#     term *= 2

# print("Sum is:", sum)


# d. S = a + a2 / 2 + a3 / 3 + ...... + a10 / 10

a = int(input("Enter a: "))
sum = 0

for i in range(1, 11):
    term = (a ** i) / i
    print(f"a^{i}/{i} = {term}")
    sum += term

print("Sum =", sum)
