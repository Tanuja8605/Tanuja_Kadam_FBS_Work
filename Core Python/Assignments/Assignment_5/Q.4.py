# 4. WAP to print Armstrong number within a given range

start = int(input("Enter starting number: "))
stop = int(input("Enter ending number: "))

for num in range(start, stop + 1):

    temp = num
    count = 0

    while temp > 0:
        count += 1
        temp = temp//10

    temp = num
    sum = 0

    while temp > 0:
        digit = temp % 10
        sum += digit ** count
        temp = temp//10

    if sum == num:
        print(num)