# 4. Python Program to Generate a Dictionary that Contains Numbers (between 1
# and n) in the Form (x,x*x).

def square(n):
    new_dict = {}

    for i in range(1, n + 1):
        new_dict[i] = i * i

    return new_dict

n = int(input("Enter value of n: "))
res = square(n)
print(res)

