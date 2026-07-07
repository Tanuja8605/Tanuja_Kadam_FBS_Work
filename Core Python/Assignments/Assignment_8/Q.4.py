# 4. Sum of all odd numbers between 1 to n
def odd_sum():
    n = int(input("Enter value of n: "))
    total = 0

    for i in range(1, n + 1):
        if i % 2 != 0:
            total += i

    return total

ans = odd_sum()
print("Summation is:", ans)