def digit_sum(x):
    total = 0
    while x > 0:
        d = x % 10
        total += d
        x = x // 10
    return total

num = int(input('Enter num: '))
res = digit_sum(num)
print('sum is:',res)
